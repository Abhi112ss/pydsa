METADATA = {
    "id": 2411,
    "name": "Smallest Subarrays With Maximum Bitwise OR",
    "slug": "smallest-subarrays-with-maximum-bitwise-or",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["sliding_window", "bit_manipulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the smallest subarray starting at each index that achieves the maximum possible bitwise OR for any subarray starting at that index.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Calculates the length of the smallest subarray starting at each index 
    that achieves the maximum possible bitwise OR.

    The maximum possible OR for a subarray starting at index i is the OR 
    of all elements from index i to the end of the array. To find the 
    smallest subarray, we track the nearest occurrence of each bit (0-30).

    Args:
        nums: A list of integers.

    Returns:
        A list of integers representing the lengths of the smallest subarrays.

    Examples:
        >>> solve([1, 0, 2, 1, 3])
        [3, 3, 1, 1, 1]
        >>> solve([1, 1, 1])
        [1, 1, 1]
    """
    n = len(nums)
    result = [0] * n
    # last_seen_bit_pos[i] stores the nearest index >= current index 
    # where the i-th bit is set to 1.
    last_seen_bit_pos = [-1] * 31

    # Iterate backwards to maintain the 'nearest' future position for each bit
    for i in range(n - 1, -1, -1):
        current_val = nums[i]
        
        # Update the last seen position for every bit set in the current number
        for bit in range(31):
            if (current_val >> bit) & 1:
                last_seen_bit_pos[bit] = i
        
        # The maximum OR is achieved by including the nearest index 
        # for every bit that appears anywhere from index i to n-1.
        # The smallest subarray length is determined by the furthest 
        # 'nearest' bit position.
        furthest_bit_index = i
        for bit in range(31):
            if last_seen_bit_pos[bit] != -1:
                if last_seen_bit_pos[bit] > furthest_bit_index:
                    furthest_bit_index = last_seen_bit_pos[bit]
        
        result[i] = (furthest_bit_index - i) + 1

    return result
