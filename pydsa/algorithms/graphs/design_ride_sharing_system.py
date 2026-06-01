METADATA = {
    "id": 3829,
    "name": "Design Ride Sharing System",
    "slug": "design_ride_sharing_system",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "graphs", "shortest_path", "dijkstra"],
    "difficulty": "hard",
    "time_complexity": "O(E log V) per query",
    "space_complexity": "O(V + E)",
    "description": "Design a system to manage rides between locations and find the minimum cost to travel between two points using Dijkstra's algorithm.",
}

import heapq
from collections import defaultdict

class RideSharingSystem:
    """
    A system to manage rides between locations and calculate the minimum cost
    to travel between any two locations using Dijkstra's algorithm.
    """

    def __init__(self):
        # Adjacency list: location -> list of (neighbor, cost)
        self.graph: dict[int, list[tuple[int, int]]] = defaultdict(list)

    def add_ride(self, from_location: int, to_location: int, cost: int) -> None:
        """
        Adds a ride between two locations. Rides are bidirectional.

        Args:
            from_location: The starting location ID.
            to_location: The destination location ID.
            cost: The cost of the ride.
        """
        self.graph[from_location].append((to_location, cost))
        self.graph[to_location].append((from_location, cost))

    def get_min_cost(self, start_location: int, end_location: int) -> int:
        """
        Calculates the minimum cost to travel from start_location to end_location
        using Dijkstra's algorithm.

        Args:
            start_location: The starting location ID.
            end_location: The destination location ID.

        Returns:
            The minimum cost to travel between the two locations. 
            Returns -1 if no path exists.

        Examples:
            >>> rss = RideSharingSystem()
            >>> rss.add_ride(1, 2, 10)
            >>> rss.add_ride(2, 3, 5)
            >>> rss.get_min_cost(1, 3)
            15
        """
        if start_location == end_location:
            return 0

        # Priority queue stores (cumulative_cost, current_location)
        priority_queue: list[tuple[int, int]] = [(0, start_location)]
        # Dictionary to track the minimum cost found so far for each location
        min_costs: dict[int, int] = {start_location: 0}

        while priority_queue:
            current_cost, current_node = heapq.heappop(priority_queue)

            # If we reached the destination, we found the shortest path due to Dijkstra's property
            if current_node == end_location:
                return current_cost

            # If we found a better path to this node already, skip processing
            if current_cost > min_costs.get(current_node, float('inf')):
                continue

            # Explore neighbors
            for neighbor, ride_cost in self.graph[current_node]:
                new_cost = current_cost + ride_cost
                
                # If this path to neighbor is cheaper than any previously found path
                if new_cost < min_costs.get(neighbor, float('inf')):
                    min_costs[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        return -1

def solve():
    """
    Example usage of the RideSharingSystem.
    """
    rss = RideSharingSystem()
    rss.add_ride(1, 2, 10)
    rss.add_ride(2, 3, 5)
    rss.add_ride(1, 3, 20)
    
    # Path 1->2->3 costs 15. Path 1->3 costs 20.
    print(f"Min cost 1 to 3: {rss.get_min_cost(1, 3)}")  # Expected: 15
    print(f"Min cost 1 to 4: {rss.get_min_cost(1, 4)}")  # Expected: -1
