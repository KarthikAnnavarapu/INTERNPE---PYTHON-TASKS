# Tic Tac Toe

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if the game is over
def is_game_over(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    # Check if the board is full
    for row in board:
        if " " in row:
            return False
    return True

# Function to check if a move is valid
def is_valid_move(board, row, col):
    return row >= 0 and row < 3 and col >= 0 and col < 3 and board[row][col] == " "

# Function to make a move
def make_move(board, row, col, symbol):
    board[row][col] = symbol

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while not is_game_over(board):
        print_board(board)
        print("Player " + current_player + ", enter your move (row, col): ")
        move = input().split(",")
        row, col = map(int, move)

        if is_valid_move(board, row, col):
            make_move(board, row, col, current_player)
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        else:
            print("Invalid move. Try again.")

    print_board(board)
    print("Game over!")

# Start the game
play_game()
