from django.contrib import admin
from django.urls import path

from apps.views import *

urlpatterns = [
    path('', HomeViewList.as_view(), name="home"),
    path('register', RegisterViewList.as_view(), name="register"),
    path('login', LoginViewList.as_view(), name="login"),
    path('vendordetail' , VenderListView.as_view(), name="vendor-detail"),
    path('vendorlist' , VenderListView.as_view(), name="vendor-list"),
    path('tasklist' , TaskListView.as_view(), name="task-list"),
    path('Dashboard' , DashboardView.as_view(), name="dashboard"),

]
