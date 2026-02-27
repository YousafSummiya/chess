import json
from pieces import Pawn, Rook, Knight, Bishop, King, Queen

class Board:
    def __init__(self):
        # Dict comprehension - Assignment requirement
        self.squares = {f"{chr(col)}{row}": None for col in range(ord('a'), ord('i')) for row in range(1, 9)}

    def setup_board(self):
        # BLACK back row
        self.squares['a8'] = Rook('BLACK', 1); self.squares['b8'] = Knight('BLACK', 1)
        self.squares['c8'] = Bishop('BLACK', 1); self.squares['d8'] = Queen('BLACK', 1)
        self.squares['e8'] = King('BLACK', 1); self.squares['f8'] = Bishop('BLACK', 2)
        self.squares['g8'] = Knight('BLACK', 2); self.squares['h8'] = Rook('BLACK', 2)

        # Black pawns - Dict comprehension - Assignment requirement
        black_pawns = {f"{chr(col)}7": Pawn('BLACK', i+1) for i, col in enumerate(range(ord('a'), ord('i')))}
        self.squares.update(black_pawns)

        # White pawns - Dict comprehension - Assignment requirement
        white_pawns = {f"{chr(col)}2": Pawn('WHITE', i+1) for i, col in enumerate(range(ord('a'), ord('i')))}
        self.squares.update(white_pawns)

        # WHITE back row
        self.squares['a1'] = Rook('WHITE', 1); self.squares['b1'] = Knight('WHITE', 1)
        self.squares['c1'] = Bishop('WHITE', 1); self.squares['d1'] = Queen('WHITE', 1)
        self.squares['e1'] = King('WHITE', 1); self.squares['f1'] = Bishop('WHITE', 2)
        self.squares['g1'] = Knight('WHITE', 2); self.squares['h1'] = Rook('WHITE', 2)

        # Link pieces to board - Assignment requirement
        for square, piece in self.squares.items():
            if piece:
                piece.set_initial_position(square)
                piece.define_board(self)

    def print_board(self):
        """Print board row by row (8 to 1) - FIXED Empty display"""
        for row in range(8, 0, -1):
            row_pieces = [str(self.squares[f"{chr(col)}{row}"] or 'Empty') for col in range(ord('a'), ord('i'))]
            print(row_pieces)

    def find_piece(self, symbol: str, identifier: int, color: str):
        """List comprehension - Assignment requirement"""
        return [piece for square, piece in self.squares.items() 
                if piece and piece.symbol == symbol and piece.identifier == identifier and piece.color == color]

    def get_piece(self, square: str):
        return self.squares.get(square)

    def is_square_empty(self, square: str) -> bool:
        return self.get_piece(square) is None

    def kill_piece(self, square: str):
        piece = self.get_piece(square)
        if piece:
            piece.die()
            self.squares[square] = None

    @staticmethod
    def load_states(filename: str = 'board.txt'):
        """Generator - Assignment requirement"""
        try:
            with open(filename, 'r') as f:
                for line in f:
                    yield json.loads(line.strip())
        except FileNotFoundError:
            print(f"No {filename} found")
