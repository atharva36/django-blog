from django.contrib.auth import forms
from django.views.generic.edit import CreateView, UpdateView
from blog.models import Profile
from django.contrib.auth.views import PasswordChangeView
from accounts.forms import EditSettingsForm, PasswordChangingForm, ProfilePageForm, SignUpForm
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# Create your views here.

class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "User registered successfully! Please login to continue"


class UserEditView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Settings edited successfully!"

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html',{})

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        context['page_user']= page_user
        return context
     
class EditProfileView(SuccessMessageMixin, generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url']
    success_url = reverse_lazy('home')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Profile edited successfully!"

class CreateProfileView(SuccessMessageMixin, CreateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    form_class = ProfilePageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Profile created successfully! You can now start posting!"
    