import random

board = [['0','0','0','0','0','0','0','0','0'],
         ['0','0','0','0','0','0','0','0','0'],
         ['0','0','0','0','0','0','0','0','0'],
         ['0','0','0','0','0','0','0','0','0'],
         ['0','0','0','0','0','0','0','0','0'],
         ['0','0','0','0','0','0','0','0','0'],
         ['0','0','0','0','0','0','0','0','0'],
         ['0','0','0','0','0','0','0','0','0'],
         ['0','0','0','0','0','0','0','0','0']]


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            col+=1
            if col % 3 == 0 and col != 9:
                if board[row][col-1] == '0':
                    print(' ', end=' || ')
                else:
                    print(board[row][col-1], end=' || ')
            else:
                if board[row][col-1] == '0':
                    print(' ', end=' | ')
                else:
                    print(board[row][col-1], end=' | ')
        row+=1
        if row % 3 == 0 and row != 9:
            print('\n' + '______' * 6)
        else:
            print('\n' + '------' * 6)

def randnum():
    return random.randint(1,9)

seen = []

for i in range(3):
    for j in range(3):
        possiblenum = str(randnum())
        if str(possiblenum) in seen:
            pass
        else:
            board[i][j] = possiblenum
            seen += board[i][j]

print_board(board)