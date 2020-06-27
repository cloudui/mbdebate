from django.urls import path
from .views import HomePageView, AboutPageView, CoachesPageView, TemporaryTournament

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('coaches/', CoachesPageView.as_view(), name='coaches'),
    path('blairbebate/', TemporaryTournament.as_view(), name='temporary'),
]