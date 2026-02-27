from abc import ABC, abstractmethod
from enum import Enum

class Color(Enum):
    WHITE = "WHITE"
    BLACK = "BLACK"

class BaseChessPiece(ABC):
    def __init__(self, color: str, identifier: int):
        self.color = color
        self.name = self.__class__.__name__
        self.identifier = identifier
        self.symbol = self._get_symbol()
        self.position = 'None'
        self.is_alive = True
        self.board = None

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value

    def _get_symbol(self):
        symbols = {
            'Pawn': '-', 'Rook': 'R', 'Bishop': 'B', 
            'Knight': 'N', 'King': 'K', 'Queen': 'Q'
        }
        return symbols.get(self.name, '')

    @abstractmethod
    def move(self, movement: str):
        pass

    def die(self):
        self.is_alive = False

    def set_initial_position(self, position):
        self.position = position

    def define_board(self, board):
        self.board = board

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return str(self)
