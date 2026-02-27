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

    def __repr__(self):
        return str(self)

class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Pawn"
        self.symbol = "-"

    def move(self, movement: str):
        print("Pawn moves forward 1 position")
        super().move(movement)
