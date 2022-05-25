from .state_type import State
import numpy as np


class StateChecker:

    def is_won(self, board):
        board_matrix = board.get_matrix()
        board_matrix_t = np.transpose(board_matrix)
        return self._scan_rows(board_matrix) or self._scan_rows(board_matrix_t) \
               or self._scan_diagonals(board_matrix)

    def _scan_rows(self, matrix):
        for row in matrix:
            # this if checks whether the entire row has the same value and its not empty
            if (len(set(row)) == 1 and row[0] != State.Empty.value):
                return True
        return False

    def _scan_diagonals(self, matrix):
        is_diag_win = self._scan_rows([np.diag(matrix)])
        if (not is_diag_win):
            # the secondary diagonal
            is_diag_win = self._scan_rows([np.diag(np.rot90(matrix))])
        return is_diag_win
