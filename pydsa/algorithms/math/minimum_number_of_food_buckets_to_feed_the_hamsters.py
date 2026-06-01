METADATA = {
    "id": 2086,
    "name": "Minimum Number of Food Buckets to Feed the Hamsters",
    "slug": "minimum_number_of_food_buckets_to_feed_the_hamsters",
    "category": "math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the minimum number of 5‑unit food buckets required to satisfy all hamsters' food requirements.",
}


def solve(requirements: list[int]) -> int:
    """Calculate the minimum number of 5‑unit food buckets needed.

    Args:
        requirements: A list of non‑negative integers where each integer
            represents the amount of food a hamster requires.

    Returns:
        The smallest integer number of buckets (each bucket holds 5 units)
        that can satisfy the total food requirement.

    Examples:
        >>> solve([1, 2, 3])
        2
        >>> solve([5, 5, 5])
        3
        >>> solve([])
        0
    """
    total_food = 0
    for amount in requirements:
        total_food += amount  # accumulate total food required

    # ceiling division by 5: (total + 4) // 5
    return (total_food + 4) // 5 if total_food > 0 else 0