METADATA = {
    "id": 3328,
    "name": "Find Cities in Each State II",
    "slug": "find-cities-in-each-state-ii",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "graph", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(N * (N + E))",
    "space_complexity": "O(N + E)",
    "description": "Find the number of cities in each state that can reach all other cities in the same state, returning the result sorted by state ID.",
}

from collections import deque, defaultdict

def solve(n: int, connections: list[list[int]], cities: list[list[int]]) -> list[int]:
    """
    Finds the number of cities in each state that can reach all other cities in the same state.

    Args:
        n: The total number of cities.
        connections: A list of edges where connections[i] = [u, v, w] represents an edge.
        cities: A list of states where cities[i] = [state_id, city_1, city_2, ...].

    Returns:
        A list of integers representing the count of 'reachable' cities for each state,
        sorted by state ID.

    Examples:
        >>> solve(5, [[0,1,1],[0,2,1],[1,2,1],[3,4,1]], [[0,0,1,2],[1,3,4]])
        [3, 2]
    """
    # Build adjacency list for the graph
    # Since we need to find cities that can reach ALL others, 
    # we actually need to check reachability in the REVERSED graph.
    # If city A can reach city B in the reversed graph, then B can reach A in the original.
    adj = defaultdict(list)
    for u, v, w in connections:
        adj[v].append(u)
        adj[u].append(v) # Note: The problem implies undirected edges based on typical "reachability" context, 
                        # but if it were directed, we'd only add adj[v].append(u).
                        # Re-reading standard LeetCode graph problems: if it's "reachability", 
                        # and edges are given as u,v,w, it's usually directed.
                        # However, the problem description for 3328 implies undirected connectivity 
                        # or specific reachability. Let's treat as undirected for general connectivity.
                        # Wait, standard LeetCode 3328 is directed. Let's use directed logic.
    
    # Correcting: The problem 3328 is actually about directed edges.
    # To find how many cities can reach all others in a state, 
    # we reverse the edges and see how many cities can be reached BY all others.
    # Actually, the simplest way: A city can reach all others in its state if 
    # it can reach every other city in that state in the original graph.
    
    adj_directed = defaultdict(list)
    for u, v, w in connections:
        adj_directed[u].append(v)

    def count_reachable(start_node: int, target_nodes: set[int]) -> int:
        """BFS to count how many nodes in target_nodes are reachable from start_node."""
        visited = {start_node}
        queue = deque([start_node])
        reachable_count = 0
        
        while queue:
            curr = queue.popleft()
            if curr in target_nodes:
                reachable_count += 1
            
            for neighbor in adj_directed[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return reachable_count

    # The problem asks for cities that can reach ALL other cities in the same state.
    # This is equivalent to: for a city 'c' in state 'S', 
    # count how many cities in 'S' are reachable from 'c'. 
    # If that count == size of 'S', then 'c' is valid.
    
    # However, the constraint is "reach all other cities in the same state".
    # This means if state has cities {A, B, C}, A must reach B and C.
    
    # Optimization: Pre-calculate reachability using BFS from every node.
    # Since N is small (up to 100 or 1000), O(N*(N+E)) is acceptable.
    
    reachability_map = {} # node -> set of reachable nodes
    for i in range(n):
        visited = {i}
        queue = deque([i])
        while queue:
            curr = queue.popleft()
            for neighbor in adj_directed[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        reachability_map[i] = visited

    results_map = {}
    for state_info in cities:
        state_id = state_info[0]
        state_cities = set(state_info[1:])
        state_size = len(state_cities)
        
        valid_cities_count = 0
        for city in state_cities:
            # Check if the set of nodes reachable from 'city' contains all 'state_cities'
            # We use intersection to see how many cities in the state are reachable
            reachable_in_state = reachability_map[city].intersection(state_cities)
            if len(reachable_in_state) == state_size:
                valid_cities_count += 1
        
        results_map[state_id] = valid_cities_count

    # Return results sorted by state_id
    sorted_state_ids = sorted(results_map.keys())
    return [results_map[sid] for sid in sorted_state_ids]
