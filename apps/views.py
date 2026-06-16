from django.shortcuts import render
from django.views.generic import TemplateView


class LoginViewList(TemplateView):
    template_name = 'Auth/Login.html'

class RegisterViewList(TemplateView):
    template_name = 'Auth/Register.html'


class HomeViewList(TemplateView):
    template_name = 'Home.html'

class InviteCreateList(TemplateView):
    template_name = 'InviteCreate.html'

class InviteShareList(TemplateView):
    template_name = 'Intiniteshare.html'