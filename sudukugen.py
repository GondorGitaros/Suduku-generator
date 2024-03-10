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
                print(board[row][col-1], end='|')
            else:
                print(board[row][col-1], end=' ')
        row+=1
        if row % 3 == 0 and row != 9:
            print('\n' + '------' * 3)
        else:
            print()

def randnum():
    return random.randint(1,9)

print(randnum())
