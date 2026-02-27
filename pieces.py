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

    @abstractmethod
    def move(self, movement=None):
        """Each piece must implement how it moves."""
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
