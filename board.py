from pieces import *
from typing import Optional, Dict, Any, List
import json

class Board:
    def __init__(self):
        # Dict comprehension for board squares
        self.squares = {
            f"{chr(col)}{row}": None 
            for col in range(ord('a'), ord('i')) 
            for row in range(1, 9)
        }
        self.setup_board()
        
        # Set positions and board reference
        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)
    def save_state_after_move(self):
          """Auto-save after every move"""
          self.save_state()

    def setup_board(self):
        """Standard chess starting position"""
        # Black back row (row 1)
        self.squares['a1'] = Rook('BLACK', 1)
        self.squares['b1'] = Knight('BLACK', 1)
        self.squares['c1'] = Bishop('BLACK', 1)
        self.squares['d1'] = Queen('BLACK', 1)
        self.squares['e1'] = King('BLACK', 1)
        self.squares['f1'] = Bishop('BLACK', 2)
        self.squares['g1'] = Knight('BLACK', 2)
        self.squares['h1'] = Rook('BLACK', 2)

        # Black pawns row 2 - dict comprehension
        black_pawns = {
            f"{chr(col)}2": Pawn('BLACK', i+1)
            for i, col in enumerate(range(ord('a'), ord('i')))
        }
        self.squares.update(black_pawns)

        # White pawns row 7 - dict comprehension
        white_pawns = {
            f"{chr(col)}7": Pawn('WHITE', i+1)
            for i, col in enumerate(range(ord('a'), ord('i')))
        }
        self.squares.update(white_pawns)

        # White back row (row 8)
        self.squares['a8'] = Rook('WHITE', 1)
        self.squares['b8'] = Knight('WHITE', 1)
        self.squares['c8'] = Bishop('WHITE', 1)
        self.squares['d8'] = Queen('WHITE', 1)
        self.squares['e8'] = King('WHITE', 1)
        self.squares['f8'] = Bishop('WHITE', 2)
        self.squares['g8'] = Knight('WHITE', 2)
        self.squares['h8'] = Rook('WHITE', 2)

    def print_board(self):
        """Print board row-first (white's perspective)"""
        for row in range(8, 0, -1):
            row_pieces = [
                self.squares.get(f"{col}{row}", None) 
                for col in 'abcdefgh'
            ]
            print([str(p) if p else 'None' for p in row_pieces])

    def get_piece(self, square: str) -> Optional[BaseChessPiece]:
        """Get piece at specific square"""
        return self.squares.get(square)

    def is_square_empty(self, square: str) -> bool:
        """Check if square is empty"""
        return self.get_piece(square) is None

    def find_piece(self, symbol: str, identifier: int, color: str) -> List[BaseChessPiece]:
        """Find pieces matching criteria using list comprehension"""
        return [
            piece for piece in self.squares.values()
            if piece and piece.symbol == symbol and 
               piece.identifier == identifier and 
               piece.color == color
        ]

    def kill_piece(self, square: str):
        """Kill piece on specific square"""
        piece = self.get_piece(square)
        if piece:
            piece.die()
            self.squares[square] = None
            print(f"Killed: {piece} at {square}")

    def save_state(self, filename: str = 'board.txt'):
        """Save board state to file"""
        state = {}
        for pos, piece in self.squares.items():
            if piece:
                state[pos] = {
                    'color': piece.color,
                    'name': piece.name,
                    'identifier': piece.identifier,
                    'symbol': piece.symbol,
                    'position': piece.position
                }
            else:
                state[pos] = None
        
        with open(filename, 'a') as file:
            file.write(json.dumps(state) + '\n')

    @staticmethod
    def load_states(filename: str = 'board.txt'):
        """Generator to load board states one by one"""
        try:
            with open(filename, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    yield line_num, json.loads(line.strip())
        except FileNotFoundError:
            print("No saved states found")
