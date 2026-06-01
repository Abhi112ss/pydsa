METADATA = {
    "id": 2600,
    "name": "K Items With the Maximum Sum",
    "slug": "k_items_with_the_maximum_sum",
    "category": "greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Return the maximum possible sum of exactly k elements from the given array.",
}


def solve(nums: list[int], k: int) -> int:
    """Return the maximum sum of exactly ``k`` items from ``nums``.

    Args:
        nums: List of integer values.
        k: Number of items to select; ``0 <= k <= len(nums)``.

    Returns:
        The maximum possible sum obtained by selecting exactly ``k`` elements.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        12
        >>> solve([-5, -2, -1, 0, 1], 2)
        1
    """
    # Sort the list in descending order to bring the largest values to the front.
    nums.sort(reverse=True)

    # Sum the first ``k`` elements, which are the largest after sorting.
    maximum_sum = sum(nums[:k])

    return maximum_sum