from typing import List


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.children: List[TreeNode] = []

    def get_value(self) -> int:
        return self.value

    def get_chile_nodes(self):
        return self.children


def is_leaf(node: TreeNode):
    return len(node.get_chile_nodes()) == 0


def leaf_sum(node: TreeNode):
    if node is None:
        return 0
    if is_leaf(node):
        return node.get_value()
    total = 0
    for child in node.get_chile_nodes():
        total += leaf_sum(child)
    return total


if __name__ == '__main__':
    data = [2, 9, 1, -6, 4, 5, 3, 0, 7, -4, 8]
    adjacent_list = [
        [],
        [],
        [0, 1],
        [],
        [2, 3],
        [4, 6],
        [7, 8, 9],
        [],
        [10],
        [],
        []
    ]
    nodes = [TreeNode(data[x]) for x in range(len(data))]
    for i, adj in enumerate(adjacent_list):
        for x in adj:
            nodes[i].children.append(nodes[x])
    print(leaf_sum(nodes[5]))
