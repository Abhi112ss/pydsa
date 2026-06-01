METADATA = {
    "id": 60,
    "name": "Permutation Sequence",
    "slug": "permutation-sequence",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "recursion", "backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the k-th lexicographical permutation sequence of a set of n numbers.",
}

def solve(n: int, k: int) -> str:
    """
    Finds the k-th permutation sequence of n numbers using a mathematical approach.

    The algorithm uses the factorial number system (factoradic) to determine 
    each digit's position without generating all permutations.

    Args:
        n: The number of elements (1 to 9).
        k: The k-th permutation to find (1-indexed).

    Returns:
        The k-th permutation as a string.

    Examples:
        >>> solve(3, 3)
        '213'
        >>> solve(4, 9)
        '2314'
    """
    # Precompute factorials up to n
    factorials = [1] * (n + 1)
    for i in range(1, n + 1):
        factorials[i] = factorials[i - 1] * i

    # Create a list of available digits
    numbers = [str(i) for i in range(1, n + 1)]
    
    # Convert k to 0-indexed for easier calculation
    k -= 1
    
    result = []
    
    # We determine the digit for each position from left to right
    for i in range(n - 1, -1, -1):
        # The number of permutations possible for the remaining (i) positions
        # is i! (factorial of the remaining count).
        # The index of the digit in the current 'numbers' list is k // i!
        idx = k // factorials[i]
        
        # Append the selected digit to the result
        result.append(numbers.pop(idx))
        
        # Update k to the remainder to find the next digit in the sub-sequence
        k %= factorials[i]
        
    return "".join(result)
