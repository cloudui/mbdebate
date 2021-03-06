from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class CoachesPageView(TemplateView):
    template_name = 'coaches.html'

class TemporaryTournament(TemplateView):
    template_name = 'blairbebate.html'