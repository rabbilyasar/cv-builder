# from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CreateAPIUser, LoginAPIUser, LogoutAPIUser, UserDetailAPIView


# from . import views

app_name = "users_app"

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/create/', CreateAPIUser.as_view(), name='create_user'),
    path('api/accounts/login/', LoginAPIUser.as_view(), name='login_user'),
    path('api/accounts/logout/', LogoutAPIUser.as_view(), name='logout'),
    path('api/accounts/detail/<pk>/', UserDetailAPIView.as_view(), name="user_detail"),
]
