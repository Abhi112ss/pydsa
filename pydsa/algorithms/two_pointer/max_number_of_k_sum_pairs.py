METADATA = {
    "id": 1679,
    "name": "Max Number of K-Sum Pairs",
    "slug": "max_number_of_k_sum_pairs",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of non-overlapping pairs that sum to a target value.",
}


def solve(nums: list[int], k: int) -> int:
    """Return the maximum number of non‑overlapping pairs whose sum equals *k*.

    Args:
        nums: List of integers.
        k: Target sum for each pair.

    Returns:
        The maximum count of disjoint pairs (i, j) such that nums[i] + nums[j] == k.

    Examples:
        >>> solve([1,2,3,4], 5)
        2
        >>> solve([3,1,3,4,3], 6)
        1
        >>> solve([1,2,3,4,5], 10)
        0
    """
    # Frequency map of numbers that have not yet been paired
    frequency: dict[int, int] = {}
    pair_count = 0

    for number in nums:
        complement = k - number
        # If a complement is available, form a pair and decrement its count
        if frequency.get(complement, 0) > 0:
            pair_count += 1
            frequency[complement] -= 1
        else:
            # Otherwise, store the current number for future matching
            frequency[number] = frequency.get(number, 0) + 1

    return pair_count