from typing import List

from graph_algorithm.data import bfs_adjacent_list

total_n = 13


def reconstructed_path(start: int, end: int, prev: List[int]):
    path = []
    at = end
    while at != -1:
        path.append(at)
        at = prev[at]

    path.reverse()
    if path[0] == start:
        return path
    return []


def solve(start: int) -> List[int]:
    queue = [start]
    visited = [False] * total_n
    visited[start] = True

    prev = [-1] * total_n
    while len(queue) != 0:
        node = queue.pop(0)
        neighbors = bfs_adjacent_list[node]
        for neighbor in neighbors:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                prev[neighbor] = node
    return prev


def bfs(start, end):
    prev = solve(start)
    return reconstructed_path(start, end, prev)


if __name__ == '__main__':
    start_node = 0
    end_node = 12
    r_path = bfs(start_node, end_node)
    print(r_path)
    r_path = bfs(start_node, 2)
    print(r_path)
