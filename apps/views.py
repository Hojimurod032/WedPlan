from django.shortcuts import render
from django.views.generic import TemplateView


class LoginViewList(TemplateView):
    template_name = 'Auth/Login.html'

class RegisterViewList(TemplateView):
    template_name = 'Auth/Register.html'


class HomeViewList(TemplateView):
    template_name = 'Home.html'


class VenderDetailViewList(TemplateView):
    template_name = 'VendorDetail.html'


class VenderListView(TemplateView):
    template_name = 'VendorList.html'



class DashboardViewList(TemplateView):
    template_name = 'Dashboard.html'

class TaskViewList(TemplateView):
    template_name = 'Task.html'
class GuestAddCreateView(TemplateView):
    template_name = 'GuestAdd.html'


class GuestListView(TemplateView):
    template_name = 'GuestList.html'

