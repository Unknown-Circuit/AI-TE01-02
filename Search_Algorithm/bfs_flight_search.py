from collections import deque
from flight_graph_data import FLIGHT_GRAPH

def bfs_search(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, {}):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

if __name__ == "__main__":
    route = bfs_search(FLIGHT_GRAPH, 'Jakarta', 'Bali')
    print("Rute BFS (Transit Minimal):", " -> ".join(route) if route else "Rute tidak ditemukan")