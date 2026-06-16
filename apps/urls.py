from django.contrib import admin
from django.urls import path

from apps.views import *

urlpatterns = [
    path('', HomeViewList.as_view(), name="home"),
    path('register', RegisterViewList.as_view(), name="register"),
    path('login', LoginViewList.as_view(), name="login"),
    path('guest-add', GuestAddCreateView.as_view(), name='guest-add'),
    path('guest-list', GuestListView.as_view(), name='guest-add')
]
