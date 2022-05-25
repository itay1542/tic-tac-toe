from src.data.board import Board
from src.state import State


class TestBoard:
    board = Board()

    def test_fill_cell_updates_correct_cell(self):
        self.board.fill_cell((0, 0), State.O)
        assert self.board.get_matrix()[0][0] == State.O.value

    def test_board_is_valid_coordinates_false_on_taken_cell(self):
        coordinates = (0, 0)
        self.board.fill_cell(coordinates, State.X)
        assert self.board.is_valid_coordinates(coordinates) == False

    def test_board_is_valid_coordinates_true_on_empty_cell(self):
        coordinates = (0, 0)
        self.board.fill_cell(coordinates, State.X)
        assert self.board.is_valid_coordinates((0, 1)) == True