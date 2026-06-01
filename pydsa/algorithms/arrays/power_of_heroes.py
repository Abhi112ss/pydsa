METADATA = {
    "id": 2681,
    "name": "Power of Heroes",
    "slug": "power_of_heroes",
    "category": "Math",
    "aliases": [],
    "tags": ["sorting", "prefix_sum", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total power of heroes where each hero's power is the product of all strengths strictly less than theirs and the square of their own strength.",
}

def solve(strengths: list[int]) -> int:
    """
    Calculates the total power of all heroes based on the given rules.
    
    The power of a hero is defined as:
    (product of all strengths < current strength) * (current strength^2)
    
    The result should be returned modulo 10^9 + 7.

    Args:
        strengths: A list of integers representing the strength of each hero.

    Returns:
        The total power of all heroes modulo 10^9 + 7.

    Examples:
        >>> solve([2, 3, 5, 1, 4])
        110
        >>> solve([1, 1, 1])
        3
    """
    MOD = 1_000_000_007
    n = len(strengths)
    if n == 0:
        return 0

    # Sort strengths to process them in increasing order
    # This allows us to maintain a running product of all elements seen so far
    sorted_strengths = sorted(strengths)
    
    total_power = 0
    prefix_product = 1
    
    # We need to handle duplicate strengths carefully.
    # For a group of identical strengths, the 'product of all strengths strictly less'
    # is the same for all of them.
    i = 0
    while i < n:
        # Find the range of indices that have the same strength
        j = i
        while j < n and sorted_strengths[j] == sorted_strengths[i]:
            j += 1
        
        # current_strength is the value for the current group
        # count is how many heroes have this strength
        current_strength = sorted_strengths[i]
        count = j - i
        
        # The power contribution for ONE hero in this group:
        # (prefix_product) * (current_strength^2)
        # Since there are 'count' such heroes, we multiply by 'count'
        # We use modular arithmetic at each step to prevent overflow
        
        # term = (prefix_product * current_strength^2 * count) % MOD
        term = (prefix_product * pow(current_strength, 2, MOD)) % MOD
        term = (term * count) % MOD
        
        total_power = (total_power + term) % MOD
        
        # Update the prefix_product for the next group of strengths
        # The next group's 'strictly less' product will include all elements in this group
        # We multiply the current prefix_product by (current_strength ^ count)
        group_product = pow(current_strength, count, MOD)
        prefix_product = (prefix_product * group_product) % MOD
        
        # Move to the next distinct strength
        i = j
        
    return total_power
