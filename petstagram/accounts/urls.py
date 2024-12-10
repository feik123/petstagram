from django.contrib.auth.views import LogoutView
from django.urls import path, include

from petstagram.accounts import views
from petstagram.accounts.views import AppUserRegisterView, AppUserLoginView

urlpatterns = [
    path('login/', AppUserLoginView.as_view(), name='login'),
    path('register/', AppUserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailView.as_view(), name='profile-details'),
        path('edit', views.ProfileEditView.as_view(), name='profile-edit'),
        path('delete', views.profile_delete, name='profile-delete'),
    ]))
]