from django.contrib import admin

# Register your models here.

from .models import Tournament


class TournamentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tournament, TournamentAdmin)
