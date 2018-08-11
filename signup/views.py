

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import  Response
from rest_framework import status
# Create your views here.

class UserCreate(APIView):

    """"
        Creating the user
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        permissin_classes = (IsAuthenticated,)
        if serializer.is_valid():
            user= serializer.save()
            if user:
                token = Token.object.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
