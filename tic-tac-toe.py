board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Function to check if a player has won
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Main game loop
current_player = 'X'
while True:
    print_board()
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != ' ':
        print("Invalid move. Try again.")
        continue

    board[move] = current_player

    if check_win(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break

    if ' ' not in board:
        print_board()
        print("It's a draw!")
        break

    current_player = 'O' if current_player == 'X' else 'X'