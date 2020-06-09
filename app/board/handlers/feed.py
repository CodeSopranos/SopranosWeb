from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth.models import User
from board.models import Dashboard, Figure


def list_dashboards(request, additional_context={}):
    boards  = Dashboard.objects.all().filter(private=False)
    context = {'dashboards': boards, **additional_context}
    return HttpResponse(render(request, 'board/feed.html', context))
