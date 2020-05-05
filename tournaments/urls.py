from django.urls import path

from .views import TournamentListView

urlpatterns = [
    path('list/', TournamentListView.as_view(), name='list'),
    # path('history/', TournamentHistory.as_view(), name='history')

]
