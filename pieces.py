from abc import ABC, abstractmethod

class BaseChessPiece(ABC):
    def __init__(self, color: str, identifier: int):
        self.color = color
        self.name = ""
        self.symbol = ""
        self.identifier = identifier
        self.position = 'None'
        self.is_alive = True
        self.board = None

    @abstractmethod
    def move(self, movement: str):
        pass

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Pawn"
        self.symbol = "-"

    def move(self, movement: str):
        print("Pawn moves forward 1 position")

class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Rook"
        self.symbol = "R"

    def move(self, movement: str):
        print("Rook moves in a straight line")

class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Bishop"
        self.symbol = "B"

    def move(self, movement: str):
        print("Bishop moves diagonally")

class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Knight"
        self.symbol = "N"

    def move(self, movement: str):
        print("Knight moves in an L shape")

class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "King"
        self.symbol = "K"

    def move(self, movement: str):
        print("King moves one position any direction")

class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Queen"
        self.symbol = "Q"

    def move(self, movement: str):
        print("Queen moves any direction")
