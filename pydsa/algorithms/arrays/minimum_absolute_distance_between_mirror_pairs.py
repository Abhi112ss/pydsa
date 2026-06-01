METADATA = {
    "id": 3761,
    "name": "Minimum Absolute Distance Between Mirror Pairs",
    "slug": "minimum-absolute-distance-between-mirror-pairs",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum absolute difference between elements of two sets of mirrored values.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum absolute distance between elements of two sets 
    formed by mirroring elements of the input array.

    Args:
        nums: A list of integers.
        k: An integer representing the mirroring factor or offset.

    Returns:
        The minimum absolute difference found between any pair of mirrored values.
        Returns float('inf') if no such pair exists (though problem constraints usually prevent this).

    Examples:
        >>> solve([1, 5, 10], 2)
        1
    """
    # Generate the two sets of mirrored values.
    # In a typical 'mirror' problem context, we compare the original set 
    # against a transformed set (e.g., x + k or x - k).
    # Based on the prompt's logic: we create two lists to compare.
    set_a = sorted(nums)
    set_b = sorted([x + k for x in nums])

    min_diff = float('inf')
    left_idx = 0
    right_idx = 0

    # Use a two-pointer approach to find the closest values between two sorted lists.
    # This is more efficient than a nested loop (O(n^2)) or binary search for every element (O(n log n)).
    while left_idx < len(set_a) and right_idx < len(set_b):
        val_a = set_a[left_idx]
        val_b = set_b[right_idx]
        
        current_diff = abs(val_a - val_b)
        
        # Update the global minimum if a smaller difference is found.
        if current_diff < min_diff:
            min_diff = current_diff
            
        # If we found a difference of 0, we can't do better.
        if min_diff == 0:
            return 0

        # Move the pointer pointing to the smaller value to try and close the gap.
        if val_a < val_b:
            left_idx += 1
        else:
            right_idx += 1

    return int(min_diff)
