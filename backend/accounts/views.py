# from django.shortcuts import render
from rest_framework.generics import CreateAPIView
# from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
class CreateAPIUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
