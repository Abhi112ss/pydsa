METADATA = {
    "id": 135,
    "name": "Candy",
    "slug": "candy",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Distribute candies to children such that children with higher ratings get more candies than their neighbors.",
}

def solve(ratings: list[int]) -> int:
    """
    Distributes candies to children based on their ratings using a two-pass greedy approach.

    Args:
        ratings: A list of integers representing the ratings of children.

    Returns:
        The minimum total number of candies required to satisfy the conditions.

    Examples:
        >>> solve([1, 0, 2])
        5
        >>> solve([1, 2, 2])
        4
    """
    n = len(ratings)
    if n == 0:
        return 0

    # Initialize every child with 1 candy to satisfy the minimum requirement
    candies = [1] * n

    # First pass: Left-to-right
    # Ensure a child has more candies than their left neighbor if they have a higher rating
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Second pass: Right-to-left
    # Ensure a child has more candies than their right neighbor if they have a higher rating
    # We use max() to ensure we don't violate the condition established in the first pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)
