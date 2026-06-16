from django.contrib import admin
from django.urls import path

from apps.views import *

urlpatterns = [
    path('', HomeViewList.as_view(), name="home"),
    path('register', RegisterViewList.as_view(), name="register"),
    path('login', LoginViewList.as_view(), name="login"),
    path('dashboard', DashboardViewList.as_view(), name="dashboard"),
    path('tasks', TaskViewList.as_view(), name="tasks"),
]
