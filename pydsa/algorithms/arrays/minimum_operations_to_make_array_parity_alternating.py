METADATA = {
    "id": 3854,
    "name": "Minimum Operations to Make Array Parity Alternating",
    "slug": "minimum-operations-to-make-array-parity-alternating",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make an array's parity alternate between even and odd.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of elements to change to make the array parity alternate.

    The parity can alternate in two ways:
    1. [Even, Odd, Even, Odd, ...]
    2. [Odd, Even, Odd, Even, ...]

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 3, 4])
        0
        >>> solve([2, 4, 6, 8])
        2
        >>> solve([1, 1, 1, 1])
        2
    """
    n = len(nums)
    if n == 0:
        return 0

    # Case 1: Pattern starts with Even (index 0 is even, index 1 is odd, etc.)
    # Even indices should have nums[i] % 2 == 0
    # Odd indices should have nums[i] % 2 == 1
    mismatches_even_start = 0
    
    # Case 2: Pattern starts with Odd (index 0 is odd, index 1 is even, etc.)
    # Even indices should have nums[i] % 2 == 1
    # Odd indices should have nums[i] % 2 == 0
    mismatches_odd_start = 0

    for i in range(n):
        current_parity = nums[i] % 2
        
        # Determine expected parity for Case 1 (Even-start)
        # If i is even, expected is 0. If i is odd, expected is 1.
        # This is equivalent to (i % 2)
        expected_even_start = i % 2
        
        if current_parity != expected_even_start:
            mismatches_even_start += 1
        else:
            # If it matches Case 1, it must mismatch Case 2
            # because Case 2 is the exact inverse of Case 1
            mismatches_odd_start += 1
            
    # Note: The logic above is slightly optimized. 
    # If current_parity == expected_even_start, it's a match for Case 1.
    # If current_parity != expected_even_start, it's a match for Case 2.
    # However, to be strictly clear and avoid confusion:
    
    mismatches_even_start = 0
    mismatches_odd_start = 0
    
    for i in range(n):
        current_parity = nums[i] % 2
        # Pattern 1: 0, 1, 0, 1... (Even, Odd, Even, Odd)
        # Expected parity for index i is i % 2
        if current_parity != (i % 2):
            mismatches_even_start += 1
            
        # Pattern 2: 1, 0, 1, 0... (Odd, Even, Odd, Even)
        # Expected parity for index i is (i + 1) % 2
        if current_parity != ((i + 1) % 2):
            mismatches_odd_start += 1

    # Return the minimum of the two possible alternating patterns
    return min(mismatches_even_start, mismatches_odd_start)
