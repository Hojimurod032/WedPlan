from django.contrib import admin
from django.urls import path

from apps.views import *

urlpatterns = [
    path('', HomeViewList.as_view(), name="home"),
    path('register', RegisterViewList.as_view(), name="register"),
    path('login', LoginViewList.as_view(), name="login"),
    path('invite-create', InviteCreateList.as_view(), name="invite-create"),
    path('invite-share', InviteShareList.as_view(), name="invite-share")
]
