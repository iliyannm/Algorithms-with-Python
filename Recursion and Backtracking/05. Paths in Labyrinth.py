def find_path(row, col, rows, cols, board, path, direction):
    if row < 0 or col < 0 or row == rows or col == cols:
        return

    if board[row][col] == 'v' or board[row][col] == '*':
        return

    path.append(direction)

    if board[row][col] == 'e':
        print(''.join(path))
    else:
        board[row][col] = 'v'
        find_path(row - 1, col, rows, cols, board, path, 'U')
        find_path(row + 1, col, rows, cols,  board, path, 'D')
        find_path(row, col - 1, rows, cols,  board, path, 'L')
        find_path(row, col + 1, rows, cols,  board, path, 'R')
        board[row][col] = '-'

    path.pop()


rows = int(input())
cols = int(input())
board = []

for _ in range(rows):
    board.append(list(input()))

find_path(0, 0, rows, cols, board, [], '')
