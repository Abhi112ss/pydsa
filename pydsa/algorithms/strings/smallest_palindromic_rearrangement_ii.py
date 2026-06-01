METADATA = {
    "id": 3518,
    "name": "Smallest Palindromic Rearrangement II",
    "slug": "smallest_palindromic_rearrangement_ii",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "greedy", "backtracking"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest palindromic rearrangement of a string that satisfies specific positional constraints.",
}

def solve(s: str, constraints: list[list[int]]) -> str:
    """
    Finds the lexicographically smallest palindromic rearrangement of string 's'
    that satisfies the given positional constraints.

    Args:
        s: The input string to be rearranged.
        constraints: A list of [index, char_index] where constraints[i][0] is the 
                     position in the palindrome and constraints[i][1] is the index 
                     of the character in the original string 's' that must be there.
                     Note: In a palindrome, if index i is constrained, index n-1-i 
                     is implicitly constrained to the same character.

    Returns:
        The lexicographically smallest palindromic string, or an empty string if impossible.

    Examples:
        >>> solve("aabb", [[0, 0]])
        "abba"
        >>> solve("aabb", [[0, 1]])
        "abba"
    """
    n = len(s)
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Check if a palindrome is even possible with given counts
    odd_count = 0
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1
    if odd_count > (1 if n % 2 != 0 else 0):
        return ""

    # result array to build the palindrome
    res = [None] * n
    
    # Map constraints to specific characters
    # Since it's a palindrome, constraint at i affects i and n-1-i
    fixed_chars = {}
    for idx, s_idx in constraints:
        char = s[s_idx]
        # Check for conflicts: if index is already set to a different char
        if idx in fixed_chars and fixed_chars[idx] != char:
            return ""
        if (n - 1 - idx) in fixed_chars and fixed_chars[n - 1 - idx] != char:
            return ""
        fixed_chars[idx] = char
        fixed_chars[n - 1 - idx] = char

    # Validate if fixed characters exceed available counts
    temp_counts = char_counts.copy()
    for idx, char in fixed_chars.items():
        # We only count each pair once for the first half or middle
        if idx <= (n - 1) // 2:
            # If it's the middle element in an odd string
            if n % 2 != 0 and idx == n // 2:
                temp_counts[char] -= 1
            else:
                # It's a pair
                temp_counts[char] -= 2
        elif idx == n // 2 and n % 2 != 0:
             temp_counts[char] -= 1
        
        # If we use more than available (accounting for symmetry)
        # This logic is simplified; actual validation happens during construction
    
    # Re-calculating counts based on fixed positions
    # We fill the first half (0 to n//2 - 1) and the middle if exists
    available_counts = char_counts.copy()
    
    # 1. Apply fixed constraints to available counts
    # We iterate through the first half to avoid double counting
    for i in range((n + 1) // 2):
        mirror_i = n - 1 - i
        
        # Check if i or mirror_i is constrained
        char_at_i = fixed_chars.get(i) or fixed_chars.get(mirror_i)
        
        if char_at_i:
            if i == mirror_i: # Middle element
                available_counts[char_at_i] -= 1
            else:
                available_counts[char_at_i] -= 2
            
            if available_counts[char_at_i] < 0:
                return ""
            res[i] = res[mirror_i] = char_at_i
        else:
            res[i] = res[mirror_i] = None

    # 2. Greedy construction for the remaining slots in the first half
    sorted_chars = sorted(available_counts.keys())
    
    for i in range((n + 1) // 2):
        if res[i] is not None:
            continue
            
        # Try characters in lexicographical order
        found = False
        for char in sorted_chars:
            if available_counts[char] >= (2 if i != n - 1 - i else 1):
                # Check if this choice is valid (doesn't violate future constraints)
                # In this specific problem, since constraints are pre-applied,
                # we just need to ensure we don't run out of characters.
                res[i] = res[n - 1 - i] = char
                available_counts[char] -= (2 if i != n - 1 - i else 1)
                found = True
                break
        
        if not found:
            return ""

    # Final verification: check if the constructed palindrome matches original counts
    final_str = "".join(res)
    final_counts = {}
    for c in final_str:
        final_counts[c] = final_counts.get(c, 0) + 1
    
    if final_counts != char_counts:
        return ""

    return final_str
