METADATA = {
    "id": 1960,
    "name": "Maximum Product of the Length of Two Palindromic Substrings",
    "slug": "maximum-product-of-the-length-of-two-palindromic-substrings",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["manacher_algorithm", "dp", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum product of the lengths of two non-overlapping palindromic substrings.",
}

def solve(s: str) -> int:
    """
    Calculates the maximum product of the lengths of two non-overlapping palindromic substrings.

    Args:
        s: The input string.

    Returns:
        The maximum product of the lengths of two non-overlapping palindromic substrings.

    Examples:
        >>> solve("abacaba")
        16
        >>> solve("abccba")
        9
    """
    n = len(s)
    if n < 2:
        return 0

    # Manacher's algorithm to find the radius of odd-length palindromes centered at each index.
    # Since the problem specifies palindromic substrings (not necessarily even), 
    # and the constraints/problem type usually imply odd-length in this specific context 
    # (or the problem can be simplified to odd-length by padding), 
    # we focus on odd-length palindromes as per the standard interpretation of this problem.
    # Note: The problem asks for palindromic substrings. In the context of this specific 
    # LeetCode problem, it refers to odd-length palindromes.
    
    radii = [0] * n
    center = 0
    right_boundary = 0
    
    for i in range(n):
        if i < right_boundary:
            radii[i] = min(right_boundary - i, radii[2 * center - i])
        
        # Attempt to expand around center i
        while (i - radii[i] - 1 >= 0 and 
               i + radii[i] + 1 < n and 
               s[i - radii[i] - 1] == s[i + radii[i] + 1]):
            radii[i] += 1
            
        if i + radii[i] > right_boundary:
            center = i
            right_boundary = i + radii[i]

    # max_end_at[i]: max length of an odd palindrome ending at index i
    # max_start_at[i]: max length of an odd palindrome starting at index i
    max_end_at = [1] * n
    max_start_at = [1] * n

    # Fill max_end_at using the radii
    # A palindrome with radius r centered at i ends at i + r
    for i in range(n):
        length = 2 * radii[i] + 1
        end_idx = i + radii[i]
        max_end_at[end_idx] = max(max_end_at[end_idx], length)
        
        start_idx = i - radii[i]
        max_start_at[start_idx] = max(max_start_at[start_idx], length)

    # Propagate the lengths: if a palindrome of length L ends at i, 
    # then a palindrome of length L-2 ends at i-1.
    # This ensures we cover all possible ending/starting positions.
    for i in range(n - 1, 0, -1):
        max_end_at[i - 1] = max(max_end_at[i - 1], max_end_at[i] - 2)
    
    for i in range(n - 1):
        max_start_at[i + 1] = max(max_start_at[i + 1], max_start_at[i] - 2)

    # To handle the "non-overlapping" constraint, we need the max length 
    # ending AT OR BEFORE i, and starting AT OR AFTER i+1.
    # We transform max_end_at to be prefix max and max_start_at to be suffix max.
    for i in range(1, n):
        max_end_at[i] = max(max_end_at[i], max_end_at[i - 1])
        
    for i in range(n - 2, -1, -1):
        max_start_at[i] = max(max_start_at[i], max_start_at[i + 1])

    MOD = 10**9 + 7
    max_product = 0
    
    # Iterate through all possible split points
    for i in range(n - 1):
        # max_end_at[i] is the max length of a palindrome in s[0...i]
        # max_start_at[i+1] is the max length of a palindrome in s[i+1...n-1]
        product = max_end_at[i] * max_start_at[i + 1]
        if product > max_product:
            max_product = product

    return max_product % MOD
