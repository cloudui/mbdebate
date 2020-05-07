from django import forms

from .models import Tournament

class TournamentRegistrationForm(forms.Form):
    pass

class TournamentUnregisterForm(forms.Form):
    pass

class TournamentFullRegistrationForm(forms.Form):
    # add_check_each_tournament()

    # OPTIONS = (
    #     ("AUT", "Austria"),
    #     ("DEU", "Germany"),
    #     ("NLD", "Neitherlands"),
    # )
    Countries = forms.ModelMultipleChoiceField(queryset=Tournament.objects.all(),widget=forms.CheckboxSelectMultiple, required=False)
        

