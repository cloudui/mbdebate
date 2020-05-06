from django.shortcuts import render


from django.urls import reverse_lazy

from django.views import generic

from .forms import CustomUserCreationForm


class ProfilePageView(generic.TemplateView):
    template_name = 'profile.html'

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



        

