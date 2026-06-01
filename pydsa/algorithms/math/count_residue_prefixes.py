METADATA = {
    "id": 3803,
    "name": "Count Residue Prefixes",
    "slug": "count_residue_prefixes",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subsegments whose sum is divisible by k using prefix sum residues.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of subsegments in nums whose sum is divisible by k.

    A subsegment [i, j] has a sum divisible by k if (prefix_sum[j] - prefix_sum[i-1]) % k == 0,
    which is equivalent to prefix_sum[j] % k == prefix_sum[i-1] % k.

    Args:
        nums: A list of integers.
        k: The divisor.

    Returns:
        The total count of subsegments whose sum is a multiple of k.

    Examples:
        >>> solve([4, 5, 0, -2, -3, 1], 5)
        7
        >>> solve([1, 2, 3], 3)
        2
    """
    # residue_counts stores the frequency of each prefix sum modulo k encountered so far.
    # We initialize with {0: 1} to account for subsegments starting from index 0.
    residue_counts: dict[int, int] = {0: 1}
    
    current_prefix_sum: int = 0
    total_count: int = 0
    
    for num in nums:
        current_prefix_sum += num
        
        # Calculate the residue. In Python, % operator on negative numbers 
        # returns a result in [0, k-1], which is exactly what we need.
        residue = current_prefix_sum % k
        
        # If this residue has been seen before, every previous occurrence 
        # marks the start of a valid subsegment ending at the current index.
        if residue in residue_counts:
            total_count += residue_counts[residue]
            residue_counts[residue] += 1
        else:
            residue_counts[residue] = 1
            
    return total_count
