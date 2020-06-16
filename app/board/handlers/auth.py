from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from board.models import Dashboard, Figure
from board.forms import SignupForm


def sign_up(request):
    form = SignupForm()
    if request.method == 'POST':
        logout(request)
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password_again = form.cleaned_data['password_again']
            email    = form.cleaned_data.get('email')
            user = User.objects.filter(username=username).first()
            if user is not None:
                form.add_error('username', 'User already exists!')
            elif password != password_again:
                form.add_error('password_again', 'Passwords mismatch!')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
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
        user = authenticate(username=username, password=password,
                            backend='django.contrib.auth.backends.ModelBackend')
        if user is not None:
            login(request, user,
                  backend='django.contrib.auth.backends.ModelBackend')
            redirect_url = request.GET.get('next')
            if redirect_url:
                return redirect(request.GET['next'])
            else:
                return HttpResponseRedirect(reverse('dashboards'))
        else:
            error = 'Invalid credentials!'
    else:
        error = None
    return  HttpResponse(render(request, 'board/login.html', {'error': error}))
