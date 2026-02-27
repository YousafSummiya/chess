from pieces import Pawn, Rook, Bishop, Knight, King, Queen

class Board:
    def __init__(self):
        # ✅ Dict comprehension - 64 squares a1-h8
        self.squares = {
            f"{chr(col)}{row}": None
            for col in range(ord('a'), ord('i'))
            for row in range(1, 9)
        }

    def setup_board(self):
        """✅ Place ALL pieces exactly as standard chess setup"""
        
        # BLACK back row (row 8): Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook
        back_row_black = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
        pieces_black = [Rook('BLACK', 1), Knight('BLACK', 1), Bishop('BLACK', 1), 
                       Queen('BLACK', 1), King('BLACK', 1), Bishop('BLACK', 2), 
                       Knight('BLACK', 2), Rook('BLACK', 2)]
        
        for square, piece in zip(back_row_black, pieces_black):
            self.squares[square] = piece

        # ✅ BLACK PAWNS row 7 - Dict comprehension EXACTLY as assignment!
        black_pawns = {
            f"{chr(col)}7": Pawn('BLACK', i+1)
            for i, col in enumerate(range(ord('a'), ord('i')))
        }
        self.squares.update(black_pawns)

        # ✅ WHITE PAWNS row 2 - Dict comprehension
        white_pawns = {
            f"{chr(col)}2": Pawn('WHITE', i+1)
            for i, col in enumerate(range(ord('a'), ord('i')))
        }
        self.squares.update(white_pawns)

        # WHITE back row (row 1)
        back_row_white = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
        pieces_white = [Rook('WHITE', 1), Knight('WHITE', 1), Bishop('WHITE', 1), 
                       Queen('WHITE', 1), King('WHITE', 1), Bishop('WHITE', 2), 
                       Knight('WHITE', 2), Rook('WHITE', 2)]
        
        for square, piece in zip(back_row_white, pieces_white):
            self.squares[square] = piece

    def print_board(self):
        """✅ Print rows 8→1 (chess standard) with list comprehension"""
        for row in range(8, 0, -1):  # Row 8 (black) to row 1 (white)
            row_pieces = [
                str(self.squares.get(f"{chr(col)}{row}", None))
                for col in range(ord('a'), ord('i'))
            ]
            print(row_pieces)  # ✅ EXACT format from assignment!
