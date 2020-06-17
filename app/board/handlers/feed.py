from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth.models import User
from board.models import Dashboard, Figure


def list_dashboards(request, additional_context={}):
    boards  = Dashboard.objects.all().filter(private=False).order_by('-created_at')
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        total_boards = len(user.dashboard_set.order_by('-created_at'))
    else:
        total_boards = 0
    context = {'dashboards': boards,
               'total_boards': total_boards,
               **additional_context}
    return HttpResponse(render(request, 'board/feed.html', context))
