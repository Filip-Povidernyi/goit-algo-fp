import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())
        self.color = color


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree Visualization"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }
    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors
    )
    plt.show()


def build_tree_from_heap(heap):
    if not heap:
        return None

    root_value = heapq.heappop(heap)
    root = Node(root_value)
    nodes = [root]
    while nodes and heap:
        current_node = nodes.pop(0)

        left_child_value = heapq.heappop(heap)
        if left_child_value is not None:
            left_child = Node(left_child_value)
            current_node.left = left_child
            nodes.append(left_child)

        if heap:
            right_child_value = heapq.heappop(heap)
            if right_child_value is not None:
                right_child = Node(right_child_value)
                current_node.right = right_child
                nodes.append(right_child)

    return root


def generate_gradient_colors(n, start="#800000", end="#ffa500"):
    def hex_to_rgb(hex):
        return tuple(int(hex[i:i+2], 16) for i in (1, 3, 5))

    def rgb_to_hex(rgb):
        return "#" + "".join(f"{v:02X}" for v in rgb)

    start_rgb = hex_to_rgb(start)
    end_rgb = hex_to_rgb(end)
    gradient = []
    for i in range(n):
        mix = tuple(
            int(start_rgb[j] + (float(i) / (n - 1))
                * (end_rgb[j] - start_rgb[j]))
            for j in range(3)
        )
        gradient.append(rgb_to_hex(mix))
    return gradient


def bfs_coloring(root):
    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    colors = generate_gradient_colors(len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i]


def dfs_coloring(root):
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)
    colors = generate_gradient_colors(len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i]


if __name__ == '__main__':

    lst = [x for x in range(1, 15)]
    heapq.heapify(lst)
    tree_bfs = build_tree_from_heap(lst.copy())
    bfs_coloring(tree_bfs)
    draw_tree(tree_bfs, title="BFS Traversal Visualization")
    tree_dfs = build_tree_from_heap(lst.copy())
    dfs_coloring(tree_dfs)
    draw_tree(tree_dfs, title="DFS Traversal Visualization")
