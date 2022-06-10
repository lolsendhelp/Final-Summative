def initialize_board():
    board = []
    for i in range(5):
        column = []
        for j in range(5):
            column.append(0)
        board.append(column)
    return board 

board = initialize_board()

ships = [board[2][1], board[1][1]]

column_hit = int(input("What column would you like to hit?: "))
row_hit = int(input("What row would you like to hit?: "))

if board[column_hit - 1][row_hit - 1] in ships:
    print("HIT!")

board[column_hit - 1][row_hit - 1] = "x"
print(board)

