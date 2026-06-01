METADATA = {
    "id": 1583,
    "name": "Count Unhappy Friends",
    "slug": "count_unhappy_friends",
    "category": "array",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Counts how many friends are unhappy based on their preferences and current pairings.",
}


def solve(
    n: int,
    preferences: list[list[int]],
    pairs: list[list[int]],
) -> int:
    """Count the number of unhappy friends.

    Args:
        n: The total number of friends, labeled from 0 to n-1.
        preferences: A list where preferences[i] is a list of friend IDs ordered
            by i's preference (most preferred first).
        pairs: A list of length n/2 where each element is a pair [x, y] indicating
            that x and y are currently paired together.

    Returns:
        The number of friends that are unhappy according to the problem definition.

    Examples:
        >>> solve(4, [[1,2,3],[3,2,0],[3,1,0],[1,2,0]], [[0,1],[2,3]])
        2
        >>> solve(2, [[1],[0]], [[0,1]])
        0
    """
    # Build a quick lookup for each friend's ranking of every other friend.
    rank = [[0] * n for _ in range(n)]
    for friend_id, pref_list in enumerate(preferences):
        for position, other_friend in enumerate(pref_list):
            rank[friend_id][other_friend] = position

    # Map each friend to their current partner.
    partner = [0] * n
    for x, y in pairs:
        partner[x] = y
        partner[y] = x

    unhappy = set()

    # For each friend, examine only those friends they prefer over their current partner.
    for friend_id in range(n):
        current_partner = partner[friend_id]
        # Iterate through the preference list until we reach the current partner.
        for preferred_friend in preferences[friend_id]:
            if preferred_friend == current_partner:
                break
            # If the preferred friend also prefers this friend over their own partner,
            # then the friend is unhappy.
            if rank[preferred_friend][friend_id] < rank[preferred_friend][partner[preferred_friend]]:
                unhappy.add(friend_id)
                break  # No need to check further preferences for this friend.

    return len(unhappy)