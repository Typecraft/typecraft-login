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


def index(request):
    return redirect(reverse(login_user))


@csrf_exempt
def login_user(request):
    """
    Logs in a user.

    :param request: The request
    :type request: Request
    :return:
    """
    if request.method == 'GET':
        return render(request, template_name='users/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.GET.get('next')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return HttpResponse(json.dumps(serializer.data), content_type='application/json')
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
        return render(request, template_name='users/login.html')

    if 'next' in request.GET or not request.is_ajax():
        response = redirect(request.GET.get('next', '/'))
    else:
        response = redirect(reverse(login_user))

    logout(request)
    return response
