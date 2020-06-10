from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth.models import User
from board.models import Dashboard, Figure

from board.analyzer.Frequency import Frequency

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
