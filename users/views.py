# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.request import Request

from api.serializers import UserSerializer
from users.forms import UserCreationForm


def _handle_default_content_negotiation(request, user):
    """
    We handle content negotiation in the same way for the signup and login views,
    which is encapsulated in this method.

    :param request:
    :param user:
    :return:
    """
    if 'next' in request.GET:
        return redirect(request.GET.get('next', '/'))

    for accept in request.META.get('HTTP_ACCEPT', 'application/json').split(','):
        if accept == 'text/html':
            return redirect('/')
        elif accept == 'application/json':
            serializer = UserSerializer(user, context={'request': request})
            return HttpResponse(json.dumps(serializer.data), content_type='application/json')

    # Return json by default
    serializer = UserSerializer(user, context={'request': request})
    return HttpResponse(json.dumps(serializer.data), content_type='application/json')


def index(request):
    if 'next' in request.GET:
        return redirect(request.GET.get('next', '/'))

    if request.user.is_authenticated:
        return render(request, template_name='users/authenticated.html')
    else:
        return redirect(reverse(login_user))


@csrf_exempt
def login_user(request):
    """
    Logs in a user.

    :param request: The request
    :type request: Request
    :return:
    """
    if request.user.is_authenticated:
        return _handle_default_content_negotiation(request, request.user)

    if request.method == 'GET':
        return render(
            request,
            template_name='users/login.html',
            context={'next': request.GET.get('next')})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            return _handle_default_content_negotiation(request, user)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
def logout_user(request):
    """
    Logs out a user.

    :param request:
    :type request: Request
    :return:
    """

    if 'next' in request.GET or not request.is_ajax():
        response = redirect(request.GET.get('next', '/'))
    else:
        response = redirect(reverse(login_user))

    logout(request)
    return response


@csrf_exempt
def signup_user(request):
    """
    Logs out a user.

    :param request:
    :type request: Request
    :return:
    """
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, context={'form': form, 'next': request.GET.get('next')}, template_name='users/signup.html')

    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)

        return _handle_default_content_negotiation(request, user)
    else:
        return render(request, context={'form': form, 'next': request.GET.get('next')}, template_name='users/signup.html')
