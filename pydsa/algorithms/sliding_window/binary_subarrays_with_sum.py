METADATA = {
    "id": 930,
    "name": "Binary Subarrays With Sum",
    "slug": "binary_subarrays_with_sum",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum equal to goal.",
}

def solve(nums: list[int], goal: int) -> int:
    """
    Calculates the number of non-empty subarrays that sum up to the target goal.

    The algorithm uses a prefix sum approach with a hash map to count occurrences 
    of prefix sums encountered so far. For every index, we check how many 
    previous prefix sums satisfy the condition (current_prefix_sum - goal).

    Args:
        nums: A list of integers containing only 0s and 1s.
        goal: The target sum for the subarrays.

    Returns:
        The total number of subarrays whose elements sum to goal.

    Examples:
        >>> solve([1, 0, 1, 0, 1], 2)
        4
        >>> solve([1, 0, 1, 0, 1], 3)
        2
        >>> solve([0, 0, 0, 0, 0], 0)
        15
    """
    # prefix_counts stores the frequency of each prefix sum encountered.
    # We initialize with {0: 1} to account for subarrays starting from index 0.
    prefix_counts: dict[int, int] = {0: 1}
    current_sum: int = 0
    total_subarrays: int = 0

    for num in nums:
        current_sum += num
        
        # If (current_sum - goal) exists in our map, it means there are 
        # 'prefix_counts[current_sum - goal]' subarrays ending at the current 
        # index that sum up to the goal.
        target_prefix = current_sum - goal
        if target_prefix in prefix_counts:
            total_subarrays += prefix_counts[target_prefix]
            
        # Update the frequency of the current prefix sum in the map.
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return total_subarrays
