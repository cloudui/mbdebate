from django.db import models

from django.contrib.auth.models import AbstractUser

# from tournaments import models as tourney_models

class CustomUser(AbstractUser):
    # tournaments = models.ManyToManyField(tourney_models.Tournament, blank=True)
    pass

    


    


