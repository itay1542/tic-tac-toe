import numpy as np
from src.state import State

class Board:
    def __init__(self, size = 3):
        self._matrix = np.zeros((size, size), int)
        self.size = size

    def fill_cell(self, index: tuple, state: State):
        self._matrix[index[0], index[1]] = state.value

    def get_matrix(self):
        return self._matrix

    def is_valid_coordinates(self, coordinates: (int, int)):
        try:
            if (self._matrix[coordinates[0], coordinates[1]] == State.Empty.value):
                return True
            return False
        except KeyError:
            return False