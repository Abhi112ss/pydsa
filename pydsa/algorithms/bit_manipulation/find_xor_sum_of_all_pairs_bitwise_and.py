METADATA = {
    "id": 1835,
    "name": "Find XOR Sum of All Pairs Bitwise AND",
    "slug": "find_xor_sum_of_all_pairs_bitwise_and",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(1)",
    "description": "Calculate the XOR sum of the bitwise AND of all possible pairs in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the XOR sum of (nums[i] & nums[j]) for all 0 <= i < j < n.

    The problem asks for the XOR sum of all pairs (i, j) where i < j. 
    A bit at position 'k' will be present in the final XOR sum if and only if 
    the number of pairs (i, j) such that (nums[i] & nums[j]) has the k-th bit set 
    is odd.
    
    The k-th bit of (nums[i] & nums[j]) is 1 if and only if both nums[i] and 
    nums[j] have the k-th bit set. If there are 'count' numbers in the array 
    with the k-th bit set, the number of pairs (i, j) with i < j that both 
    have the k-th bit set is given by the combination formula: count * (count - 1) // 2.

    Args:
        nums: A list of integers.

    Returns:
        The XOR sum of the bitwise AND of all pairs.

    Examples:
        >>> solve([1, 2, 3])
        # Pairs: (1&2)=0, (1&3)=1, (2&3)=2. XOR sum: 0 ^ 1 ^ 2 = 3
        3
        >>> solve([1, 1, 1])
        # Pairs: (1&1)=1, (1&1)=1, (1&1)=1. XOR sum: 1 ^ 1 ^ 1 = 1
        1
    """
    if not nums:
        return 0

    xor_sum = 0
    # Find the maximum value to determine how many bits we need to check
    max_val = max(nums)
    if max_val == 0:
        return 0
        
    # Determine the number of bits required (up to 31 for standard positive integers)
    max_bits = max_val.bit_length()

    # Iterate through each bit position independently
    for bit in range(max_bits):
        count_with_bit_set = 0
        for num in nums:
            # Check if the current bit is set in the number
            if (num >> bit) & 1:
                count_with_bit_set += 1
        
        # The number of pairs (i, j) with i < j where both have this bit set
        # is the combination C(count, 2) = count * (count - 1) / 2
        num_pairs_with_bit_set = (count_with_bit_set * (count_with_bit_set - 1)) // 2
        
        # If the number of such pairs is odd, this bit will contribute to the XOR sum
        if num_pairs_with_bit_set % 2 == 1:
            xor_sum |= (1 << bit)

    return xor_sum
