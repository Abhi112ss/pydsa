METADATA = {
    "id": 3179,
    "name": "Find the N-th Value After K Seconds",
    "slug": "find-the-n-th-value-after-k-seconds",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["math", "dp"],
    "difficulty": "medium",
    "time_complexity": "O(k)",
    "space_complexity": "O(k)",
    "description": "Find the n-th value in a sequence where each second the sequence doubles and each element is incremented by its index.",
}

def solve(n: int, k: int) -> int:
    """
    Args:
        n: The index of the value to find (1-indexed).
        k: The number of seconds elapsed.

    Returns:
        The n-th value after k seconds modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    
    if k == 0:
        return 1
    
    current_sequence = [1] * n
    
    for second in range(1, k + 1):
        next_sequence = [0] * n
        for index in range(n):
            next_sequence[index] = (current_sequence[index] * 2 + (index + 1)) % MODULUS
        current_sequence = next_sequence
        
    return current_sequence[n - 1]