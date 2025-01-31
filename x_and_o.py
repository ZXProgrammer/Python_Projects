# Tic Tac Toe 
game_over = False

row1 = ["-","-","-"]
row2 = ["-","-","-"]
row3 = ["-","-","-"]
board = [row1, row2, row3]

def display_board():
    for row in board:
        print(row)
      
def user_input_update_board(marker):
    while True:
        x_position = input("Enter Row [1 - 9]\n")
        if x_position == "1":
            if board[0][0] != "-":
                print("The cell is full")
                continue
            board[0][0] = marker
            break
        elif x_position == "2":
            if board[0][1] != "-":
                print("The cell is full")
                continue
            board[0][1] = marker
            break
        elif x_position == "3":
            if board[0][2] != "-":
                print("The cell is full")
                continue
            board[0][2] = marker
            break
        elif x_position == "4":
            if board[1][0] != "-":
                print("The cell is full")
                continue
            board[1][0] = marker
            break
        elif x_position == "5":
            if board[1][1] != "-":
                print("The cell is full")
                continue
            board[1][1] = marker
            break
        elif x_position == "6":
            if board[1][2] != "-":
                print("The cell is full")
                continue
            board[1][2] = marker
            break
        elif x_position == "7":
            if board[2][0] != "-":
                print("The cell is full")
                continue
            board[2][0] = marker
            break
        elif x_position == "8":
            if board[2][1] != "-":
                print("The cell is full")
                continue
            board[2][1] = marker
            break
        elif x_position == "9":
            if board[2][2] != "-":
                print("The cell is full")
                continue
            board[2][2] = marker
            break
        else:
            print("Incorrect Enter 1 or 9")

def row_checker(marker):
    if board[0][0] == marker and board[0][1] == marker and board[0][2] == marker:
        return True
    elif board[1][0] == marker and board[1][1] == marker and board[1][2] == marker:
        return True
    elif board[2][0] == marker and board[2][1] == marker and board[2][2] == marker:
        return True
    else:
        return False

def column_checker(marker):
    if board[0][0] == marker and board[1][0] == marker and board[2][0] == marker:
        return True
    elif board[0][1] == marker and board[1][1] == marker and board[2][1] == marker:
        return True
    elif board[0][2] == marker and board[1][2] == marker and board[2][2] == marker:
        return True
    else:
        return False
    
def diagonal_checker(marker):
    if board[0][0] == marker and board[1][1] == marker and board[2][2] == marker:
        return True
    elif board[0][2] == marker and board[1][1] == marker and board[2][0] == marker:
        return True
    else:
        return False
    
def win_checker(marker):
    if row_checker(marker) or column_checker(marker) or diagonal_checker(marker):
        return True
    else:
        False
    
for _ in range(8):
    user_input_update_board(marker = "x")
    Xgame_over = win_checker(marker="x")
    display_board()
    if Xgame_over:
        break
    
    user_input_update_board(marker = "o")
    Ogame_over = win_checker(marker = "o")
    display_board()
    if Ogame_over:
        break

if  Xgame_over:
    print("X wins")
elif Ogame_over:
    print("O wins")
else:
    print("Game is a draw")