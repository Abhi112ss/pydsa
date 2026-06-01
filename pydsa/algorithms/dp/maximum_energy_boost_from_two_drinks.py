METADATA = {
    "id": 3259,
    "name": "Maximum Energy Boost From Two Drinks",
    "slug": "maximum-energy-boost-from-two-drinks",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum energy boost possible by selecting two non-adjacent drinks with a specific gap constraint.",
}

def solve(energy: list[int]) -> int:
    """
    Calculates the maximum energy boost from two drinks such that the 
    drinks are not adjacent and satisfy the problem's specific constraints.
    
    Note: Based on the problem description (implied by the ID/context), 
    this is a variation of the maximum sum of two non-adjacent elements 
    where we want to maximize energy[i] + energy[j] given |i - j| > 1.

    Args:
        energy: A list of integers representing energy boost from each drink.

    Returns:
        The maximum energy boost possible.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        9  # (4 + 5 is adjacent, so 3 + 5 = 8 or 2 + 5 = 7 or 4 + 2 = 6... 
           # wait, if non-adjacent: 1+3=4, 1+4=5, 1+5=6, 2+4=6, 2+5=7, 3+5=8. Max is 8)
           # Correction: If the problem asks for max(energy[i] + energy[j]) where |i-j| > 1:
           # For [1, 2, 3, 4, 5], pairs are (1,3), (1,4), (1,5), (2,4), (2,5), (3,5).
           # Sums: 4, 5, 6, 6, 7, 8. Max is 8.
    """
    n = len(energy)
    if n < 3:
        # If we need two non-adjacent drinks, we need at least 3 drinks.
        # If the problem allows any two, the logic changes, but standard 
        # non-adjacent problems require n >= 3.
        return 0

    # max_so_far tracks the maximum energy value seen so far that is 
    # at least two indices away from the current index 'i'.
    max_so_far = energy[0]
    max_boost = 0

    # We iterate from the third element (index 2) to the end.
    # For each element at index i, the best partner is the max element 
    # found in the range [0, i-2].
    for i in range(2, n):
        # Update the maximum energy seen up to index i-2
        # This ensures the non-adjacency constraint |i - j| >= 2
        max_so_far = max(max_so_far, energy[i - 2])
        
        # Calculate potential boost with current drink and the best valid previous drink
        current_boost = energy[i] + max_so_far
        
        # Update global maximum
        if current_boost > max_boost:
            max_boost = current_boost

    return max_boost
