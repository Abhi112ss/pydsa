METADATA = {
    "id": 2760,
    "name": "Longest Even Odd Subarray With Threshold",
    "slug": "longest-even-odd-subarray-with-threshold",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subarray where elements alternate between even and odd and every element is less than or equal to a given threshold.",
}

def solve(nums: list[int], threshold: int) -> int:
    """
    Finds the length of the longest subarray where elements alternate parity 
    and all elements are within the threshold.

    Args:
        nums: A list of integers.
        threshold: An integer threshold that all elements in the subarray must not exceed.

    Returns:
        The length of the longest valid subarray.

    Examples:
        >>> solve([3, 2, 5, 4], 5)
        4
        >>> solve([2, 3, 4, 5, 6], 3)
        2
        >>> solve([1, 2, 3, 4, 5], 1)
        1
    """
    max_length = 0
    current_length = 0
    
    for i in range(len(nums)):
        # Check if the current element satisfies the threshold condition
        if nums[i] <= threshold:
            # If it's the first element of a potential subarray
            if current_length == 0:
                current_length = 1
            else:
                # Check if the current element has different parity than the previous one
                # (even + odd) % 2 is always 1, (even + even) % 2 is 0, (odd + odd) % 2 is 0
                if (nums[i] % 2) != (nums[i - 1] % 2):
                    current_length += 1
                else:
                    # Parity pattern broken, reset to 1 (the current element itself)
                    current_length = 1
        else:
            # Threshold violated, reset current sequence
            current_length = 0
            
        # Update the global maximum length found so far
        if current_length > max_length:
            max_length = current_length
            
    return max_length
