METADATA = {
    "id": 1888,
    "name": "Minimum Number of Flips to Make the Binary String Alternating",
    "slug": "minimum-number-of-flips-to-make-the-binary-string-alternating",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "strings", "sliding window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of flips to make a circular binary string alternating.",
}

def solve(s: str, k: int) -> int:
    """
    Calculates the minimum number of flips to make a circular substring of length k alternating.

    The problem is solved by doubling the string to handle circularity and using a 
    sliding window of size k. We compare the window against two possible alternating 
    patterns: one starting with '0' and one starting with '1'.

    Args:
        s: The input binary string.
        k: The length of the substring to make alternating.

    Returns:
        The minimum number of flips required.

    Examples:
        >>> solve("0110", 2)
        0
        >>> solve("010", 3)
        0
        >>> solve("1111", 2)
        1
    """
    n = len(s)
    # Double the string to handle circularity easily
    extended_s = s + s
    
    # We want to find the minimum flips for a window of size k.
    # There are two target patterns:
    # Pattern A: 0, 1, 0, 1... (even index is 0, odd index is 1)
    # Pattern B: 1, 0, 1, 0... (even index is 1, odd index is 0)
    
    # diff_a[i] will be 1 if extended_s[i] does NOT match Pattern A, else 0
    # diff_b[i] will be 1 if extended_s[i] does NOT match Pattern B, else 0
    # Note: Pattern B is just the inverse of Pattern A.
    
    diff_a = []
    for i in range(2 * n):
        # Pattern A expects '0' at even indices and '1' at odd indices
        expected_a = '0' if i % 2 == 0 else '1'
        diff_a.append(1 if extended_s[i] != expected_a else 0)
        
    # Initial window sum for Pattern A
    current_diff_a = sum(diff_a[:k])
    # Initial window sum for Pattern B is (k - current_diff_a) 
    # because if it doesn't match A, it must match B.
    current_diff_b = k - current_diff_a
    
    min_flips = min(current_diff_a, current_diff_b)
    
    # Slide the window across the extended string. 
    # We only need to check windows starting from index 1 up to n-1.
    # A window starting at index n would be the same as index 0.
    for i in range(1, n):
        # Remove the element leaving the window (i-1)
        # Add the element entering the window (i + k - 1)
        current_diff_a = current_diff_a - diff_a[i - 1] + diff_a[i + k - 1]
        current_diff_b = k - current_diff_a
        
        if current_diff_a < min_flips:
            min_flips = current_diff_a
        if current_diff_b < min_flips:
            min_flips = current_diff_b
            
    return min_flips
