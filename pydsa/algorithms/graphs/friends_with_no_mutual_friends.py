METADATA = {
    "id": 3058,
    "name": "Friends With No Mutual Friends",
    "slug": "friends_with_no_mutual_friends",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "hash_map", "set"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the number of pairs of friends who do not share any mutual friends.",
}

def solve(n: int, friendships: list[list[int]]) -> int:
    """
    Calculates the number of pairs of friends who have no mutual friends.

    A pair of friends (u, v) is counted if they are friends and the intersection
    of their friendship sets is empty.

    Args:
        n: The number of people in the network.
        friendships: A list of pairs [u, v] representing a friendship.

    Returns:
        The count of friend pairs with zero mutual friends.

    Examples:
        >>> solve(4, [[0, 1], [1, 2], [2, 3], [3, 0]])
        4
        >>> solve(3, [[0, 1], [1, 2]])
        0
    """
    # Build an adjacency list using sets for O(1) average lookup and intersection
    adj: dict[int, set[int]] = {}
    
    # Initialize adjacency list for all nodes to handle potential isolated nodes
    for i in range(n):
        adj[i] = set()

    # Populate the friendship network
    for u, v in friendships:
        adj[u].add(v)
        adj[v].add(u)

    mutual_friendless_count = 0

    # Iterate through each unique friendship pair
    # We only check existing friendships, so we iterate through the input list
    # To avoid double counting (u,v) and (v,u), we ensure u < v
    seen_pairs = set()
    
    for u, v in friendships:
        # Normalize pair to ensure uniqueness in the set
        pair = (min(u, v), max(u, v))
        if pair in seen_pairs:
            continue
        seen_pairs.add(pair)

        # Check if the intersection of their friend sets is empty
        # The intersection operation on sets is efficient
        if not (adj[u] & adj[v]):
            mutual_friendless_count += 1

    return mutual_friendless_count
