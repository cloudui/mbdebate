from django.contrib import admin

# Register your models here.

from .models import Tournament


class TournamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tournament, TournamentAdmin)
