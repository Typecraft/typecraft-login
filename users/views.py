# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(['GET', 'POST'])
def login_user(request):
    """
    Logs in a user
    :param request:
    :type requset: Request
    :return:
    """
    if request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username, password)
        if user is not None:
            login(request, user)
            return Response()
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
