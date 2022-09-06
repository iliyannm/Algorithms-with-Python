def print_board(board):
    for r in range(len(board)):
        print(' '.join(board[r]))
    print()


def can_place_queen(row, col, rows, cols, right_diagonals, left_diagonals):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left_diagonals:
        return False
    if (row + col) in right_diagonals:
        return False
    return True


def set_queen(row, col, board, rows, cols, right_diagonals, left_diagonals):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(row, col, board, rows, cols, right_diagonals, left_diagonals):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def put_queens(row, board, rows, cols, right_diagonals, left_diagonals):
    if row == 8:
        print_board(board)
        return

    for col in range(8):
        if can_place_queen(row, col, rows, cols, right_diagonals, left_diagonals):
            set_queen(row, col, board, rows, cols, right_diagonals, left_diagonals)
            put_queens(row + 1, board, rows, cols, right_diagonals, left_diagonals)
            remove_queen(row, col, board, rows, cols, right_diagonals, left_diagonals)

n = 8
board = []

for _ in range(n):
    board.append(['-'] * n)


put_queens(0, board, set(), set(), set(), set())
