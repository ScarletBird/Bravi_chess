from django.db import models

TYPE = [
    ('k', 'King' ),
    ('q', 'Queen' ),
    ('b', 'Bishop' ),
    ('n', 'Knight' ),
    ('r', 'Rook' ),
    ('p', 'Pawn' )
]

COLOUR = [
    ('w', 'White'),
    ('b', 'Black')
]    

# Create your models here.
class ChessPiece(models.Model):
    type = models.CharField(max_length=1, choices = TYPE)
    colour = models.CharField(max_length=1, choices = COLOUR)

class BoardSpace(models.Model):
    coordinate = models.CharField(max_length=2)
