# from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.views import APIView
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
class CreateAPIUser(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class LoginAPIUser(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):

        if not request.user.is_authenticated:
            return Response({"message": "You are already logged in"})
        else:

            user = authenticate(
                username=self.request.data["username"],
                password=self.request.data['password']
            )
            if user is not None:
                login(request, user)
                return Response({"message": "Login Exitoso"})

            else:
                return Response({"message": "Verify your username or password"})


class LogoutAPIUser(APIView):

    def post(self, request):
        logout(request)

        return Response({"message": "Logged out Correctly"})


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):

    # Pending on handling permissions
    serializer_class = UserSerializer
    queryset = User.objects.all()
