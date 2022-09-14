def dfs(parent, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != parent:
        return

    visited[row][col] = True
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row - 1, col, matrix, visited)
    dfs(parent, row, col + 1, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []
areas = {}

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
        if key not in areas:
            areas[key] = 0
        areas[key] += 1

print(f"Areas: {sum(x for x in areas.values())}")
for k in sorted(areas.keys()):
    print(f"Letter '{k}' -> {areas[k]}")
