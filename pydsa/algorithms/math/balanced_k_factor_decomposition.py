METADATA = {
    "id": 3669,
    "name": "Balanced K-Factor Decomposition",
    "slug": "balanced_k_factor_decomposition",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "recursion", "backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(log n)",
    "description": "Find if a number n can be decomposed into k factors such that the difference between the maximum and minimum factor is minimized.",
}

import math

def solve(n: int, k: int) -> int:
    """
    Finds the minimum possible difference between the maximum and minimum 
    factors in a k-factor decomposition of n.

    Args:
        n: The integer to decompose.
        k: The number of factors required.

    Returns:
        The minimum difference between the largest and smallest factor. 
        Returns -1 if no such decomposition exists.

    Examples:
        >>> solve(12, 2)
        1  # (3, 4) -> 4-3=1
        >>> solve(12, 3)
        1  # (2, 2, 3) -> 3-2=1
        >>> solve(7, 2)
        -1 # No decomposition into 2 factors > 1
    """
    if k == 1:
        return 0
    
    # Pre-calculate all divisors to speed up backtracking
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i*i != n:
                divisors.append(n // i)
    divisors.sort()

    # We only care about factors > 1 for a meaningful decomposition 
    # unless k is large and we must use 1s. 
    # However, standard k-factor problems usually imply factors > 1.
    # If the problem allows 1s, the logic changes. 
    # Assuming factors must be > 1 to avoid triviality.
    valid_divisors = [d for d in divisors if d > 1]
    
    min_diff = float('inf')

    def backtrack(remaining_n: int, remaining_k: int, min_f: int, max_f: int) -> None:
        nonlocal min_diff
        
        # Base case: all factors chosen
        if remaining_k == 0:
            if remaining_n == 1:
                min_diff = min(min_diff, max_f - min_f)
            return

        # Pruning: if current diff already exceeds best found
        if max_f - min_f >= min_diff:
            return

        # Optimization: if remaining_n is too small or too large for remaining_k
        # This is a loose bound; tighter bounds could use nth roots.
        
        # Iterate through possible next factors
        # To avoid permutations, we enforce non-decreasing order
        for d in valid_divisors:
            if d < min_f:
                continue
            if d > remaining_n:
                break
            
            # Check if d can actually be a factor
            if remaining_n % d == 0:
                # Update min/max for the next step
                new_min = min_f if min_f != -1 else d
                new_max = max(max_f, d)
                
                # Heuristic: if d^(remaining_k) > remaining_n, d is too large
                # if (remaining_n/d)^(remaining_k-1) < d, d is too small
                # But we use simple recursion for clarity
                backtrack(remaining_n // d, remaining_k - 1, new_min, new_max)

    # Start backtracking
    # We use -1 as a sentinel for uninitialized min/max
    backtrack(n, k, -1, -1)

    return int(min_diff) if min_diff != float('inf') else -1
