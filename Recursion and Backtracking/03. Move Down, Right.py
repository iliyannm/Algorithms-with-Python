def find_paths(row, col, trace, paths):
    if row >= len(trace) or col >= len(trace[0]):
        return

    if trace[row][col] == '!':
        return

    if row == len(trace) - 1 and col == len(trace[0]) - 1:
        paths.append(0)
    else:
        trace[row][col] = '!'
        find_paths(row + 1, col, trace, paths)
        find_paths(row, col + 1, trace, paths)
        trace[row][col] = '-'

    return len(paths)


rows = int(input())
cols = int(input())

matrix = []

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        matrix[i].append('-')

print(find_paths(0, 0, matrix, []))
