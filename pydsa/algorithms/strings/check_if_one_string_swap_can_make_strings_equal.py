METADATA = {
    "id": 1790,
    "name": "Check if One String Swap Can Make Strings Equal",
    "slug": "check-if-one-string-swap-can-make-strings-equal",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a single swap of two characters in one string can make it equal to another string.",
}

def solve(s: str, t: str) -> bool:
    """
    Determines if swapping two characters in string s can make it equal to string t.

    Args:
        s: The first input string.
        t: The second input string.

    Returns:
        True if a single swap makes the strings equal, False otherwise.

    Examples:
        >>> solve("swapping", "swapping")
        True
        >>> solve("bank", "kanb")
        True
        >>> solve("attack", "defend")
        False
    """
    # If strings are already equal, no swap is needed (or a swap of same chars works)
    if s == t:
        return True

    # Store indices where the characters differ
    mismatched_indices: list[int] = []
    
    # Iterate through both strings to find all positions where characters don't match
    for i in range(len(s)):
        if s[i] != t[i]:
            mismatched_indices.append(i)
            
        # Optimization: if more than 2 mismatches, one swap cannot fix it
        if len(mismatched_indices) > 2:
            return False

    # A single swap can only fix exactly 2 mismatches
    if len(mismatched_indices) != 2:
        return False

    # Check if swapping the two mismatched characters in s results in t
    # Specifically: s[i] must match t[j] AND s[j] must match t[i]
    idx1, idx2 = mismatched_indices
    return s[idx1] == t[idx2] and s[idx2] == t[idx1]
