from flight_graph_data import FLIGHT_GRAPH

def dfs_search(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    if start == goal:
        return path

    visited.add(start)

    for neighbor in graph.get(start, {}):
        if neighbor not in visited:
            result = dfs_search(graph, neighbor, goal, path + [neighbor], visited)
            if result is not None:
                return result

    return None

if __name__ == "__main__":
    route = dfs_search(FLIGHT_GRAPH, 'Jakarta', 'Bali')
    print("Rute DFS:", " -> ".join(route) if route else "Rute tidak ditemukan")