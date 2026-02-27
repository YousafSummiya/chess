from abc import ABC
import functools
import json
from movements import BoardMovements

class BaseChessPiece(ABC):
    def __init__(self, color: str, identifier: int):
        self.color = color
        self.name = ""
        self.symbol = ""
        self.identifier = identifier
        self.position = None
        self.is_alive = True
        self.board = None

    # DECORATORS - Assignment requirement
    def print_board_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            print(f"\n {self.name} now at {self.position}")
            self.board.print_board()
        return wrapper

    def save_board_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            # FIXED: None → 'Empty' for JSON
            state = {k: (str(v) if v else 'Empty') for k, v in self.board.squares.items()}
            with open('board.txt', 'a') as f:
                f.write(json.dumps(state) + '\n')
        return wrapper

    @print_board_decorator
    @save_board_decorator
    def move(self, movement: str):
        """Move with capture logic - Assignment requirement"""
        target = self.board.get_piece(movement)
        if target:
            if target.color != self.color:
                print(f"  {self.name} captures {target.name}!")
                self.board.kill_piece(movement)
            else:
                print(" Blocked by friendly piece!")
                return

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

    __repr__ = __str__

# CHESS PIECES - Assignment requirement
class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Pawn"
        self.symbol = "-"
    def move(self):
        movement = BoardMovements.forward(self.position, self.color, 1)
        super().move(movement)

class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Rook"
        self.symbol = "R"
    def move(self, direction: str, squares: int = 1):
        direction = direction.lower()
        if direction == "left": movement = BoardMovements.left(self.position, squares)
        elif direction == "right": movement = BoardMovements.right(self.position, squares)
        elif direction == "forward": movement = BoardMovements.forward(self.position, self.color, squares)
        elif direction == "backward": movement = BoardMovements.backward(self.position, self.color, squares)
        else: raise ValueError(f"Rook invalid: {direction}")
        super().move(movement)

class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Bishop"
        self.symbol = "B"
    def move(self, direction: str, squares: int = 1):
        direction = direction.lower()
        mapping = {"forward-left": BoardMovements.forward_left, "forward-right": BoardMovements.forward_right,
                   "backward-left": BoardMovements.backward_left, "backward-right": BoardMovements.backward_right}
        movement = mapping[direction](self.position, self.color, squares)
        super().move(movement)

class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Knight"
        self.symbol = "N"
    def move(self):
        print("♞ Knight L-move (custom logic needed)")

class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "King"
        self.symbol = "K"
    def move(self, direction: str):
        direction = direction.lower()
        mapping = {"forward": BoardMovements.forward, "backward": BoardMovements.backward,
                   "left": BoardMovements.left, "right": BoardMovements.right,
                   "forward-left": BoardMovements.forward_left, "forward-right": BoardMovements.forward_right}
        movement = mapping[direction](self.position, self.color, 1)
        super().move(movement)

class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Queen"
        self.symbol = "Q"
    def move(self, direction: str, squares: int = 1):
        direction = direction.lower()
        mapping = {"forward": BoardMovements.forward, "backward": BoardMovements.backward,
                   "left": BoardMovements.left, "right": BoardMovements.right,
                   "forward-left": BoardMovements.forward_left, "forward-right": BoardMovements.forward_right,
                   "backward-left": BoardMovements.backward_left, "backward-right": BoardMovements.backward_right}
        movement = mapping[direction](self.position, self.color, squares)
        super().move(movement)
