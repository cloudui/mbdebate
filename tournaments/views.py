from django.shortcuts import render

from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy, reverse
from .forms import TournamentRegistrationForm, TournamentUnregisterForm, TournamentFullRegistrationForm

from .models import Tournament

class TournamentListView(ListView):
    model = Tournament
    template_name = 'tournament_list.html'
    login_url = 'account_login'

class TournamentFullRegistrationView(LoginRequiredMixin, ListView, FormView):
    
    model = Tournament
    form_class = TournamentFullRegistrationForm

    template_name = "tournament_full_registration.html"
    success_url = reverse_lazy('list')
    login_url = 'account_login'
        
    def form_valid(self, form):
        form_results = form.cleaned_data['tournaments']
        for tournament in form_results:
            Tournament.register(self.request.user, tournament)

        return super(TournamentFullRegistrationView, self).form_valid(form)
        


class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'tournament_detail.html'

class TournamentRegistrationView(LoginRequiredMixin, FormView, DetailView):
    model = Tournament
    form_class = TournamentRegistrationForm
    template_name = 'tournament_registration.html'
    success_url = reverse_lazy('list')
    login_url = 'account_login'

    def form_valid(self, form):
        tournament_slug = self.kwargs['slug']
        tourney = Tournament.objects.get(slug=tournament_slug)
        Tournament.register(self.request.user, tourney)
        return super(TournamentRegistrationView, self).form_valid(form)

class TournamentUnregisterView(LoginRequiredMixin, FormView, DetailView):
    model = Tournament
    form_class = TournamentUnregisterForm
    template_name = 'tournament_unregister.html'
    success_url = reverse_lazy('list')
    login_url = 'account_login'

    def form_valid(self, form):
        
        tournament_slug = self.kwargs['slug']
        tourney = Tournament.objects.get(slug=tournament_slug)
        Tournament.unregister(self.request.user, tourney)
        return super(TournamentUnregisterView, self).form_valid(form)


