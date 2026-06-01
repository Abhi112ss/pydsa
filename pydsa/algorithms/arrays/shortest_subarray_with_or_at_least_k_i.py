METADATA = {
    "id": 3095,
    "name": "Shortest Subarray With OR at Least K I",
    "slug": "shortest-subarray-with-or-at-least-k-i",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "bit_manipulation", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the shortest non-empty subarray such that the bitwise OR of its elements is at least k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the length of the shortest non-empty subarray such that the bitwise OR 
    of its elements is at least k.

    Args:
        nums: A list of integers.
        k: The target minimum bitwise OR value.

    Returns:
        The length of the shortest subarray, or -1 if no such subarray exists.

    Examples:
        >>> solve([1, 2, 3], 3)
        1
        >>> solve([1, 2, 3], 4)
        -1
    """
    n = len(nums)
    min_length = float('inf')
    
    # bit_counts stores the frequency of each bit (0-30) in the current window
    bit_counts = [0] * 31
    current_or = 0
    left = 0

    for right in range(n):
        # Add nums[right] to the window
        val_to_add = nums[right]
        for bit in range(31):
            if (val_to_add >> bit) & 1:
                if bit_counts[bit] == 0:
                    current_or |= (1 << bit)
                bit_counts[bit] += 1
        
        # Shrink the window from the left as long as the OR condition is met
        while current_or >= k and left <= right:
            min_length = min(min_length, right - left + 1)
            
            val_to_remove = nums[left]
            for bit in range(31):
                if (val_to_remove >> bit) & 1:
                    bit_counts[bit] -= 1
                    # If no more numbers in window have this bit set, update current_or
                    if bit_counts[bit] == 0:
                        current_or &= ~(1 << bit)
            left += 1

    return int(min_length) if min_length != float('inf') else -1
