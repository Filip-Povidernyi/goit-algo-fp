import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
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


lst = [x for x in range(1, 15)]


heapq.heapify(lst)
tree = build_tree_from_heap(lst)
draw_tree(tree)
