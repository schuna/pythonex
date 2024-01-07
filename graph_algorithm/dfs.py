from graph_algorithm.data import adjacent_list

total_n = 13
visited = [False for _ in range(total_n)]


def dfs(pos):
    if visited[pos]:
        return
    print(f'visited = {pos}')
    visited[pos] = True

    neighbors = adjacent_list[pos]
    for next_pos in sorted(neighbors, reverse=True):
        dfs(next_pos)


if __name__ == '__main__':
    start_node = 0
    dfs(start_node)
    print(visited)
