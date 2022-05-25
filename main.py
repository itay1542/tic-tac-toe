from src.view.console_board_view import ConsoleBoardView
from src.state import StateChecker
from src.tic_tac_toe_runner import TicTacToeRunner
from src.data.board import Board

def init_board():
    board_size = int(input("choose board size --->"))
    return Board(board_size)

def main():
    state_checker = StateChecker()
    board_view = ConsoleBoardView()
    runner = TicTacToeRunner(state_checker, board_view, init_board())
    runner.run()


if __name__ == '__main__':
    main()
