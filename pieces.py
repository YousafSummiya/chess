from abc import ABC
import functools
import json

class BaseChessPiece(ABC):
    def __init__(self, color: str, identifier: int):
        self.color = color
        self.name = ""
        self.symbol = ""
        self.identifier = identifier
        self.position = 'None'
        self.is_alive = True
        self.board = None

    def print_board_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.board.print_board()
        return wrapper

    def save_board_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            with open('board.txt', 'a') as f:
                f.write(json.dumps({k: str(v) for k, v in self.board.squares.items()}) + '\n')
        return wrapper

    @print_board_decorator
    def move(self, movement: str):
        """Move piece to new position"""
        new_location = self.board.get_piece(movement)
        
        if new_location and new_location.color != self.color:
            self.board.kill_piece(movement)
        
        self.board.squares[self.position] = None
        self.position = movement
        self.board.squares[self.position] = self

    def die(self):
        self.is_alive = False

    def set_initial_position(self, position: str):
        self.position = position

    def define_board(self, board):
        self.board = board

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Pawn"
        self.symbol = "-"

    def move(self, movement: str):
        movement = "Pawn moves forward 1 position"
        super().move(movement)

class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Rook"
        self.symbol = "R"

    def move(self, movement: str):
        movement = "Rook moves in a straight line"
        super().move(movement)

class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Bishop"
        self.symbol = "B"

    def move(self, movement: str):
        movement = "Bishop moves diagonally"
        super().move(movement)

class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Knight"
        self.symbol = "N"

    def move(self, movement: str):
        movement = "Knight moves in an L shape"
        super().move(movement)

class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "King"
        self.symbol = "K"

    def move(self, movement: str):
        movement = "King moves one position any direction"
        super().move(movement)

class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Queen"
        self.symbol = "Q"

    def move(self, movement: str):
        movement = "Queen moves any direction"
        super().move(movement)
