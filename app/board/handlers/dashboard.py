from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth.models import User
from board.models import Dashboard, Figure

from board.transport.RIAparser import RIAparser
from board.transport.Twiparser import TWITTERparser

import numpy as np

@login_required(login_url='/board/signin/')
def show_dashboards(request, additional_context={}):
    user = get_object_or_404(User, pk=request.user.id)
    boards = user.dashboard_set.order_by('-created_at')
    context = {'dashboards': boards, 'total_boards': len(boards), **additional_context}
    return HttpResponse(render(request, 'board/dashboards.html', context))


def view_dashboard(request, dashboard_id, additional_context={}):
    dashboard = get_object_or_404(Dashboard, pk=dashboard_id)
    figures = dashboard.figure_set.order_by('-modify_at')
    context = { 'dashboard': dashboard,
                'dashboard_data':np.random.permutation(dashboard.data)[:2],
                'figures': figures,
                **additional_context}
    return HttpResponse(render(request, 'board/view_dashboard.html', context))


@login_required(login_url='/board/signin/')
def get_dashboard(request, dashboard_id, additional_context={}):
    user = User.objects.get(pk=request.user.id)
    dashboard = get_object_or_404(Dashboard, pk=dashboard_id)
    if dashboard.owner == user:
        figures = dashboard.figure_set.order_by('-modify_at')
        context = { 'dashboard': dashboard,
                    'dashboard_data': np.random.permutation(dashboard.data)[:3],
                    'figures': figures,
                    **additional_context}
        return HttpResponse(render(request, 'board/dashboard.html', context))
    else:
        return HttpResponseRedirect(reverse('dashboards'))


@login_required(login_url='/board/signin/')
def create_dashboard(request):
    user = User.objects.get(pk=request.user.id)
    board_name = request.POST['board_name']
    theme = request.POST['theme']
    try:
        if request.POST['is_private']:
            is_private = True
    except:
        is_private = False
    try:
        n = int(request.POST['n_articles'])
    except:
        n = 5

    error_message = None
    if not board_name or board_name.isspace():
        error_message = 'Please provide non-empty dashboard name!'
    if not theme or theme.isspace():
        error_message = 'Please provide non-empty dashboard theme!'
    if not n or n < 1 or n > 10:
        error_message = 'Please provide a postive number of pages!'
    if error_message:
        context = {'error': error_message, 'board_name':board_name, 'theme': theme}
        return  HttpResponseRedirect(reverse('dashboards'))

    # ria_parser = RIAparser()
    # articles = ria_parser.get(tag=theme, n=20, offset=n)
    twi_parser = TWITTERparser()
    articles   = twi_parser.get(tag=theme, n=n)
    Dashboard.objects.create(owner=user,
                             name=board_name,
                             theme=theme,
                             data=articles,
                             private=is_private)
    return HttpResponseRedirect(reverse('dashboards'))


@login_required(login_url='/board/signin/')
def add_description(request, dashboard_id):
    text = request.POST['description']
    dashboard = get_object_or_404(Dashboard, pk=dashboard_id)
    dashboard.description = text
    dashboard.save()
    return HttpResponseRedirect(reverse('dashboard_by_id',
                                kwargs={'dashboard_id': dashboard_id}))
