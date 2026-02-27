from abc import ABC, abstractmethod

class BaseChessPiece(ABC):
    def __init__(self, color: str, name: str, symbol: str, identifier: int):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.is_alive = True
        self.position = None  # Filled later by the board
        self.board = None     # Filled later by the board class

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return self.__str__()

    def move(self, movement=None):
        """Base move implementation - prints the movement."""
        if movement is None:
            movement = "Unknown movement"
        print(f"{movement}")

    @abstractmethod
    def calculate_movement(self):
        """Each piece must implement how it calculates its movement."""
        pass

    def die(self):
        """Mark this piece as dead."""
        self.is_alive = False

    def set_initial_position(self, position):
        """Set initial position when piece is placed on board."""
        self.position = position

    def define_board(self, board):
        """Attach a reference to the board."""
        self.board = board

# All chess pieces - Step 3 complete implementation
class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Pawn", "-", identifier)

    def calculate_movement(self):
        return "Pawn moves forward 1 position"

    def move(self, movement=None):
        if movement is None:
            movement = self.calculate_movement()
        super().move(movement)

class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Rook", "R", identifier)

    def calculate_movement(self):
        return "Rook moves in a straight line"

    def move(self, movement=None):
        if movement is None:
            movement = self.calculate_movement()
        super().move(movement)

class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Bishop", "B", identifier)

    def calculate_movement(self):
        return "Bishop moves diagonally"

    def move(self, movement=None):
        if movement is None:
            movement = self.calculate_movement()
        super().move(movement)

class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Queen", "Q", identifier)

    def calculate_movement(self):
        return "Queen moves in all directions"

    def move(self, movement=None):
        if movement is None:
            movement = self.calculate_movement()
        super().move(movement)

class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "King", "K", identifier)

    def calculate_movement(self):
        return "King moves one square any direction (can kill)"

    def move(self, movement=None):
        if movement is None:
            movement = self.calculate_movement()
        super().move(movement)

class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Knight", "N", identifier)

    def calculate_movement(self):
        return "Knight moves in L-shape (can jump over pieces)"

    def move(self, movement=None):
        if movement is None:
            movement = self.calculate_movement()
        super().move(movement)
