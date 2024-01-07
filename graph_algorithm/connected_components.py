data = [
    [4, 8, 13, 14],
    [5],
    [9, 15],
    [9],
    [0, 8],
    [1, 16, 17],
    [7, 11],
    [6, 11],
    [0, 4, 14],
    [2, 3, 15],
    [15],
    [6, 7],
    [],
    [0, 14],
    [0, 13],
    [2, 9, 10],
    [5],
    [5]
]

visited = [False] * len(data)
components = [-1] * len(data)
count = 0


def dfs(node):
    visited[node] = True
    components[node] = count
    for neighbor in data[node]:
        if not visited[neighbor]:
            dfs(neighbor)


if __name__ == '__main__':
    for i in range(len(data)):
        if not visited[i]:
            count += 1
            dfs(i)

    print(count)
    print(components)
