from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic import DetailView

from .models import Tournament

class TournamentListView(ListView):
    model = Tournament
    template_name = 'tournament_list.html'
    # login_url = 'login'

class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'tournament_detail.html'

    