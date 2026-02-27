from pieces import Pawn, Rook, Bishop, Knight, King, Queen
import json

class Board:
    def __init__(self):
        self.squares = {
            f"{chr(col)}{row}": None
            for col in range(ord('a'), ord('i'))
            for row in range(1, 9)
        }

    def setup_board(self):
        # BLACK back row (row 8): Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook
        self.squares['a8'] = Rook('BLACK', 1)
        self.squares['b8'] = Knight('BLACK', 1)
        self.squares['c8'] = Bishop('BLACK', 1)
        self.squares['d8'] = Queen('BLACK', 1)
        self.squares['e8'] = King('BLACK', 1)
        self.squares['f8'] = Bishop('BLACK', 2)
        self.squares['g8'] = Knight('BLACK', 2)
        self.squares['h8'] = Rook('BLACK', 2)
        
        # Black pawns row 7 - dict comprehension
        black_pawns = {
            f"{chr(col)}7": Pawn('BLACK', i+1)
            for i, col in enumerate(range(ord('a'), ord('i')))
        }
        self.squares.update(black_pawns)
        
        # White pawns row 2 - dict comprehension
        white_pawns = {
            f"{chr(col)}2": Pawn('WHITE', i+1)
            for i, col in enumerate(range(ord('a'), ord('i')))
        }
        self.squares.update(white_pawns)
        
        # WHITE back row (row 1)
        self.squares['a1'] = Rook('WHITE', 1)
        self.squares['b1'] = Knight('WHITE', 1)
        self.squares['c1'] = Bishop('WHITE', 1)
        self.squares['d1'] = Queen('WHITE', 1)
        self.squares['e1'] = King('WHITE', 1)
        self.squares['f1'] = Bishop('WHITE', 2)
        self.squares['g1'] = Knight('WHITE', 2)
        self.squares['h1'] = Rook('WHITE', 2)

        # Set initial positions and board reference for all pieces
        for square, piece in self.squares.items():
            if piece:
                piece.set_initial_position(square)
                piece.define_board(self)

    def print_board(self):
        """Print board row by row (8 to 1) - EXACT assignment format"""
        for row in range(8, 0, -1):
            row_pieces = [
                str(self.squares.get(f"{chr(col)}{row}", None))
                for col in range(ord('a'), ord('i'))
            ]
            print(row_pieces)

    def find_piece(self, symbol: str, identifier: int, color: str):
        """List comprehension - find piece by symbol/id/color"""
        return [
            piece for square, piece in self.squares.items()
            if (piece and 
                piece.symbol == symbol and 
                piece.identifier == identifier and 
                piece.color == color)
        ]

    def get_piece(self, square: str):
        """Get piece on specific square"""
        return self.squares.get(square)

    def is_square_empty(self, square: str) -> bool:
        """True if square empty"""
        return self.get_piece(square) is None

    def kill_piece(self, square: str):
        """Kill piece on square"""
        piece = self.get_piece(square)
        if piece:
            piece.die()
            self.squares[square] = None

    @staticmethod
    def load_states(filename: str = 'board.txt'):
        """Generator - yield board states one line at a time"""
        try:
            with open(filename, 'r') as f:
                for line in f:
                    yield json.loads(line.strip())
        except FileNotFoundError:
            print(f"No {filename} found")

class BoardMovements:
    """Static methods for chess movements"""
    
    @staticmethod
    def forward(position: str, color: str, squares: int = 1):
        """Forward movement (WHITE down, BLACK up)"""
        col, row = position[0], int(position[1])
        delta = -squares if color == 'WHITE' else squares
        new_row = max(1, min(8, row + delta))
        return f"{col}{new_row}"

    @staticmethod
    def backward(position: str, color: str, squares: int = 1):
        """Backward movement"""
        col, row = position[0], int(position[1])
        delta = squares if color == 'WHITE' else -squares
        new_row = max(1, min(8, row + delta))
        return f"{col}{new_row}"

    @staticmethod
    def left(position: str, squares: int = 1):
        """Left movement"""
        col, row = position[0], int(position[1])
        new_col_ord = max(ord('a'), ord(col) - squares)
        return f"{chr(new_col_ord)}{row}"

    @staticmethod
    def right(position: str, squares: int = 1):
        """Right movement"""
        col, row = position[0], int(position[1])
        new_col_ord = min(ord('h'), ord(col) + squares)
        return f"{chr(new_col_ord)}{row}"

    @staticmethod
    def forward_left(position: str, color: str, squares: int = 1):
        """Diagonal forward-left"""
        col, row = position[0], int(position[1])
        delta_row = -squares if color == 'WHITE' else squares
        new_col_ord = max(ord('a'), ord(col) - squares)
        new_row = max(1, min(8, row + delta_row))
        return f"{chr(new_col_ord)}{new_row}"

    @staticmethod
    def forward_right(position: str, color: str, squares: int = 1):
        """Diagonal forward-right"""
        col, row = position[0], int(position[1])
        delta_row = -squares if color == 'WHITE' else squares
        new_col_ord = min(ord('h'), ord(col) + squares)
        new_row = max(1, min(8, row + delta_row))
        return f"{chr(new_col_ord)}{new_row}"
