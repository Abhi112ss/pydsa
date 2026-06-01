METADATA = {
    "id": 2121,
    "name": "Intervals Between Identical Elements",
    "slug": "intervals-between-identical-elements",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "prefix_sum", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of the lengths of all intervals between identical elements in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of the lengths of all intervals between identical elements.
    
    The length of an interval between two indices i and j (i < j) is (j - i - 1).
    For a set of indices [i1, i2, ..., ik] where nums[i1] == nums[i2] == ... == nums[ik],
    the sum of all pairwise (j - i - 1) can be computed efficiently using prefix sums.
    
    Mathematical derivation:
    Sum = sum_{1 <= a < b <= k} (idx[b] - idx[a] - 1)
    Sum = sum_{1 <= a < b <= k} (idx[b] - idx[a]) - sum_{1 <= a < b <= k} (1)
    The number of pairs is k * (k - 1) / 2.
    The sum of (idx[b] - idx[a]) can be calculated by tracking the sum of indices 
    seen so far and the count of elements seen so far.

    Args:
        nums: A list of integers.

    Returns:
        The total sum of the lengths of all intervals between identical elements.

    Examples:
        >>> solve([1, 4, 1, 2, 1, 4, 1])
        10
        >>> solve([1, 1, 1, 1])
        4
        >>> solve([1, 2, 3, 4])
        0
    """
    # Maps element value to a tuple: (count_of_occurrences, sum_of_indices_seen_so_far)
    # Using a dictionary to store running statistics for each unique number.
    tracker: dict[int, tuple[int, int]] = {}
    total_interval_sum = 0

    for current_index, value in enumerate(nums):
        if value in tracker:
            count, sum_indices = tracker[value]
            
            # For the current index 'j', we want to add (j - i - 1) for all previous 'i's.
            # Sum_{i < j} (j - i - 1) = (count * j) - (sum_of_previous_indices) - count
            total_interval_sum += (count * current_index) - sum_indices - count
            
            # Update the tracker with the new count and the new sum of indices
            tracker[value] = (count + 1, sum_indices + current_index)
        else:
            # First time seeing this element
            tracker[value] = (1, current_index)

    return total_interval_sum
