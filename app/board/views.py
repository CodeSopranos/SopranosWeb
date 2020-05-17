from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Dashboard, Figure


def dashboard(request):
    boards = Dashboard.objects.all()
    context = {'dashboards': boards}
    return HttpResponse(render(request, 'board/dashboard.html', context))
