METADATA = {
    "id": 455,
    "name": "Assign Cookies",
    "slug": "assign_cookies",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Determine the maximum number of children that can be satisfied with given cookie sizes.",
}

def solve(greed_factors: list[int], cookie_sizes: list[int]) -> int:
    """Assign cookies to children to maximize satisfied count.

    Args:
        greed_factors: List of integers where each value represents a child's minimum
            cookie size needed to be content.
        cookie_sizes: List of integers where each value represents the size of a cookie.

    Returns:
        The maximum number of children that can be satisfied.

    Examples:
        >>> solve([1, 2, 3], [1, 1])
        1
        >>> solve([1, 2], [1, 2, 3])
        2
    """
    # Sort both lists to enable greedy matching of smallest sufficient cookie.
    sorted_greed = sorted(greed_factors)
    sorted_cookies = sorted(cookie_sizes)

    child_index = 0  # Index for the current child in sorted_greed
    cookie_index = 0  # Index for the current cookie in sorted_cookies
    satisfied_children = 0

    # Iterate while there are children and cookies left.
    while child_index < len(sorted_greed) and cookie_index < len(sorted_cookies):
        if sorted_cookies[cookie_index] >= sorted_greed[child_index]:
            # Cookie satisfies the child; move to next child and cookie.
            satisfied_children += 1
            child_index += 1
            cookie_index += 1
        else:
            # Cookie too small; try next larger cookie.
            cookie_index += 1

    return satisfied_children