METADATA = {
    "id": 2002,
    "name": "Maximum Product of the Length of Two Palindromic Subsequences",
    "slug": "maximum-product-of-the-length-of-two-palindromic-subsequences",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_mask", "dp", "subsequence"],
    "difficulty": "medium",
    "time_complexity": "O(2^n * n)",
    "space_complexity": "O(2^n)",
    "description": "Find the maximum product of the lengths of two disjoint palindromic subsequences in a given string.",
}

def solve(s: str) -> int:
    """
    Calculates the maximum product of the lengths of two disjoint palindromic subsequences.

    Args:
        s: The input string.

    Returns:
        The maximum product of the lengths of two disjoint palindromic subsequences.

    Examples:
        >>> solve("leetcode")
        12
        >>> solve("bb"))
        1
    """
    n = len(s)
    # Dictionary to store the length of the palindrome for each bitmask
    # mask -> length
    palindrome_lengths: dict[int, int] = {}

    # Step 1: Precompute all possible palindromic subsequences using bitmasks
    # There are 2^n possible subsequences
    for mask in range(1, 1 << n):
        subsequence = ""
        for i in range(n):
            # Check if the i-th character is included in the current mask
            if (mask >> i) & 1:
                subsequence += s[i]
        
        # Check if the extracted subsequence is a palindrome
        if subsequence == subsequence[::-1]:
            palindrome_lengths[mask] = len(subsequence)

    max_product = 0
    
    # Convert to list of tuples to avoid repeated dict lookups in the nested loop
    # Each tuple is (mask, length)
    palindromes = list(palindrome_lengths.items())

    # Step 2: Compare all pairs of palindromic masks to find disjoint ones
    for i in range(len(palindromes)):
        mask_a, len_a = palindromes[i]
        for j in range(i + 1, len(palindromes)):
            mask_b, len_b = palindromes[j]
            
            # Two subsequences are disjoint if their bitmasks have no common set bits
            if (mask_a & mask_b) == 0:
                product = len_a * len_b
                if product > max_product:
                    max_product = product

    return max_product
