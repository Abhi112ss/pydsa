METADATA = {
    "id": 3470,
    "name": "Permutations IV",
    "slug": "permutations_iv",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["backtracking", "dynamic_programming", "bitmask"],
    "difficulty": "hard",
    "time_complexity": "O(2^n * n^2)",
    "space_complexity": "O(2^n * n)",
    "description": "Count the number of valid permutations of a given array based on specific constraints using bitmask DP.",
}

def solve(nums: list[int], constraints: list[list[int]]) -> int:
    """
    Counts the number of valid permutations of nums that satisfy all constraints.
    A constraint [i, j] means that in the permutation, the element at index i 
    must appear before the element at index j.

    Args:
        nums: A list of integers representing the elements to permute.
        constraints: A list of pairs [i, j] where index i must appear before index j.

    Returns:
        The total number of valid permutations.

    Examples:
        >>> solve([1, 2, 3], [[0, 1]])
        4
        >>> solve([1, 2], [[1, 0]])
        1
    """
    n = len(nums)
    MOD = 10**9 + 7

    # Pre-process constraints into a bitmask for each element.
    # must_precede[j] will contain a bitmask where the i-th bit is set 
    # if index i must appear before index j.
    must_precede = [0] * n
    for u, v in constraints:
        must_precede[v] |= (1 << u)

    # dp[mask] stores the number of valid ways to arrange the elements 
    # represented by the set bits in 'mask'.
    dp = [0] * (1 << n)
    dp[0] = 1

    # Iterate through all possible subsets (masks)
    for mask in range(1 << n):
        if dp[mask] == 0:
            continue
        
        # Try adding an element 'next_idx' to the current subset 'mask'
        for next_idx in range(n):
            # Check if next_idx is not already in the mask
            if not (mask & (1 << next_idx)):
                # Check if all required predecessors for next_idx are already in the mask
                if (mask & must_precede[next_idx]) == must_precede[next_idx]:
                    new_mask = mask | (1 << next_idx)
                    dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD

    return dp[(1 << n) - 1]
