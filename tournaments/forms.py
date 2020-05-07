from django import forms

from django.forms import models as ble

from .models import Tournament

class TournamentRegistrationForm(forms.Form):
    pass

class TournamentUnregisterForm(forms.Form):
    pass

class MyMultipleModelChoiceField(ble.ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return f"{obj.name} | {obj.date}"

class TournamentFullRegistrationForm(forms.Form):
    # add_check_each_tournament()

    # OPTIONS = (
    #     ("AUT", "Austria"),
    #     ("DEU", "Germany"),
    #     ("NLD", "Neitherlands"),
    # )
    tournaments = MyMultipleModelChoiceField(queryset=Tournament.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
        


