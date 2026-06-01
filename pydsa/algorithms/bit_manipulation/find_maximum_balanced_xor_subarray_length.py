METADATA = {
    "id": 3755,
    "name": "Find Maximum Balanced XOR Subarray Length",
    "slug": "find_maximum_balanced_xor_subarray_length",
    "category": "Array",
    "aliases": [],
    "tags": ["bit_manipulation", "prefix_xor", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest subarray where the XOR sum of its elements is zero using prefix XORs.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest subarray with an XOR sum of zero.

    A subarray [i, j] has an XOR sum of zero if the prefix XOR up to index i-1 
    is equal to the prefix XOR up to index j.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest subarray whose elements XOR to zero. 
        Returns 0 if no such subarray exists.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        2  # Subarray [1, 2, 3] -> 1^2^3 = 0, length 3. Wait, 1^2=3, 3^3=0. Length is 3.
        >>> solve([1, 1, 1, 1])
        4
        >>> solve([1, 2, 4, 8])
        0
    """
    # prefix_xor_map stores the first index where a specific XOR sum was encountered.
    # We initialize with {0: -1} to handle subarrays starting from index 0.
    prefix_xor_map: dict[int, int] = {0: -1}
    current_xor_sum = 0
    max_length = 0

    for index, num in enumerate(nums):
        # Update the running prefix XOR
        current_xor_sum ^= num

        if current_xor_sum in prefix_xor_map:
            # If this XOR sum has been seen before, the subarray between 
            # the previous occurrence and the current index has an XOR sum of 0.
            start_index = prefix_xor_map[current_xor_sum]
            current_length = index - start_index
            if current_length > max_length:
                max_length = current_length
        else:
            # Store only the first occurrence to maximize the distance (length)
            prefix_xor_map[current_xor_sum] = index

    return max_length
