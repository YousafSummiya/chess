from abc import ABC, abstractmethod

class BaseChessPiece(ABC):
    def __init__(self, color: str, identifier: int):
        self.color = color
        self.name = ""  # Set by subclasses
        self.symbol = ""  # Set by subclasses  
        self.identifier = identifier
        self.position = 'None'
        self.is_alive = True
        self.board = None

    @abstractmethod
    def move(self, movement: str):
        """Abstract method - must be implemented by subclasses"""
        pass

    def die(self):
        """Toggle is_alive to False"""
        self.is_alive = False

    def set_initial_position(self, position: str):
        self.position = position

    def define_board(self, board):
        self.board = board

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return str(self)

# ✅ ONLY ONE of each class
class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Pawn"
        self.symbol = "-"

    def move(self, movement: str):
        print("Pawn moves forward 1 position")
        super().move(movement)

class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Rook"
        self.symbol = "R"

    def move(self, movement: str):
        print("Rook moves in a straight line")
        super().move(movement)

class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Bishop"
        self.symbol = "B"

    def move(self, movement: str):
        print("Bishop moves diagonally")
        super().move(movement)

class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Knight"
        self.symbol = "N"

    def move(self, movement: str):
        print("Knight moves in an L shape")
        super().move(movement)

class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "King"
        self.symbol = "K"

    def move(self, movement: str):
        print("King moves one position any direction")
        super().move(movement)

class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Queen"
        self.symbol = "Q"

    def move(self, movement: str):
        print("Queen moves any direction")
        super().move(movement)
