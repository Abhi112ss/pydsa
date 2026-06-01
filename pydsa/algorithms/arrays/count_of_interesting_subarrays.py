METADATA = {
    "id": 2845,
    "name": "Count of Interesting Subarrays",
    "slug": "count_of_interesting_subarrays",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["prefix_xor", "hash_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subarrays where the XOR sum of elements is equal to k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of subarrays whose XOR sum equals k.

    The problem asks for subarrays where the XOR sum of elements is k.
    Using the property of XOR: if prefix_xor[i] ^ prefix_xor[j] = k,
    then prefix_xor[i] ^ k = prefix_xor[j]. We can use a hash map to 
    track the frequency of prefix XOR values encountered so far.

    Args:
        nums: A list of integers.
        k: The target XOR sum.

    Returns:
        The total count of interesting subarrays.

    Examples:
        >>> solve([1, 1, 2], 0)
        1
        >>> solve([1, 2, 3], 0)
        1
    """
    # count_map stores the frequency of prefix XOR values seen so far.
    # We initialize with {0: 1} to account for subarrays starting from index 0.
    count_map: dict[int, int] = {0: 1}
    current_prefix_xor = 0
    total_interesting_subarrays = 0

    for num in nums:
        # Update the running prefix XOR
        current_prefix_xor ^= num
        
        # We want to find a previous prefix_xor such that:
        # current_prefix_xor ^ previous_prefix_xor == k
        # This is algebraically equivalent to:
        # previous_prefix_xor = current_prefix_xor ^ k
        target_prefix_xor = current_prefix_xor ^ k
        
        # If the target exists in our map, it means there are 'n' 
        # subarrays ending at the current index that satisfy the condition.
        if target_prefix_xor in count_map:
            total_interesting_subarrays += count_map[target_prefix_xor]
            
        # Update the map with the current prefix XOR
        count_map[current_prefix_xor] = count_map.get(current_prefix_xor, 0) + 1

    return total_interesting_subarrays
