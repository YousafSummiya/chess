from pieces import Pawn, Rook, Bishop, Queen, King, Knight
import json
import os

class Board:
    def __init__(self):
        self.squares = {
            f"{chr(col)}{row}": None 
            for col in range(ord('a'), ord('i')) 
            for row in range(1, 9)
        }
        self.setup_board()

    def setup_board(self):
        """Place all pieces in starting positions."""
        # Black pieces row 1
        self.squares['a1'] = Rook('BLACK', 1)
        self.squares['b1'] = Knight('BLACK', 1)
        self.squares['c1'] = Bishop('BLACK', 1)
        self.squares['d1'] = Queen('BLACK', 1)
        self.squares['e1'] = King('BLACK', 1)
        self.squares['f1'] = Bishop('BLACK', 2)
        self.squares['g1'] = Knight('BLACK', 2)
        self.squares['h1'] = Rook('BLACK', 2)
        
        # Black pawns row 2
        black_pawns = {f"{chr(col)}2": Pawn('BLACK', i+1) for col, i in zip(range(ord('a'), ord('i')), range(8))}
        self.squares.update(black_pawns)
        
        # White pawns row 7
        white_pawns = {f"{chr(col)}7": Pawn('WHITE', i+1) for col, i in zip(range(ord('a'), ord('i')), range(8))}
        self.squares.update(white_pawns)
        
        # White pieces row 8
        self.squares['a8'] = Rook('WHITE', 1)
        self.squares['b8'] = Knight('WHITE', 1)
        self.squares['c8'] = Bishop('WHITE', 1)
        self.squares['d8'] = Queen('WHITE', 1)
        self.squares['e8'] = King('WHITE', 1)
        self.squares['f8'] = Bishop('WHITE', 2)
        self.squares['g8'] = Knight('WHITE', 2)
        self.squares['h8'] = Rook('WHITE', 2)
        
        # Link pieces to board
        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)

    def print_board(self):
        for row in range(8, 0, -1):
            row_pieces = [str(self.squares.get(f"{chr(col)}{row}", None)) for col in range(ord('a'), ord('i'))]
            print(row_pieces)

    def get_piece(self, square):
        return self.squares.get(square)

    def is_square_empty(self, square):
        return self.get_piece(square) is None

    def find_piece(self, symbol: str, identifier: int, color: str):
        return [(square, piece) for square, piece in self.squares.items()
                if piece and piece.symbol == symbol and piece.identifier == identifier and piece.color == color]

    def kill_piece(self, square):
        piece = self.get_piece(square)
        if piece:
            piece.die()
            self.squares[square] = None

    @staticmethod
    def load_board_states_generator(filename='board.txt'):
        """FIXED: Generator with proper None handling."""
        if not os.path.exists(filename):
            print(f"❌ No {filename} found")
            return
            
        try:
            with open(filename, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    try:
                        raw_state = json.loads(line.strip())
                        # FIX: Convert string 'None' back to actual None
                        state = {k: None if v == 'null' or v is None else v for k, v in raw_state.items()}
                        yield line_num, state
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    @staticmethod
    def print_state_from_generator(state_dict):
        """Print saved state in board format."""
        squares = {k: None if v is None or v == 'null' else v for k, v in state_dict.items()}
        for row in range(8, 0, -1):
            row_pieces = [str(squares.get(f"{chr(col)}{row}", None)) for col in range(ord('a'), ord('i'))]
            print(row_pieces)
