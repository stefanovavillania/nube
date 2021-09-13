from django.contrib.auth.models import User, Permission
from django.shortcuts import render
from django.views.generic import View
from .serializers import UserSerializer, PermissionSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

class IndexView(View):
    template = 'base.html'
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, self.template, {'users': users})

class ListUserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

class UpdateUserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.get(id = self.kwargs.get('pk')))
        return Response(serializer.data, status =status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.get(id = self.kwargs.get('pk')), data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

class DeleteUserAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
