from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, View
from django.shortcuts import redirect
from .forms import CustomUserCreationForm 

class LoginView(FormView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class SignupView(CreateView):
    form_class = CustomUserCreationForm  # Use the custom form
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")
    
class CustomPasswordResetView(PasswordResetView):
    template_name = "accounts/forgot_password.html"
    email_template_name = "accounts/password_reset_email.html"
    success_url = reverse_lazy("login")
    form_class = PasswordResetForm

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("login")
    form_class = SetPasswordForm

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("dashboard")
    form_class = PasswordChangeForm

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
