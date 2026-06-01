METADATA = {
    "id": 575,
    "name": "Distribute Candies",
    "slug": "distribute_candies",
    "category": "array",
    "aliases": [],
    "tags": ["hash_set", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the maximum number of different candy types the sister can receive.",
}


def solve(candies: list[int]) -> int:
    """Calculate the maximum number of distinct candy types the sister can get.

    Args:
        candies: A list of integers where each integer represents a type of candy.

    Returns:
        The maximum possible number of different candy types the sister can receive.

    Examples:
        >>> solve([1, 1, 2, 2, 3, 3])
        3
        >>> solve([1, 1, 2, 3])
        2
    """
    # Count distinct candy types using a hash set.
    distinct_candy_types = len(set(candies))

    # The sister can receive at most half of the total candies.
    max_candies_for_sister = len(candies) // 2

    # The answer is limited by both constraints.
    return distinct_candy_types if distinct_candy_types < max_candies_for_sister else max_candies_for_sister