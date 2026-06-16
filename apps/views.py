from django.shortcuts import render
from django.views.generic import TemplateView


class LoginViewList(TemplateView):
    template_name = 'Auth/Login.html'

class RegisterViewList(TemplateView):
    template_name = 'Auth/Register.html'


class HomeViewList(TemplateView):
    template_name = 'Home.html'


class DashboardViewList(TemplateView):
    template_name = 'Dashboard.html'

class TaskViewList(TemplateView):
    template_name = 'Task.html'    