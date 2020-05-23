from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth.models import User
from .models import Dashboard, Figure

from .transport.RIAparser import RIAparser
from .analyzer.Frequency import Frequency

def sign_up(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('dashboards'))
    return HttpResponse(render(request, 'board/signup.html', {'form': form}))

def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboards'))

def sign_in(request):
    if request.method == 'POST':
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'])
        else:
            error = 'Invalid credentials!'
    else:
        error = None
    return  HttpResponse(render(request, 'board/login.html', {'error': error}))


@login_required(login_url='/board/signin/')
def show_dashboards(request, additional_context={}):
    user = get_object_or_404(User, pk=request.user.id)
    boards = user.dashboard_set.order_by('-created_at')
    context = {'dashboards': boards, **additional_context}
    return HttpResponse(render(request, 'board/dashboards.html', context))

@login_required(login_url='/board/signin/')
def create_dashboard(request):
    user = User.objects.get(pk=request.user.id)
    board_name = request.POST['board_name']
    theme = request.POST['theme']
    try:
        n_offset = int(request.POST['n_articles'])
    except:
        n_offset = None

    error_message = None
    if not board_name or board_name.isspace():
        error_message = 'Please provide non-empty dashboard name!'
    if not theme or theme.isspace():
        error_message = 'Please provide non-empty dashboard theme!'
    if not n_offset or n_offset < 1 or n_offset > 10:
        error_message = 'Please provide a postive number of pages!'
    if error_message:
        context = {'error': error_message, 'board_name':board_name, 'theme': theme}
        return show_dashboards(request, additional_context=context)
    ria_parser = RIAparser()
    articles = ria_parser.get(tag=theme, n=20, offset=n_offset)
    Dashboard.objects.create(owner=user, name=board_name, theme=theme, data=articles)
    return HttpResponseRedirect(reverse('dashboards'))

@login_required(login_url='/board/signin/')
def get_dashboard(request, dashboard_id, additional_context={}):
    user = User.objects.get(pk=request.user.id)
    dashboard = get_object_or_404(Dashboard, pk=dashboard_id)
    if dashboard.owner == user:
        figures = dashboard.figure_set.order_by('-modify_at')
        context = { 'dashboard': dashboard,
                    'dashboard_data':dashboard.data[:10],
                    'figures': figures,
                    **additional_context}
        return HttpResponse(render(request, 'board/dashboard.html', context))
    else:
        return HttpResponseRedirect(reverse('dashboards'))

@login_required(login_url='/board/signin/')
def add_figure(request, dashboard_id):
    try:
        figure_type = request.POST['figure_type']
    except:
        error_message = 'Please select figure type!'
        context = {'error': error_message}
        return get_dashboard(request, dashboard_id, additional_context=context)
    dashboard = get_object_or_404(Dashboard, pk=dashboard_id)
    analyzed_data = {'lol':1}
    if figure_type == 'Frequency analysis':
        analyzer = Frequency(dashboard.data)
        analyzer.preprocess()
        analyzed_data = analyzer.analyze().to_dict()
    Figure.objects.create(dashboard=dashboard, type=figure_type, data=analyzed_data, params={'lol':1})
    return HttpResponseRedirect(reverse('dashboard_by_id',
                                kwargs={'dashboard_id': dashboard_id}))
