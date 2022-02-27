from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView

from .forms import ChessPieceForm
from .models import ChessPiece

# Create your views here.
class HomeView(TemplateView):
    template_name = 'knightmoves/welcome.html'

class RegisterChessPieceView(CreateView):
    model = ChessPiece
    success_url = ''
    form_class = ChessPieceForm

class DetailChessPieceView(DetailView):
    model = ChessPiece
    context_object_name = 'chesspiece'