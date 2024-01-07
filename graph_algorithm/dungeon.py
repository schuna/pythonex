number_rows = 5
number_cols = 7
maze = [
    ['.', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'E', '.', '#', '.']
]
sr = 0
sc = 0
rq = []
cq = []

move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

reached_end = False

visited = [[False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False]]

dr = [-1, 1, 0, 0]
dc = [0, 0, +1, -1]


def explore_neighbors(r, c):
    global nodes_in_next_layer
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr < 0 or rr >= number_rows or cc < 0 or cc >= number_cols:
            continue
        if visited[rr][cc]:
            continue
        if maze[rr][cc] == '#':
            continue
        rq.append(rr)
        cq.append(cc)
        visited[rr][cc] = True
        nodes_in_next_layer += 1


def solve():
    global move_count, nodes_left_in_layer, nodes_in_next_layer, reached_end
    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True
    while len(rq) != 0:
        r = rq.pop(0)
        c = cq.pop(0)
        if maze[r][c] == 'E':
            reached_end = True
            break
        explore_neighbors(r, c)
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end:
        return move_count
    return -1


if __name__ == '__main__':
    result = solve()
    print(result)
