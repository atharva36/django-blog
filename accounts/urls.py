from django import views
from django.urls import path
from .views import CreateProfileView, EditProfileView, PasswordsChangeView, ShowProfileView, UserEditView, UserRegisterView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('edit_settings/', UserEditView.as_view(), name='edit_settings'),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success.',views.password_success, name='password_success'),
    path('<int:pk>/profile/',ShowProfileView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile/', EditProfileView.as_view(), name='edit_profile_page'),
    path('create_profile/',  CreateProfileView.as_view(), name='create_profile_page'),
]
