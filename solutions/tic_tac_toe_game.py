def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn.")

        try:
            row, col = map(
                int,
                input(
                    "Enter row and column (0, 1, or 2 separated by a space): "
                ).split(),
            )
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid position. Please enter numbers between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("Position already taken. Choose another.")
            continue

        board[row][col] = current_player
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print("It's a tie!")
            break

        turn += 1


if __name__ == "__main__":
    tic_tac_toe()
