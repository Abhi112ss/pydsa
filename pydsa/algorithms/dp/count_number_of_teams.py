METADATA = {
    "id": 1395,
    "name": "Count Number of Teams",
    "slug": "count-number-of-teams",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of triplets (i, j, k) such that the elements at these indices are in strictly increasing or strictly decreasing order.",
}

def solve(rating: list[int]) -> int:
    """
    Counts the number of valid triplets (i, j, k) where i < j < k and 
    rating[i] < rating[j] < rating[k] OR rating[i] > rating[j] > rating[k].

    Args:
        rating: A list of integers representing the ratings of players.

    Returns:
        The total number of valid triplets.

    Examples:
        >>> solve([2, 5, 3, 4, 1])
        3
        >>> solve([1, 2, 3, 4])
        4
    """
    n = len(rating)
    total_teams = 0

    # We iterate through each element treating it as the middle element 'j' of the triplet.
    # For a fixed j, the number of increasing triplets is (count of smaller to left) * (count of larger to right).
    # The number of decreasing triplets is (count of larger to left) * (count of smaller to right).
    for j in range(n):
        smaller_left = 0
        larger_left = 0
        smaller_right = 0
        larger_right = 0

        # Count elements to the left of j
        for i in range(j):
            if rating[i] < rating[j]:
                smaller_left += 1
            elif rating[i] > rating[j]:
                larger_left += 1

        # Count elements to the right of j
        for k in range(j + 1, n):
            if rating[k] < rating[j]:
                smaller_right += 1
            elif rating[k] > rating[j]:
                larger_right += 1

        # Calculate combinations for both increasing and decreasing patterns
        # Increasing: rating[i] < rating[j] < rating[k]
        total_teams += (smaller_left * larger_right)
        # Decreasing: rating[i] > rating[j] > rating[k]
        total_teams += (larger_left * smaller_right)

    return total_teams
