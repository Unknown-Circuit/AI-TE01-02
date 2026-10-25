import heapq
from flight_graph_data import FLIGHT_GRAPH

def astar_search(graph, start, goal):
    # Priority Queue Simpan: (f_score, current_node, path, total_cost)
    pq = [(0, start, [start], 0)]
    visited = {}

    while pq:
        f_score, current, path, cost = heapq.heappop(pq)

        if current == goal:
            return path, cost

        if current in visited and visited[current] <= cost:
            continue
        visited[current] = cost

        for neighbor, weight in graph.get(current, {}).items():
            new_cost = cost + weight
            # Heuristik sederhana = 0 (Dijkstra Equivalent)
            h_score = 0 
            heapq.heappush(pq, (new_cost + h_score, neighbor, path + [neighbor], new_cost))

    return None, float("inf")

if __name__ == "__main__":
    route, total_cost = astar_search(FLIGHT_GRAPH, 'Jakarta', 'Bali')
    if route:
        print(f"Rute Optimal A*: {' -> '.join(route)}")
        print(f"Total Biaya: Rp {total_cost * 1000:,}")
    else:
        print("Rute tidak ditemukan")