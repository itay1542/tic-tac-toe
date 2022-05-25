from src.data.board import Board

class ConsoleBoardView:

    def show_board(self, board: Board):
        vertical_border = '|  '
        self.__print_horizontal_border(len(board.get_matrix()))
        for row in board.get_matrix():
            print(vertical_border , end="")
            for cell in row:
                print(" " if cell == 0 else 'X' if cell == 1 else 'O', vertical_border, end="")
            print()
            self.__print_horizontal_border(len(board.get_matrix()))

    def __print_horizontal_border(self, length):
        horizontal_border = ' --- '
        print(horizontal_border * length)