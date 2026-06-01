METADATA = {
    "id": 332,
    "name": "Reconstruct Itinerary",
    "slug": "reconstruct-itinerary",
    "category": "Graph",
    "aliases": [],
    "tags": ["depth_first_search", "graph", "hierholzer_algorithm"],
    "difficulty": "Hard",
    "time_complexity": "O(E log E)",
    "space_complexity": "O(E)",
    "description": "Reconstruct the itinerary from a list of airline tickets using Hierholzer's algorithm to find an Eulerian path.",
}

import collections

def solve(tickets: list[list[str]]) -> list[str]:
    """
    Reconstructs the itinerary from a list of airline tickets.
    
    The problem asks for the lexicographically smallest itinerary that uses 
    all tickets exactly once. This is equivalent to finding an Eulerian path 
    in a directed graph.

    Args:
        tickets: A list of pairs [from, to] representing flight tickets.

    Returns:
        A list of strings representing the reconstructed itinerary.

    Examples:
        >>> solve([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "JFK"], ["LHR", "SFO"]])
        ['JFK', 'MUC', 'LHR', 'SFO', 'JFK']
        >>> solve([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL",", "JFK"]])
        # (Note: Example logic depends on lexicographical order)
    """
    # Build adjacency list where destinations are stored in a min-heap (or sorted list)
    # to ensure we always pick the lexicographically smallest destination first.
    adj = collections.defaultdict(list)
    for src, dst in sorted(tickets, key=lambda x: x[1], reverse=True):
        # We sort in reverse so we can use pop() which is O(1) to get the smallest element
        adj[src].append(dst)

    itinerary = []

    def dfs(airport: str) -> None:
        """
        Performs a post-order DFS traversal to find the Eulerian path.
        """
        # While there are available flights from the current airport
        while adj[airport]:
            # Pick the lexicographically smallest destination
            next_destination = adj[airport].pop()
            dfs(next_destination)
        
        # Post-order: add the airport to the itinerary after all its neighbors are visited
        itinerary.append(airport)

    # The problem guarantees a valid itinerary starting from "JFK"
    dfs("JFK")

    # The itinerary is built in reverse order (post-order traversal)
    return itinerary[::-1]
