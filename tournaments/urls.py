from django.urls import path

from .views import TournamentListView, TournamentDetailView

urlpatterns = [
    path('', TournamentListView.as_view(), name='list'),
    path('<slug:slug>/', TournamentDetailView.as_view(), name='detail'),
    # path('history/', TournamentHistory.as_view(), name='history')

]
