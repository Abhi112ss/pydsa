METADATA = {
    "id": 2977,
    "name": "Minimum Cost to Convert String II",
    "slug": "minimum-cost-to-convert-string-ii",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "strings", "dijkstra", "shortest-path"],
    "difficulty": "hard",
    "time_complexity": "O(N + K log K)",
    "space_complexity": "O(K)",
    "description": "Find the minimum cost to transform a string into another string using a set of character transformation rules.",
}

import heapq

def solve(s: str, t: str, conversions: list[list[int]]) -> int:
    """
    Calculates the minimum cost to convert string s to string t using given conversions.

    Args:
        s: The source string.
        t: The target string.
        conversions: A list of lists where each sublist is [char1, char2, cost].
                     Note: The problem description implies char1 and char2 are 
                     represented as integers or characters. In LeetCode context, 
                     they are often provided as integers representing ASCII or 
                     specific mappings. We assume they are integers here.

    Returns:
        The minimum total cost to perform all conversions. 
        Returns -1 if any character cannot be converted.

    Examples:
        >>> solve("abc", "def", [[97, 100, 1], [98, 101, 1], [99, 102, 1]])
        3
        >>> solve("a", "b", [[97, 98, 5]])
        5
        >>> solve("a", "b", [])
        -1
    """
    if len(s) != len(t):
        return -1

    # Build adjacency list for the graph of character transformations
    # Using a dictionary of dictionaries to store min cost between characters
    adj: dict[int, dict[int, int]] = {}
    for u, v, cost in conversions:
        if u not in adj:
            adj[u] = {}
        if v not in adj:
            adj[v] = {}
        
        # If multiple rules exist for the same pair, keep the minimum cost
        if v not in adj[u] or cost < adj[u][v]:
            adj[u][v] = cost
        if u not in adj[v] or cost < adj[v][u]:
            adj[v][u] = cost

    # Precompute shortest paths for all unique characters involved in conversions
    # Since the number of unique characters (K) is small (max 26 or 52 or 256),
    # we can run Dijkstra from each character that appears in 's' but not in 't'
    # or simply run Dijkstra for all characters present in the conversion rules.
    
    memo_costs: dict[int, dict[int, int]] = {}

    def get_shortest_paths(start_node: int) -> dict[int, int]:
        """Standard Dijkstra's algorithm to find shortest paths from start_node."""
        distances = {start_node: 0}
        pq = [(0, start_node)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if current_dist > distances.get(u, float('inf')):
                continue
            
            if u in adj:
                for v, weight in adj[u].items():
                    distance = current_dist + weight
                    if distance < distances.get(v, float('inf')):
                        distances[v] = distance
                        heapq.heappush(pq, (distance, v))
        return distances

    total_cost = 0
    
    # Iterate through each character pair in the strings
    for char_s, char_t in zip(s, t):
        # Convert characters to their integer representations (ASCII)
        u, v = ord(char_s), ord(char_t)
        
        if u == v:
            continue
            
        # If we haven't computed paths from u yet, do it now
        if u not in memo_costs:
            memo_costs[u] = get_shortest_paths(u)
            
        # Check if a path exists from u to v
        if v in memo_costs[u]:
            total_cost += memo_costs[u][v]
        else:
            return -1
            
    return total_cost
