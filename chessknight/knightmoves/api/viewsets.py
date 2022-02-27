from ast import Pass
from urllib import request
from xmlrpc.client import ResponseError
from rest_framework import viewsets, status
from rest_framework.response import Response

from . import serializers
from ..models import ChessPiece, BoardSpace

def validateType(type):
    '''
    Function to validate if a Type is in the format accepted by the database (single char)
    '''
    if len(type) > 1:
        type = {
            'king': 'k',
            'queen': 'q',
            'bishop': 'b',
            'knight': 'n',
            'rook': 'r',
            'pawn': 'p'
        }[type.lower()]
    return type.lower()

def validateColour(colour):
    '''
    Function to validate if a Colour is in the format accepted by the database (single char)
    '''
    if len(colour) > 1:
        colour = {
            'white': 'w',
            'black': 'b'
        }[colour.lower()]
    return colour.lower()

class ChessPieceViewSet(viewsets.ModelViewSet):

    def create(self, request):
        # Change to validate if the user sent a valid type and colour, changing it for the database to use
        data = request.data
        data["type"] = validateType(data["type"])
        data["colour"] = validateColour(data["colour"])

        # Here continues the code as common
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        # When GET, visualize only the ID
        if self.request.method == 'GET':
            return serializers.ReadChessPieceSerializer
        else:
            return serializers.CreateChessPieceSerializer

    def get_queryset(self):
        
        queryset = ChessPiece.objects.all()

        piece_type = self.request.query_params.get('type')
        piece_colour = self.request.query_params.get('colour')

        # If the user specified the piece colour and type, only their ID is sent
        if piece_colour is not None and piece_type is not None:
            piece_type = validateType(piece_type)
            piece_colour = validateColour(piece_colour)

            queryset =  queryset.filter(type=piece_type, colour=piece_colour)
        return queryset

class ChessMovesViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ChessMovesSerializer

    def get_queryset(self):
        if self.request.method == 'GET' and 'piece_id' in self.request.query_params:

            piece_id = self.request.query_params.get('piece_id')
            coordinate = self.request.query_params.get("coordinate")

            piece = ChessPiece.objects.filter(id=piece_id)

            # Check if the piece is a Knight
            if piece[0].type == 'n':

                column = int(ord(coordinate[0]) - 64)
                row = int(coordinate[1])

                def makeArrayMoves(tuple_row_column):
                    '''
                    Function to calculate possible movements by a horse, given its current coordinate
                    '''
                    possible_moves = []
                    column, row = tuple_row_column

                    for i in [1, -1]:
                        for j in [1, -1]:
                            if row + (2 * i) in range(1,8) and column + (1 * j) in range(1,8):
                                possible_moves.append((row + (2 * i), column + (1 * j)))
                            if row + (1 * i) in range(1,8) and column + (2 * j) in range(1,8):
                                possible_moves.append((row + (1 * i), column + (2 * j)))
                    return possible_moves
                
                first_move = makeArrayMoves((column, row))

                for moves in first_move:
                    second_move = makeArrayMoves(i for i in moves)

                all_moves = []
                for moves in second_move:
                    # Transforming integers into Algebraic Notation
                    all_moves.append(f'{chr(moves[0]+64)}{moves[1]}')
                
                # Filtering using the board to also avoid duplicates
                queryset = BoardSpace.objects.filter(coordinate__in=all_moves)
                
                return queryset
            else: return BoardSpace.objects.all()
        else: return BoardSpace.objects.all()