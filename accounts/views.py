from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
#
# class PasswordReset(PasswordResetView):
#     # from_email = 'email-username@hotmail.com'
#     success_url = reverse_lazy('account:password_reset_done')
#
#
# class PasswordResetConfirm(PasswordResetConfirmView):
#     success_url = reverse_lazy('account:password_reset_complete')
