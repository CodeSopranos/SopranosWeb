from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Dashboard, Figure

from .transport.RIAparser import RIAparser


def show_dashboards(request, additional_context={}):
    boards = Dashboard.objects.all()
    context = {'dashboards': boards, **additional_context}
    return HttpResponse(render(request, 'board/dashboards.html', context))


def create_dashboard(request):
    board_name = request.POST['board_name']
    theme = request.POST['theme']
    n_articles = int(request.POST['n_articles'])

    error_message = None
    if not board_name or board_name.isspace():
        error_message = 'Please provide non-empty dashboard name!'
    if not theme or theme.isspace():
        error_message = 'Please provide non-empty dashboard theme!'
    if n_articles < 1:
        error_message = 'Please provide a postive number of articles!'
    elif not n_articles:
        n_articles = 5
    if error_message:
        context = {'error': error_message, 'board_name':board_name, 'theme': theme}
        return show_dashboards(request, additional_context=context)
    ria_parser = RIAparser()
    articles = ria_parser.get(tag=theme, n=n_articles, offset=1)
    Dashboard.objects.create(name=board_name, theme=theme, data=articles)
    return HttpResponseRedirect('dashboards')


def get_dashboard(request, dashboard_id, additional_context={}):
    dashboard = get_object_or_404(Dashboard, pk=dashboard_id)
    figures = dashboard.figure_set.order_by('-modify_at')
    context = {'dashboard': dashboard, 'figures': figures,  **additional_context}
    return HttpResponse(render(request, 'board/dashboard.html', context))

def add_figure(request, dashboard_id):
    dashboard = get_object_or_404(Dashboard, pk=dashboard_id)
    ria_parser = RIAparser()
    articles = ria_parser.get(tag='Прага', offset=1)
    return HttpResponse(articles[0]['text'])
