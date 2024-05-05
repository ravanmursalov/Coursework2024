def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")


def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all(
            [board[j][i] == player for j in range(3)]
        ):
            return True
    if all([board[i][i] == player for i in range(3)]) or all(
        [board[i][2 - i] == player for i in range(3)]
    ):
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        player = players[turn]
        print(f"Player {player}'s turn.")

        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        turn = (turn + 1) % 2


if __name__ == "__main__":
    main()
