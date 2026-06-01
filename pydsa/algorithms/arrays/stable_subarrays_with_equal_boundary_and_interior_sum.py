METADATA = {
    "id": 3728,
    "name": "Stable Subarrays With Equal Boundary and Interior Sum",
    "slug": "stable_subarrays_with_equal_boundary_and_interior_sum",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of subarrays where the sum of the interior elements equals the sum of the boundary elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of subarrays where the sum of the interior elements 
    equals the sum of the boundary elements.

    The condition for a subarray [i, j] (where j - i >= 2) is:
    sum(nums[i+1 : j]) == nums[i] + nums[j]
    
    Let P[k] be the prefix sum up to index k (inclusive).
    The sum of interior elements is: P[j-1] - P[i]
    The condition becomes: P[j-1] - P[i] = nums[i] + nums[j]
    Rearranging terms:
    P[j-1] - nums[j] = P[i] + nums[i]

    Args:
        nums: A list of integers.

    Returns:
        The total count of stable subarrays.

    Examples:
        >>> solve([1, 2, 1])
        1
        >>> solve([1, 1, 1, 1])
        2
    """
    n = len(nums)
    if n < 3:
        return 0

    # prefix_sums[k] = sum(nums[0...k-1])
    # We use a running prefix sum to avoid O(n) space for the whole array if preferred,
    # but for clarity we'll track the current prefix sum.
    
    count = 0
    current_prefix_sum = 0
    
    # We need to store the frequency of (P[i] + nums[i]) seen so far.
    # The index i must be at least 2 positions behind j to ensure an interior exists.
    # When we are at index j, the valid i's are 0 to j-2.
    # The condition is: P[j-1] - nums[j] == P[i] + nums[i]
    
    # hash_map stores: { (prefix_sum_up_to_i + nums[i]): frequency }
    target_map: dict[int, int] = {}
    
    # To handle the j-2 constraint, we use a pointer or a delayed update.
    # As we iterate j from 2 to n-1:
    # 1. Add the value (P[i] + nums[i]) for i = j-2 to the map.
    # 2. Check how many times (P[j-1] - nums[j]) exists in the map.
    
    # Pre-calculate prefix sums or maintain them on the fly.
    # Let's maintain prefix_sum[k] = sum(nums[0...k-1])
    # P[i] = sum(nums[0...i-1])
    # P[j-1] = sum(nums[0...j-2])
    
    # Let's redefine prefix sum for easier indexing:
    # Let S[k] be the sum of nums[0...k]
    # Interior sum (i+1 to j-1) = S[j-1] - S[i]
    # Condition: S[j-1] - S[i] = nums[i] + nums[j]
    # Rearrange: S[j-1] - nums[j] = S[i] + nums[i]
    
    prefix_sum = 0
    # We'll store S[i] + nums[i] in the map.
    # We need to iterate j from 2 to n-1.
    # When j=2, i can only be 0.
    # When j=3, i can be 0, 1.
    
    # To implement this, we'll keep track of S[i] as we go.
    # S_vals[i] will store the prefix sum up to index i.
    S = [0] * n
    current_s = 0
    for k in range(n):
        current_s += nums[k]
        S[k] = current_s

    for j in range(2, n):
        # The new valid i available for this j is i = j - 2
        i_new = j - 2
        val_to_store = S[i_new] + nums[i_new]
        target_map[val_to_store] = target_map.get(val_to_store, 0) + 1
        
        # Check the condition: S[j-1] - nums[j] == S[i] + nums[i]
        # Note: S[j-1] is the sum up to index j-1.
        # The interior sum is nums[i+1] + ... + nums[j-1].
        # This is S[j-1] - S[i].
        # So: S[j-1] - S[i] = nums[i] + nums[j]
        # => S[j-1] - nums[j] = S[i] + nums[i]
        
        target_val = S[j-1] - nums[j]
        if target_val in target_map:
            count += target_map[target_val]
            
    return count
