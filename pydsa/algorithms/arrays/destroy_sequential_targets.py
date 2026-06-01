METADATA = {
    "id": 2453,
    "name": "Destroy Sequential Targets",
    "slug": "destroy_sequential_targets",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["hash_map", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of targets that can be destroyed in a sequence where each subsequent target is exactly 'value' greater than the previous.",
}

def solve(nums: list[int], value: int) -> int:
    """
    Calculates the maximum number of targets that can be destroyed in a sequence.
    
    A sequence is valid if each element is exactly 'value' greater than the 
    previous element in the sequence. Since we can only destroy targets in 
    increasing order of their indices, we track the length of the sequence 
    ending at each number.

    Args:
        nums: A list of integers representing the targets.
        value: The required difference between consecutive targets in a sequence.

    Returns:
        The maximum number of targets that can be destroyed.

    Examples:
        >>> solve([4, 2, 1, 7, 5], 2)
        2
        >>> solve([1, 2, 3, 4, 5], 1)
        5
        >>> solve([1, 5, 2, 3, 4], 1)
        4
    """
    # dp stores the length of the longest valid sequence ending with the key
    dp: dict[int, int] = {}
    max_destroyed = 0

    for target in nums:
        # Check if there is a preceding element in the sequence (target - value)
        # If it exists, the current sequence length is dp[target - value] + 1
        # Otherwise, the sequence starts here with length 1
        previous_element = target - value
        current_length = dp.get(previous_element, 0) + 1
        
        # Update the dp table for the current target
        dp[target] = current_length
        
        # Keep track of the global maximum sequence length found so far
        if current_length > max_destroyed:
            max_destroyed = current_length

    return max_destroyed
