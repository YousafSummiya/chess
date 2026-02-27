from abc import ABC, abstractmethod
from functools import wraps
from movements import BoardMovement

def print_board(func):
    """Decorator: Print board before and after move."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"\n--- {self} MOVING from {self.position} ---")
        self.board.print_board()
        print()
        
        result = func(self, *args, **kwargs)
        
        print(f"--- AFTER {self} MOVE ---")
        self.board.print_board()
        print("-" * 50)
        return result
    return wrapper

def save_board(func):
    """Decorator: Save board state to board.txt after move."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        
        # Save board state to file
        import json
        try:
            with open('board.txt', 'a') as file:
                state = {k: str(v) if v else None for k, v in self.board.squares.items()}
                file.write(json.dumps(state) + '\n')
            print(f"💾 Board state saved (total lines: {sum(1 for _ in open('board.txt'))})")
        except Exception as e:
            print(f"Save failed: {e}")
        return result
    return wrapper

class BaseChessPiece(ABC):
    def __init__(self, color: str, name: str, symbol: str, identifier: int):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.is_alive = True
        self.position = None
        self.board = None

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return self.__str__()

    @print_board
    @save_board
    def move(self, new_position: str = None):
        """Execute movement on the board with decorators."""
        if new_position is None:
            new_position = self.calculate_movement()
        
        if not new_position:
            print(f"{self} cannot move - blocked or invalid!")
            return False

        # Check if new location is free or enemy
        target_piece = self.board.get_piece(new_position)
        if target_piece:
            if target_piece.color == self.color:
                print(f"{self} blocked by friendly piece at {new_position}!")
                return False
            else:
                print(f"{self} kills {target_piece} at {new_position}!")
                target_piece.die()
                self.board.squares[new_position] = None

        # Execute move
        self.board.squares[self.position] = None
        self.position = new_position
        self.board.squares[self.position] = self
        
        print(f"✅ {self} successfully moved to {new_position}")
        return True

    @abstractmethod
    def calculate_movement(self) -> str:
        pass

    def die(self):
        self.is_alive = False

    def set_initial_position(self, position):
        self.position = position

    def define_board(self, board):
        self.board = board

# Piece implementations (unchanged from Step 5)
class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Pawn", "-", identifier)

    def calculate_movement(self) -> str:
        return BoardMovement.forward(self.position, self.color, 1)

class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Rook", "R", identifier)

    def calculate_movement(self) -> str:
        return BoardMovement.forward(self.position, self.color, 1)

class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Bishop", "B", identifier)

    def calculate_movement(self) -> str:
        return BoardMovement.forward_left(self.position, self.color, 1)

class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Queen", "Q", identifier)

    def calculate_movement(self) -> str:
        return BoardMovement.forward(self.position, self.color, 1)

class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "King", "K", identifier)

    def calculate_movement(self) -> str:
        return BoardMovement.forward(self.position, self.color, 1)

class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Knight", "N", identifier)

    def calculate_movement(self) -> str:
        col_idx = ord(self.position[0]) - ord('a')
        row = int(self.position[1])
        
        if self.color == "WHITE":
            new_row = min(row + 2, 8)
        else:
            new_row = max(row - 2, 1)
        new_col_idx = max(col_idx - 1, 0)
        new_col = chr(ord('a') + new_col_idx)
        
        return f"{new_col}{new_row}"
