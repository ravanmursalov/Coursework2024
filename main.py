class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.grid:
            print("|".join(row))
            print("-----")

    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row)

    def is_cell_empty(self, row, col):
        return self.grid[row][col] == " "

    def place_mark(self, row, col, player):
        self.grid[row][col] = player.mark


class Player:
    def __init__(self, mark):
        self.mark = mark

    def make_move(self, board):
        while True:
            row = int(input(f"Enter row (0, 1, or 2) for {self.mark}: "))
            col = int(input(f"Enter column (0, 1, or 2) for {self.mark}: "))
            if 0 <= row < 3 and 0 <= col < 3 and board.is_cell_empty(row, col):
                board.place_mark(row, col, self)
                break
            else:
                print("Invalid move. Try again.")


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.turn = 0

    def check_winner(self, player):
        mark = player.mark
        b = self.board.grid
        for i in range(3):
            if all(b[i][j] == mark for j in range(3)) or all(b[j][i] == mark for j in range(3)):
                return True
        if all(b[i][i] == mark for i in range(3)) or all(b[i][2 - i] == mark for i in range(3)):
            return True
        return False

    def play(self):
        print("Welcome to Tic-Tac-Toe!")

        while True:
            self.board.print_board()
            current_player = self.players[self.turn]
            print(f"Player {current_player.mark}'s turn.")

            current_player.make_move(self.board)

            if self.check_winner(current_player):
                self.board.print_board()
                print(f"Player {current_player.mark} wins!")
                break
            elif self.board.is_full():
                self.board.print_board()
                print("It's a tie!")
                break

            self.turn = (self.turn + 1) % 2


if __name__ == "__main__":
    game = Game()
    game.play()
