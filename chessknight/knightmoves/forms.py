from django import forms
from .models import ChessPiece

class ChessPieceForm(forms.ModelForm):
    TYPES = (
        ('k', 'King' ),
        ('q', 'Queen' ),
        ('b', 'Bishop' ),
        ('n', 'Knight' ),
        ('r', 'Rook' ),
        ('p', 'Pawn' )
    )

    COLOURS = (
        ('w', 'White'),
        ('b', 'Black')
    )

    type = forms.ChoiceField(label='Type',widget=forms.Select, choices=TYPES)
    colour = forms.ChoiceField(label='Colour',widget=forms.Select, choices=COLOURS)

    class Meta:
        model = ChessPiece
        fields = ['type', 'colour']