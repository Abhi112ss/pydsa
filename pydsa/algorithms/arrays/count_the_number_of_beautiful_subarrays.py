METADATA = {
    "id": 2588,
    "name": "Count the Number of Beautiful Subarrays",
    "slug": "count-the-number-of-beautiful-subarrays",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "bit_manipulation", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subarrays where the XOR sum of all elements is zero.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of subarrays whose XOR sum is equal to zero.

    A subarray has an XOR sum of zero if the prefix XOR at the start index 
    (minus one) is equal to the prefix XOR at the end index.

    Args:
        nums: A list of integers.

    Returns:
        The total count of beautiful subarrays.

    Examples:
        >>> solve([1, 1, 2, 1, 1])
        2
        >>> solve([0, 0, 0])
        6
    """
    # prefix_counts stores the frequency of each prefix XOR value encountered.
    # We initialize with {0: 1} because a prefix XOR of 0 itself represents 
    # a beautiful subarray starting from index 0.
    prefix_counts: dict[int, int] = {0: 1}
    
    current_xor_sum = 0
    total_beautiful_subarrays = 0
    
    for num in nums:
        # Update the running XOR sum (prefix XOR)
        current_xor_sum ^= num
        
        # If this current_xor_sum has been seen before, it means the XOR sum 
        # of the elements between the previous occurrence and now is zero.
        # The number of such subarrays is equal to the number of times 
        # we have seen this specific XOR sum before.
        if current_xor_sum in prefix_counts:
            total_beautiful_subarrays += prefix_counts[current_xor_sum]
            prefix_counts[current_xor_sum] += 1
        else:
            prefix_counts[current_xor_sum] = 1
            
    return total_beautiful_subarrays
