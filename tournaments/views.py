from django.shortcuts import render

from django.views.generic import ListView, DetailView, FormView

from django.urls import reverse_lazy
from .forms import TournamentRegistrationForm, TournamentUnregisterForm

from .models import Tournament

class TournamentListView(ListView):
    model = Tournament
    template_name = 'tournament_list.html'
    # login_url = 'login'

class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'tournament_detail.html'

class TournamentRegistrationView(FormView):
    form_class = TournamentRegistrationForm
    template_name = 'tournament_registration.html'
    success_url = reverse_lazy('list')
    

    def form_valid(self, form):
        tournament_slug = self.kwargs['slug']
        tourney = Tournament.objects.get(slug=tournament_slug)
        Tournament.register(self.request.user, tourney)
        return super(TournamentRegistrationView, self).form_valid(form)

class TournamentUnregisterView(FormView):
    form_class = TournamentUnregisterForm
    template_name = 'tournament_unregister.html'
    success_url = reverse_lazy('list')
    

    def form_valid(self, form):
        tournament_slug = self.kwargs['slug']
        tourney = Tournament.objects.get(slug=tournament_slug)
        Tournament.unregister(self.request.user, tourney)
        return super(TournamentUnregisterView, self).form_valid(form)
