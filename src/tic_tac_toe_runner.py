from src.data.board import Board
from src.state import StateChecker, State
from src.view.console_board_view import ConsoleBoardView


class TicTacToeRunner:
    def __init__(self, state_checker: StateChecker, board_view: ConsoleBoardView,
                 board: Board):
        self.state_checker = state_checker
        self.board_view = board_view
        self.board = board

    def run(self):
        turns_elapsed = 0
        max_turns = self.board.size ** 2
        while turns_elapsed < max_turns:
            self.board_view.show_board(self.board)
            user_turn = ('X', State.X) if turns_elapsed % 2 == 0 else ('O', State.O)
            coordinates = self._get_user_input(user_turn)
            self.board.fill_cell(coordinates, user_turn[1])
            has_finished = self.state_checker.is_won(self.board)
            if has_finished:
                print(F"its a win for {user_turn[0]}!")
                return
            turns_elapsed += 1
        print("this game ends with a tie")

    def _get_user_input(self, whos_turn) -> (int, int):
        while True:
            try:
                coordinates_raw = input(F"{whos_turn[0]} turn, select coordinates <x, y>")
                split = coordinates_raw.split(',')
                coordinates = int(split[0]), int(split[1])
                if (self.board.is_valid_coordinates(coordinates)):
                    return coordinates
                else:
                    raise Exception("invalid coordinates, try again")
            except KeyError or ValueError:
                print("please input coordinates in the following format: x,y")
            except Exception as e:
                print(e)
