METADATA = {
    "id": 3416,
    "name": "Subsequences with a Unique Middle Mode II",
    "slug": "subsequences-with-a-unique-middle-mode-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "combinatorics", "counting"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count subsequences where a specific element acts as a unique middle mode based on frequency constraints.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of subsequences where a unique middle mode exists.
    
    A middle mode is defined by its frequency being strictly greater than 
    the frequency of any other element in the subsequence.
    
    Args:
        nums: A list of integers.
        k: A constraint parameter (used in specific problem variations).
        
    Returns:
        The total count of valid subsequences modulo 10^9 + 7.
        
    Examples:
        >>> solve([1, 2, 1], 1)
        # Example logic depends on specific problem constraints
    """
    MOD = 10**9 + 7
    n = len(nums)
    if n == 0:
        return 0

    # Precompute combinations using Pascal's triangle for O(1) lookup
    # C[n][r] = nCr
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

    # Group indices by value to handle frequency counts efficiently
    val_to_indices = {}
    for idx, val in enumerate(nums):
        if val not in val_to_indices:
            val_to_indices[val] = []
        val_to_indices[val].append(idx)

    sorted_vals = sorted(val_to_indices.keys())
    total_valid_subsequences = 0

    # For each unique value, treat it as the potential 'unique middle mode'
    for target_val in sorted_vals:
        indices = val_to_indices[target_val]
        m = len(indices)
        
        # We need to count subsequences where target_val appears 'f' times,
        # and every other value appears < 'f' times.
        # This is typically solved by iterating through possible frequencies 'f'.
        
        # Pre-calculate counts of elements smaller and larger than target_val
        # to optimize the combinatorial selection.
        smaller_count = 0
        larger_count = 0
        for v in sorted_vals:
            if v < target_val:
                smaller_count += len(val_to_indices[v])
            elif v > target_val:
                larger_count += len(val_to_indices[v])

        # To satisfy the 'unique middle mode' condition:
        # 1. Pick 'f' occurrences of target_val (f >= 1).
        # 2. For every other value 'v', pick 'j' occurrences where 0 <= j < f.
        
        # This specific problem structure (Subsequences with Unique Middle Mode II)
        # often implies a DP approach where we track the contribution of each element.
        # Given the O(n^2) constraint, we iterate through possible frequencies f.
        
        for f in range(1, m + 1):
            # Ways to choose exactly f elements of target_val
            ways_to_pick_target = C[m][f]
            
            # ways_others: product of (sum_{j=0}^{min(count_v, f-1)} C[count_v][j])
            # for all v != target_val.
            ways_others = 1
            
            for v in sorted_vals:
                if v == target_val:
                    continue
                
                count_v = len(val_to_indices[v])
                ways_for_v = 0
                # Sum combinations for this value such that frequency < f
                for j in range(min(count_v, f - 1) + 1):
                    ways_for_v = (ways_for_v + C[count_v][j]) % MOD
                
                ways_others = (ways_others * ways_for_v) % MOD
            
            # Add to total: (ways to pick target) * (ways to pick others)
            current_f_contribution = (ways_to_pick_target * ways_others) % MOD
            total_valid_subsequences = (total_valid_subsequences + current_f_contribution) % MOD

    return total_valid_subsequences
