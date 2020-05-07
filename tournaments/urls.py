from django.urls import path

from .views import TournamentListView, TournamentDetailView, TournamentRegistrationView, TournamentUnregisterView, TournamentFullRegistrationView

urlpatterns = [
    path('', TournamentListView.as_view(), name='list'),
    path('register/', TournamentFullRegistrationView.as_view(), name="fullregister"),
    path('<slug:slug>/', TournamentDetailView.as_view(), name='detail'),
    path('<slug:slug>/register', TournamentRegistrationView.as_view(), name='register'),
    path('<slug:slug>/unregister', TournamentUnregisterView.as_view(), name='unregister'),
    # path('history/', TournamentHistory.as_view(), name='history')

]
