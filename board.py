from pieces import Pawn, Rook, Bishop, Queen, King, Knight

class Board:
    def __init__(self):
        # Dict comprehension to create all 64 squares (a1-h8)
        self.squares = {
            f"{chr(col)}{row}": None 
            for col in range(ord('a'), ord('i')) 
            for row in range(1, 9)
        }
        self.setup_board()

    def setup_board(self):
        """Place all pieces in starting positions."""
        
        # Black pieces (row 1 & 2)
        # Row 1: Rooks, Knights, Bishops, Queen, King, Bishops, Knights, Rooks
        self.squares['a1'] = Rook('BLACK', 1)
        self.squares['b1'] = Knight('BLACK', 1)
        self.squares['c1'] = Bishop('BLACK', 1)
        self.squares['d1'] = Queen('BLACK', 1)
        self.squares['e1'] = King('BLACK', 1)
        self.squares['f1'] = Bishop('BLACK', 2)
        self.squares['g1'] = Knight('BLACK', 2)
        self.squares['h1'] = Rook('BLACK', 2)
        
        # Black pawns (row 2) - Dict comprehension!
        black_pawns = {
            f"{chr(col)}2": Pawn('BLACK', i+1) 
            for col, i in zip(range(ord('a'), ord('i')), range(8))
        }
        self.squares.update(black_pawns)
        
        # Empty rows 3-6 (already None from init)
        
        # White pawns (row 7) - Dict comprehension!
        white_pawns = {
            f"{chr(col)}7": Pawn('WHITE', i+1) 
            for col, i in zip(range(ord('a'), ord('i')), range(8))
        }
        self.squares.update(white_pawns)
        
        # White pieces (row 8)
        self.squares['a8'] = Rook('WHITE', 1)
        self.squares['b8'] = Knight('WHITE', 1)
        self.squares['c8'] = Bishop('WHITE', 1)
        self.squares['d8'] = Queen('WHITE', 1)
        self.squares['e8'] = King('WHITE', 1)
        self.squares['f8'] = Bishop('WHITE', 2)
        self.squares['g8'] = Knight('WHITE', 2)
        self.squares['h8'] = Rook('WHITE', 2)
        
        # Link pieces to board and set positions
        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)

    def print_board(self):
        """Print board in row-first format (8 to 1, white's perspective)."""
        for row in range(8, 0, -1):  # Print row 8 first (white), then 7, ..., 1
            row_pieces = [
                str(self.squares.get(f"{col}{row}", None)) 
                for col in range(ord('a'), ord('i'))
            ]
            print(row_pieces)

    def get_piece(self, square):
        """Returns the piece that is on a specific square."""
        return self.squares.get(square)

    def is_square_empty(self, square):
        """Returns True if the square is empty, False otherwise."""
        return self.get_piece(square) is None

    def find_piece(self, symbol: str, identifier: int, color: str):
        """Find piece by symbol, identifier, and color using list comprehension."""
        return [
            (square, piece) for square, piece in self.squares.items()
            if piece is not None and 
               piece.symbol == symbol and 
               piece.identifier == identifier and 
               piece.color == color
        ]

    def kill_piece(self, square):
        """Kill the piece on a specific square."""
        piece = self.get_piece(square)
        if piece:
            piece.die()
            self.squares[square] = None
