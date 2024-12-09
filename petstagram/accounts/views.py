from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from petstagram.accounts.forms import AppUserCreationForm, ProfileEditForm
from petstagram.accounts.models import Profile

UserModel = get_user_model()

class AppUserLoginView(LoginView):
    template_name = "accounts/login-page.html"


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        user = form.save()
        login(self.request, self.object)

        return response

def profile_delete(request, pk:int):
    return render(request, 'accounts/profile-delete-page.html')

def profile_details(request, pk:int):
    return render(request, 'accounts/profile-details-page.html')

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )
