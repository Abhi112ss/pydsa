METADATA = {
    "id": 1234,
    "name": "Replace the Substring for Balanced String",
    "slug": "replace-the-substring-for-balanced-string",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "string", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the shortest substring that can be replaced to make a string balanced.",
}

def solve(s: str, k: int) -> int:
    """
    Finds the length of the shortest substring that can be replaced to make 
    the string balanced (each character 'Q', 'W', 'E', 'R' appears exactly k times).

    Args:
        s: The input string consisting of 'Q', 'W', 'E', 'R'.
        k: The target frequency for each character.

    Returns:
        The length of the shortest substring to replace. Returns 0 if already balanced.

    Examples:
        >>> solve("QQQWER", 1)
        3
        >>> solve("QQQWER", 2)
        0
    """
    n = len(s)
    target = k
    counts = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
    
    # Initial pass to count all characters in the string
    for char in s:
        counts[char] += 1
        
    # Check if the string is already balanced
    if all(counts[c] == target for c in "QWER"):
        return 0

    min_len = n
    left = 0
    
    # Sliding window approach:
    # We want to find the smallest window [left, right] such that 
    # all characters OUTSIDE the window have counts <= target.
    for right in range(n):
        # Remove the character at 'right' from the "outside" counts
        counts[s[right]] -= 1
        
        # While the current window satisfies the condition (all outside counts <= target)
        # try to shrink the window from the left to find the minimum length.
        while left <= right and all(counts[c] <= target for c in "QWER"):
            min_len = min(min_len, right - left + 1)
            
            # Add the character at 'left' back to the "outside" counts
            counts[s[left]] += 1
            left += 1
            
    return min_len
