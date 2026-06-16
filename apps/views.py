from django.shortcuts import render
from django.views.generic import TemplateView


class LoginViewList(TemplateView):
    template_name = 'Auth/Login.html'

class RegisterViewList(TemplateView):
    template_name = 'Auth/Register.html'


class HomeViewList(TemplateView):
    template_name = 'Home.html'


class GuestAddCreateView(TemplateView):
    template_name = 'GuestAdd.html'


class GuestListView(TemplateView):
    template_name = 'GuestList.html'

