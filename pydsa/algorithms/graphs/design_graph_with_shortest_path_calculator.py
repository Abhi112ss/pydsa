METADATA = {
    "id": 2642,
    "name": "Design Graph With Shortest Path Calculator",
    "slug": "design-graph-with-shortest-path-calculator",
    "category": "Design",
    "aliases": [],
    "tags": ["dijkstra", "graph", "priority_queue", "shortest-path"],
    "difficulty": "hard",
    "time_complexity": "O(E log V) per query",
    "space_complexity": "O(V + E)",
    "description": "Design a graph data structure that supports adding edges and calculating the shortest path between two nodes using Dijkstra's algorithm.",
}

import heapq

class Graph:
    """
    A graph implementation that supports adding weighted edges and 
    calculating the shortest path between two nodes using Dijkstra's algorithm.
    """

    def __init__(self, n: int):
        """
        Initializes the graph with n nodes.

        Args:
            n (int): The number of nodes in the graph (labeled 0 to n-1).
        """
        self.n = n
        # Adjacency list: list of lists containing (neighbor, weight) tuples
        self.adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, weight: int) -> None:
        """
        Adds an undirected weighted edge between nodes u and v.

        Args:
            u (int): The first node.
            v (int): The second node.
            weight (int): The weight of the edge.
        """
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def shortest_path(self, start_node: int, end_node: int) -> int:
        """
        Calculates the shortest path from start_node to end_node using Dijkstra's algorithm.

        Args:
            start_node (int): The starting node.
            end_node (int): The destination node.

        Returns:
            int: The shortest distance between the two nodes. Returns -1 if no path exists.

        Examples:
            >>> g = Graph(3)
            >>> g.add_edge(0, 1, 10)
            >>> g.add_edge(1, 2, 20)
            >>> g.shortest_path(0, 2)
            30
            >>> g.shortest_path(0, 3) # Assuming node 3 doesn't exist or is disconnected
            -1
        """
        # Distances array initialized to infinity
        distances = [float('inf')] * self.n
        distances[start_node] = 0
        
        # Min-priority queue stores (current_distance, current_node)
        priority_queue: list[tuple[int, int]] = [(0, start_node)]

        while priority_queue:
            current_dist, u = heapq.heappop(priority_queue)

            # If we found a shorter path to u already, skip this entry
            if current_dist > distances[u]:
                continue
            
            # Optimization: if we reached the target, we can return immediately
            if u == end_node:
                return int(current_dist)

            # Explore neighbors
            for v, weight in self.adj[u]:
                new_dist = current_dist + weight
                
                # Relaxation step
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(priority_queue, (new_dist, v))

        # If end_node distance is still infinity, no path exists
        result = distances[end_node]
        return int(result) if result != float('inf') else -1

def solve():
    """
    Example usage of the Graph class.
    """
    # Example 1
    g1 = Graph(3)
    g1.add_edge(0, 1, 10)
    g1.add_edge(1, 2, 20)
    print(f"Shortest path 0 to 2: {g1.shortest_path(0, 2)}")  # Expected: 30

    # Example 2
    g2 = Graph(4)
    g2.add_edge(0, 1, 1)
    g2.add_edge(1, 2, 1)
    g2.add_edge(2, 3, 1)
    g2.add_edge(0, 3, 10)
    print(f"Shortest path 0 to 3: {g2.shortest_path(0, 3)}")  # Expected: 3

    # Example 3: Disconnected graph
    g3 = Graph(3)
    g3.add_edge(0, 1, 5)
    print(f"Shortest path 0 to 2: {g3.shortest_path(0, 2)}")  # Expected: -1
