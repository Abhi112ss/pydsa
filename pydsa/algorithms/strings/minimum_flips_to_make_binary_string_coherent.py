METADATA = {
    "id": 3922,
    "name": "Minimum Flips to Make Binary String Coherent",
    "slug": "minimum-flips-to-make-binary-string-coherent",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of flips required to make a binary string alternate between 0 and 1.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of flips to make a binary string coherent.
    A string is coherent if it follows an alternating pattern (0101... or 1010...).

    Args:
        s: A string consisting of '0's and '1's.

    Returns:
        The minimum number of flips required to achieve coherence.

    Examples:
        >>> solve("010")
        0
        >>> solve("111")
        1
        >>> solve("0000")
        2
    """
    flips_pattern_a = 0  # Pattern: 0, 1, 0, 1...
    flips_pattern_b = 0  # Pattern: 1, 0, 1, 0...

    for index, char in enumerate(s):
        # Determine expected character for Pattern A (starts with 0)
        # If index is even, expected is '0'. If index is odd, expected is '1'.
        expected_a = '0' if index % 2 == 0 else '1'
        
        if char != expected_a:
            flips_pattern_a += 1
        else:
            # If it matches Pattern A, it must mismatch Pattern B
            flips_pattern_b += 1
            
    # Note: The logic above is optimized. 
    # If char != expected_a, it contributes to pattern_a's cost.
    # If char == expected_a, it contributes to pattern_b's cost because 
    # pattern_b is the exact inverse of pattern_a.
    
    # However, to be more explicit and readable for production:
    # Let's re-calculate based on the two distinct patterns.
    
    cost_0101 = 0
    cost_1010 = 0
    
    for i in range(len(s)):
        # Pattern 0101...: even indices are '0', odd are '1'
        target_0101 = '0' if i % 2 == 0 else '1'
        if s[i] != target_0101:
            cost_0101 += 1
            
        # Pattern 1010...: even indices are '1', odd are '0'
        target_1010 = '1' if i % 2 == 0 else '0'
        if s[i] != target_1010:
            cost_1010 += 1
            
    return min(cost_0101, cost_1010)
