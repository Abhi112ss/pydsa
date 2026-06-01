METADATA = {
    "id": 2450,
    "name": "Number of Distinct Binary Strings After Applying Operations",
    "slug": "number-of-distinct-binary-strings-after-applying-operations",
    "category": "math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of distinct binary strings possible after applying the given operations to a string of length n.",
}

def solve(n: int, operations: int) -> int:
    """
    Args:
        n: The length of the binary string.
        operations: The number of operations to perform.

    Returns:
        The number of distinct binary strings modulo 10^9 + 7.
    """
    MODULO = 1_000_000_007
    
    total_operations = n + operations
    
    def combinations(n_val: int, k_val: int) -> int:
        if k_val < 0 or k_val > n_val:
            return 0
        if k_val == 0 or k_val == n_val:
            return 1
        if k_val > n_val // 2:
            k_val = n_val - k_val
            
        numerator = 1
        denominator = 1
        for i in range(k_val):
            numerator = (numerator * (n_val - i)) % MODULO
            denominator = (denominator * (i + 1)) % MODULO
            
        return (numerator * pow(denominator, MODULO - 2, MODULO)) % MODULO

    return combinations(total_operations, n)