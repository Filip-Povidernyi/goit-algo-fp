import networkx as nx
import heapq


def dijkstra(graph, start):
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    visited = set()
    distances = {vertex: float("infinity") for vertex in graph.nodes}
    distances[start] = 0

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == '__main__':

    G = nx.Graph()

    cities = ['Kyiv', 'Lviv', 'Kharkiv', 'Odesa', 'Dnipro', 'Zaporizhzhia']
    G.add_nodes_from(cities)

    roads = [
        ('Kyiv', 'Lviv', 540),
        ('Kyiv', 'Kharkiv', 480),
        ('Kyiv', 'Odesa', 475),
        ('Lviv', 'Odesa', 790),
        ('Odesa', 'Dnipro', 500),
        ('Dnipro', 'Zaporizhzhia', 85),
        ('Kharkiv', 'Dnipro', 215),
        ('Zaporizhzhia', 'Kyiv', 500)
    ]

    G.add_weighted_edges_from(roads)

    start = 'Dnipro'

    shortest_paths = dijkstra(G, start)

    for vertex, distance in shortest_paths.items():
        print(f"Найкоротша відстань від {start} до {vertex}: {distance}")
