METADATA = {
    "id": 597,
    "name": "Friend Requests I: Overall Acceptance Rate",
    "slug": "friend-requests-i-overall-acceptance-rate",
    "category": "Math",
    "aliases": [],
    "tags": ["logic", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the overall acceptance rate of friend requests given a list of sent and accepted requests.",
}

def solve(friend_requests: list[list[int]], accepted_friend_requests: list[list[int]]) -> float:
    """
    Calculates the overall acceptance rate of friend requests.

    The overall acceptance rate is defined as the total number of accepted 
    friend requests divided by the total number of sent friend requests.

    Args:
        friend_requests: A list of pairs [u, v] representing a sent request from u to v.
        accepted_friend_requests: A list of pairs [u, v] representing an accepted request from u to v.

    Returns:
        The overall acceptance rate as a float.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 4]], [[1, 2], [3, 4]])
        0.6666666666666666
        >>> solve([[1, 2]], [[1, 2]])
        1.0
        >>> solve([], [])
        0.0
    """
    # Handle the edge case where no requests were sent to avoid division by zero
    if not friend_requests:
        return 0.0

    total_sent = len(friend_requests)
    total_accepted = len(accepted_friend_requests)

    # The rate is simply the ratio of accepted to total sent
    return total_accepted / total_sent
