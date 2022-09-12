def dfs(node, graph, visited, component):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)


n = int(input())
graph = []

for i in range(n):
    line = input()
    graph.append([] if line == '' else [int(x) for x in line.split()])

visited = [None] * n

for node in range(len(graph)):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)
    print(f"Connected component: {' '.join(str(x) for x in component)}")
