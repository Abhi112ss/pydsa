METADATA = {
    "id": 1995,
    "name": "Count Special Quadruplets",
    "slug": "count-special-quadruplets",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count the number of quadruplets (i, j, k, l) such that 0 <= i < j < k < l < n and nums[i] == nums[l] and nums[j] == nums[k] and nums[i] < nums[j].",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of special quadruplets (i, j, k, l) in the given list.
    
    A quadruplet is special if:
    0 <= i < j < k < l < n
    nums[i] == nums[l]
    nums[j] == nums[k]
    nums[i] < nums[j]

    Args:
        nums: A list of integers.

    Returns:
        The total count of special quadruplets.

    Examples:
        >>> solve([4, 1, 2, 1, 2])
        1
        >>> solve([1, 2, 3, 4, 5])
        0
    """
    n = len(nums)
    if n < 4:
        return 0

    # count_pairs[x][y] will store the number of pairs (j, k) 
    # such that j < k, nums[j] == y, nums[k] == x, and y > x.
    # However, the problem asks for nums[i] < nums[j] where nums[i]==nums[l] and nums[j]==nums[k].
    # Let's redefine: we want to find pairs (j, k) such that j < k and nums[j] == nums[k].
    # For a fixed i and l (where nums[i] == nums[l]), we need to count pairs (j, k)
    # such that i < j < k < l and nums[j] == nums[k] and nums[j] > nums[i].

    # To achieve O(n^2), we iterate through all possible pairs (j, k) and 
    # pre-calculate how many valid (i, l) pairs exist for them, or vice versa.
    
    # Let's use the approach: iterate through j and k as the middle elements.
    # For every pair (j, k) where j < k and nums[j] == nums[k], 
    # we need to know how many i < j and l > k exist such that nums[i] == nums[l] and nums[i] < nums[j].
    
    # A more efficient way:
    # Iterate through all possible values of 'a' (nums[i]) and 'b' (nums[j]).
    # But since values can be large, we use the indices.
    
    # Let's use the property: 
    # Total = sum over all (j, k) where j < k and nums[j] == nums[k]:
    #         (count of i < j where nums[i] < nums[j] and nums[i] == some_val) * 
    #         (count of l > k where nums[l] == some_val)
    # This is still tricky. Let's simplify.
    
    # Correct O(n^2) approach:
    # We iterate through all possible pairs (j, k) that could be the middle elements.
    # For a fixed j and k, if nums[j] == nums[k], we need to count pairs (i, l)
    # such that i < j, l > k, and nums[i] == nums[l] and nums[i] < nums[j].
    
    # Let's precompute:
    # left_count[val][index] = number of times 'val' appears in nums[0...index]
    # right_count[val][index] = number of times 'val' appears in nums[index...n-1]
    
    # Since we only care about nums[i] < nums[j], we can iterate through all 
    # possible values of nums[i].
    
    # Let's use a 2D array to store the count of pairs (i, l) such that 
    # nums[i] == nums[l] and nums[i] < some_value.
    # Actually, let's track the count of pairs (i, l) where nums[i] == nums[l] = v.
    # For a fixed j, k, we want to sum (count of i < j where nums[i] == v) * (count of l > k where nums[l] == v)
    # for all v < nums[j].
    
    # Let's use a frequency map for the 'i' elements and 'l' elements.
    # As we move j and k, we can't easily update.
    
    # Let's try this:
    # Iterate through all pairs (i, l) such that nums[i] == nums[l] and i < l.
    # For each such pair, we need to count (j, k) such that i < j < k < l and nums[j] == nums[k] and nums[j] > nums[i].
    
    # Let's use the "middle-out" approach:
    # Precompute `pair_counts[v]` which is the number of pairs (j, k) 
    # such that j < k and nums[j] == nums[k] == v.
    # This doesn't account for the i < j < k < l constraint.
    
    # Let's use the "middle-out" with a 2D structure:
    # For every pair (j, k) with j < k and nums[j] == nums[k], 
    # we want to know how many i < j and l > k satisfy nums[i] == nums[l] < nums[j].
    
    # Let's maintain a 2D array `count_map[v1][v2]`? No, values are up to 100.
    # The constraints say nums[i] is up to 100. This is key!
    
    # Let's use the fact that nums[i] <= 100.
    # Let `dp[v]` be the number of pairs (i, j) such that i < j and nums[i] == v and nums[j] > v.
    # This is not quite right.
    
    # Let's use:
    # For each pair (k, l) with k < l:
    #   If nums[k] == nums[l], we need to find how many (i, j) exist such that
    #   i < j < k and nums[i] == nums[l] and nums[j] > nums[i].
    # Wait, the condition is nums[i] == nums[l] and nums[j] == nums[k].
    # Let's re-read: nums[i] == nums[l] and nums[j] == nums[k] and nums[i] < nums[j].
    
    # Let's fix j and k. If nums[j] == nums[k], we need to count (i, l) 
    # such that i < j, l > k, and nums[i] == nums[l] and nums[i] < nums[j].
    
    # Let `ways[v]` be the number of pairs (i, j) such that i < j, nums[i] == v, and nums[j] > v.
    # This is still not quite right because of the l > k constraint.
    
    # Let's use:
    # For each possible value `v` (from 1 to 100):
    #   Count how many pairs (i, l) exist such that nums[i] == v and nums[l] == v and i < l.
    #   But we need the middle elements (j, k) to be between them.
    
    # Let's use the O(n^2) approach:
    # Iterate through all j from 0 to n-1.
    # For a fixed j, we want to find all k > j such that nums[k] == nums[j].
    # For each such (j, k), we need to count (i, l) such that i < j, l > k, and nums[i] == nums[l] < nums[j].
    
    # Let's precompute `prefix_count[v][idx]` = count of value `v` in `nums[0...idx]`.
    # Let's precompute `suffix_count[v][idx]` = count of value `v` in `nums[idx...n-1]`.
    
    max_val = 101
    prefix_count = [[0] * (n + 1) for _ in range(max_val)]
    for v in range(max_val):
        for idx in range(n):
            prefix_count[v][idx + 1] = prefix_count[v][idx] + (1 if nums[idx] == v else 0)
            
    suffix_count = [[0] * (n + 1) for _ in range(max_val)]
    for v in range(max_val):
        for idx in range(n - 1, -1, -1):
            suffix_count[v][idx] = suffix_count[v][idx + 1] + (1 if nums[idx] == v else 0)

    total_quadruplets = 0
    
    # We iterate through all possible pairs (j, k) that could be the middle elements.
    # j is the second element, k is the third.
    # Condition: j < k and nums[j] == nums[k].
    # We also need nums[i] == nums[l] < nums[j] where i < j and l > k.
    
    # To optimize, for a fixed j and k, we need:
    # sum_{v < nums[j]} (count of v in nums[0...j-1]) * (count of v in nums[k+1...n-1])
    
    # We can precompute this sum for all j, k.
    # But we only care about j, k where nums[j] == nums[k].
    
    # Let's optimize the inner loop.
    # For a fixed j, as k increases, the suffix_count changes.
    # However, we can iterate j from 0 to n-1, and for each j, 
    # iterate k from j+1 to n-1.
    
    for j in range(n):
        # Pre-calculate the sum for all v < nums[j] for the current j
        # This sum depends on k.
        # sum_v_less_than_j[k] = sum_{v < nums[j]} (prefix_count[v][j] * suffix_count[v][k+1])
        
        # Since we only care about k where nums[k] == nums[j], 
        # we can just compute the sum on the fly.
        
        target_val = nums[j]
        
        # Optimization: if target_val is 0, no v < target_val exists.
        if target_val == 0:
            continue
            
        # Pre-calculate prefix_count[v][j] for all v < target_val
        # to avoid repeated lookups in the k loop.
        relevant_prefixes = []
        for v in range(target_val):
            count = prefix_count[v][j]
            if count > 0:
                relevant_prefixes.append((v, count))
        
        if not relevant_prefixes:
            continue

        for k in range(j + 1, n):
            if nums[k] == target_val:
                # Found a valid (j, k) pair. Now count valid (i, l) pairs.
                # We need i < j and l > k such that nums[i] == nums[l] = v < target_val.
                current_sum = 0
                for v, p_count in relevant_prefixes:
                    s_count = suffix_count[v][k + 1]
                    current_sum += p_count * s_count
                total_quadruplets += current_sum

    return total_quadruplets
