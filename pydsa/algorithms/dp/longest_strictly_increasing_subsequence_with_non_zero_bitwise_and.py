METADATA = {
    "id": 3825,
    "name": "Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND",
    "slug": "longest_strictly_increasing_subsequence_with_non_zero_bitwise_and",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bitwise"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(log(max_val))",
    "description": "Find the length of the longest strictly increasing subsequence where the bitwise AND of all elements is non-zero.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest strictly increasing subsequence where 
    the bitwise AND of all elements in the subsequence is non-zero.

    The condition that the bitwise AND of a set of numbers is non-zero means 
    there must exist at least one bit position 'i' that is set (1) in every 
    number in that subsequence.

    Args:
        nums: A list of positive integers.

    Returns:
        The length of the longest such subsequence.

    Examples:
        >>> solve([1, 2, 4, 8])
        1
        >>> solve([3, 5, 10, 12, 15])
        3
        >>> solve([1, 2, 3, 4, 5])
        2
    """
    if not nums:
        return 0

    # max_bits is determined by the maximum value in nums. 
    # Since nums[i] can be up to 10^9, 31 bits is sufficient.
    max_val = max(nums)
    max_bits = max_val.bit_length()
    
    # dp[i] stores the length of the longest strictly increasing subsequence 
    # where every element in the subsequence has the i-th bit set.
    # Because we want the subsequence to be strictly increasing, we process 
    # elements in the order they appear in the input.
    # However, the problem asks for a subsequence that is strictly increasing.
    # If we pick a set of numbers that all share bit 'i', and we pick them 
    # in their original relative order, they form a subsequence. 
    # To ensure it is strictly increasing, we must ensure that for any 
    # chosen elements a and b where index(a) < index(b), a < b.
    
    # Wait, the standard "Longest Increasing Subsequence" (LIS) usually 
    # implies we pick elements such that their indices are increasing 
    # AND their values are increasing.
    # If the condition is "bitwise AND is non-zero", all elements must share 
    # a bit. If they all share bit 'i', and we want them to be strictly 
    # increasing, we are looking for the LIS of the subset of numbers 
    # that have bit 'i' set.
    
    # However, the problem can be simplified: if we fix a bit 'i', 
    # any subsequence where all elements have bit 'i' set will have a 
    # non-zero bitwise AND. To maximize the length of such a subsequence 
    # while maintaining the "strictly increasing" property, we simply 
    # need to find the LIS of the elements that have bit 'i' set.
    
    # But there's a catch: the problem asks for the longest subsequence 
    # that is BOTH strictly increasing AND has non-zero AND.
    # If we pick a bit 'i', and we only consider numbers with bit 'i' set, 
    # any subsequence we pick from these numbers will satisfy the AND condition.
    # To satisfy the "strictly increasing" condition, we just need to 
    # find the LIS of the elements that have bit 'i' set.
    
    # Let's refine: For each bit position 'b' from 0 to 30:
    # 1. Filter nums to get only those where (num & (1 << b)) != 0.
    # 2. Find the LIS of this filtered list.
    # 3. The answer is the maximum LIS found across all bits.

    def get_lis_length(arr: list[int]) -> int:
        """Standard O(n log n) LIS algorithm."""
        if not arr:
            return 0
        tails = []
        for x in arr:
            # Binary search for the smallest tail >= x
            import bisect
            idx = bisect.bisect_left(tails, x)
            if idx < len(tails):
                tails[idx] = x
            else:
                tails.append(x)
        return len(tails)

    max_len = 0
    
    # Iterate through each possible bit position
    for bit in range(max_bits):
        # Extract elements that have the current bit set
        # We must maintain their original relative order to form a subsequence
        filtered_nums = [x for x in nums if (x & (1 << bit))]
        
        if not filtered_nums:
            continue
            
        # Calculate LIS for this specific bit group
        current_lis = get_lis_length(filtered_nums)
        if current_lis > max_len:
            max_len = current_lis
            
    return max_len
