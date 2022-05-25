from src.state import State, StateChecker
from unittest.mock import Mock

class TestStateChecker:
    state_checker = StateChecker()
    board_mock = Mock()

    def test_is_won_returns_false_on_empty_board(self):
        game_matrix = [[State.Empty.value for j in range(3)] for i in range(3)]
        self.board_mock.get_matrix.return_value = game_matrix
        assert self.state_checker.is_won(self.board_mock) == False

    def test_is_won_returns_true_on_row_of_x(self):
        game_matrix = [[State.X.value for j in range(3)] for i in range(1)] \
                + [[State.Empty.value for k in range(2)]]
        self.board_mock.get_matrix.return_value = game_matrix
        assert self.state_checker.is_won(self.board_mock) == True

    def test_is_won_returns_true_on_row_of_o(self):
        game_matrix = [[State.O.value for j in range(3)] for i in range(1)] \
                + [[State.Empty.value for k in range(2)]]
        self.board_mock.get_matrix.return_value = game_matrix
        assert self.state_checker.is_won(self.board_mock) == True

    def test_is_won_returns_true_on_column_of_x(self):
        game_matrix = [[State.X.value, State.Empty.value, State.Empty.value] for i in range(3)]
        self.board_mock.get_matrix.return_value = game_matrix
        assert self.state_checker.is_won(self.board_mock) == True

    def test_is_won_returns_true_on_diagonal_of_x(self):
        game_matrix = [[State.X.value, State.Empty.value, State.Empty.value],
                       [State.O.value, State.X.value, State.Empty.value],
                       [State.O.value, State.Empty.value, State.X.value]]
        self.board_mock.get_matrix.return_value = game_matrix
        assert self.state_checker.is_won(self.board_mock) == True

    def test_is_won_returns_true_on_secondary_diagonal_of_x(self):
        game_matrix = [[State.O.value, State.Empty.value, State.X.value],
                       [State.O.value, State.X.value, State.Empty.value],
                       [State.X.value, State.Empty.value, State.O.value]]
        self.board_mock.get_matrix.return_value = game_matrix
        assert self.state_checker.is_won(self.board_mock) == True