from enum import Enum
from typing import List


class Color(Enum):
    WHITE = 0
    BLACK = 1

class PieceType(Enum):
    PAWN = 0
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    QUEEN = 4
    KING = 5


class Piece:

    color: Color
    piece_type: PieceType

    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

class Square:
    row: int
    col: int

    def __init__(self, row, col):
        self.row = row
        self.col = col

class Move:
    start: Square
    end: Square

    piece: Piece

    is_capture: bool

    def __init__(self, start, end, piece, is_capture):
        self.start = start
        self.end = end
        self.piece = piece
        self.is_capture = is_capture


class Board:
    __board: List[List[Piece]] = [[None] * 8 for _ in range(8)]
    __moves

    def __init__(self):
        pass

    def create_move(self, move_description: str) -> Move:
