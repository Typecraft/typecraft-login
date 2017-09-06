# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.request import Request

from api.serializers import UserSerializer


def index(request):
    return redirect(reverse(login_user))

@csrf_exempt
def login_user(request):
    """
    Logs in a user
    :param request:
    :type request: Request
    :return:
    """
    if request.method == 'GET':
        return render(request, template_name='users/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return HttpResponse(json.dumps(serializer.data), content_type='application/json')
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
