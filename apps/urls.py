from django.contrib import admin
from django.urls import path

from apps.views import *

urlpatterns = [
    path('', HomeViewList.as_view(), name="home"),
    path('register', RegisterViewList.as_view(), name="register"),
    path('login', LoginViewList.as_view(), name="login"),
    path('guest-add', GuestAddCreateView.as_view(), name='guest-add'),
    path('guest-list', GuestListView.as_view(), name='guest-add'),
    path('vendordetail' , VenderListView.as_view(), name="vendor-detail"),
    path('vendorlist' , VenderListView.as_view(), name="vendor-list"),
    path('tasklist' , TaskView.as_view(), name="task-list"),
    path('Dashboard' , DashboardView.as_view(), name="dashboard"),
    path('tasklist' , TaskView.as_view(), name="task-list"),
    path('Dashboard' , DashboardView.as_view(), name="dashboard"),

    path('tasklist' , TaskViewList.as_view(), name="task-list"),
    path('Dashboard' , DashboardViewList.as_view(), name="dashboard"),
    path('invite-create', InviteCreateList.as_view(), name="invite-create"),
    path('invite-share', InviteShareView.as_view(), name="invite-share")
]
