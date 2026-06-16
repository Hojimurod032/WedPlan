from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView

from apps.forms import RegisterForm, LoginForm
from apps.models import User


class LoginViewList(FormView):
    form_class = LoginForm
    template_name = 'Auth/Login.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "Hush kelibsiz")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_messege in form.errors.values():
            messages.error(self.request, error_messege)
        return super().form_invalid(form)


class RegisterViewList(CreateView):
    form_class = RegisterForm
    queryset = User.objects.all()
    template_name = 'Auth/Register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Muffaqaiyati royxatdan otildi")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_messege in form.errors.values():
            messages.error(self.request, error_messege)
        return super().form_invalid(form)


class HomeViewList(TemplateView):
    template_name = 'Home.html'


class InviteCreateList(TemplateView):
    template_name = 'InviteCreate.html'


class InviteShareView(TemplateView):
    template_name = 'Intiniteshare.html'


class VenderDetailViewList(TemplateView):
    template_name = 'VendorDetail.html'


class VenderListView(TemplateView):
    template_name = 'VendorList.html'


class DashboardViewList(TemplateView):
    template_name = 'Dashboard.html'


class TaskViewList(TemplateView):
    template_name = 'TasksList.html'


class GuestAddCreateView(TemplateView):
    template_name = 'GuestAdd.html'


class GuestListView(TemplateView):
    template_name = 'GuestList.html'


class BudgetListView(TemplateView):
    template_name = 'BudgetList.html'
