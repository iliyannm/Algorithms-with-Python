def find_paths(row, col, map, paths):
    if row >= len(map) or col >= len(map[0]):
        return

    if map[row][col] == 'v':
        return

    if map[row][col] == 'e':
        paths.append(0)
    else:
        map[row][col] = 'v'
        find_paths(row + 1, col, map, paths)
        find_paths(row, col + 1, map, paths)
        map[row][col] = '-'

    return len(paths)


m = int(input())
n = int(input())

map = []
for _ in range(m):
    map.append(['-'] * n)

map[m - 1][n - 1] = 'e'

print(find_paths(0, 0, map, []))
