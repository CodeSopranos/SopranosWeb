from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Dashboard, Figure

from .transport.RIAparser import RIAparser


def dashboard(request):
    boards = Dashboard.objects.all()
    context = {'dashboards': boards}
    return HttpResponse(render(request, 'board/dashboard.html', context))


def parse_theme(request):
    ria_parser = RIAparser()
    text = ria_parser.get(tag=request.POST['theme'], offset=1)
    boards = Dashboard.objects.all()
    context = {'dashboards': boards, 'parsed_text': 'LOL'}
    print(context)
    return HttpResponse(render(request, 'board/dashboard.html'), context)