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

    # ✅ ONLY ONE move() method - implements abstractmethod logic
    def move(self, movement: str):
        print(movement)

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

# ✅ Now pieces DEFINE movement string and call super()
class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Pawn"
        self.symbol = "-"

    def move(self, movement: str):
        movement = "Pawn moves forward 1 position"  # ✅ Define movement
        super().move(movement)  # ✅ Parent prints it!

class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, identifier)
        self.name = "Rook"
        self.symbol = "R"

    def move(self, movement: str):
        movement = "Rook moves in a straight line"
        super().move(movement)

# Apply same pattern to ALL other pieces (Bishop, Knight, King, Queen)
