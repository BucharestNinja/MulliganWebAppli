from django import forms
from .models import Deck

class DeckForm:
    class:Meta:
        model=Deck
        fields=("card")
