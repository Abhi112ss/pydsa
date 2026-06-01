METADATA = {
    "id": 1529,
    "name": "Minimum Suffix Flips",
    "slug": "minimum_suffix_flips",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of suffix flips required to transform a binary string into a target binary string.",
}

def solve(s: str, target: str) -> int:
    """
    Calculates the minimum number of suffix flips needed to transform s into target.
    
    A suffix flip involves choosing an index i and flipping all characters from 
    index i to the end of the string (0 becomes 1, 1 becomes 0).

    Args:
        s: The initial binary string.
        target: The target binary string.

    Returns:
        The minimum number of suffix flips required.

    Examples:
        >>> solve("0011", "1100")
        2
        >>> solve("0101", "0101")
        0
        >>> solve("111", "000")
        1
    """
    n = len(s)
    flips = 0
    # current_state tracks whether the current character is flipped 
    # relative to its original value based on previous suffix flips.
    # 0 means original, 1 means flipped.
    current_flip_state = 0
    
    # We iterate from right to left because a flip at index i 
    # affects all indices from i to n-1. By going backwards, 
    # we can determine if the current character matches the target 
    # after all subsequent flips have been applied.
    for i in range(n - 1, -1, -1):
        # Determine the actual value of s[i] after applying previous flips
        # If current_flip_state is 1, '0' becomes '1' and '1' becomes '0'
        original_val = int(s[i])
        actual_val = original_val if current_flip_state == 0 else 1 - original_val
        
        target_val = int(target[i])
        
        # If the current actual value doesn't match the target, 
        # we must perform a flip starting at this index.
        if actual_val != target_val:
            flips += 1
            # Toggle the flip state for all characters to the left
            current_flip_state = 1 - current_flip_state
            
    return flips
