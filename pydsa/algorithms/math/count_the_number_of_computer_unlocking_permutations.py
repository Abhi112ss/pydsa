METADATA = {
    "id": 3577,
    "name": "Count the Number of Computer Unlocking Permutations",
    "slug": "count-computer-unlocking-permutations",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of valid permutations of computer unlocking sequences under specific constraints using combinatorics.",
}

def solve(n: int, k: int, mod: int = 10**9 + 7) -> int:
    """
    Calculates the number of valid unlocking permutations.
    
    The problem asks for the number of permutations of length n where each 
    element is chosen from a set of k available keys, subject to the 
    constraint that no two adjacent elements are the same.
    
    Args:
        n: The length of the permutation sequence.
        k: The number of available keys.
        mod: The modulus for the result.

    Returns:
        The total number of valid permutations modulo mod.

    Examples:
        >>> solve(3, 3)
        12
        # Explanation: (3 choices for 1st) * (2 choices for 2nd) * (2 choices for 3rd) = 3 * 2 * 2 = 12
        >>> solve(1, 5)
        5
    """
    if n == 0:
        return 0
    if n == 1:
        return k % mod
    
    # The first position can be any of the k keys.
    # For every subsequent position (from 2 to n), we must choose a key 
    # that is different from the one immediately preceding it.
    # This leaves (k - 1) choices for each of the remaining (n - 1) positions.
    
    # Result = k * (k - 1)^(n - 1)
    
    # We use modular exponentiation for efficiency and to handle large n.
    # pow(base, exp, mod) is O(log n)
    
    first_choice = k % mod
    remaining_choices = pow(k - 1, n - 1, mod)
    
    return (first_choice * remaining_choices) % mod
