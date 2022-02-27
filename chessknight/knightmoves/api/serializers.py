from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from ..models import ChessPiece, BoardSpace

class ReadChessPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessPiece
        fields = ['id']

class CreateChessPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessPiece
        fields = ['id', 'type', 'colour']

class ChessMovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardSpace
        fields = ["coordinate"]