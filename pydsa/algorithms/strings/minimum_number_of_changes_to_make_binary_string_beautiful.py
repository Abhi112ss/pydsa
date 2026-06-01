METADATA = {
    "id": 2914,
    "name": "Minimum Number of Changes to Make Binary String Beautiful",
    "slug": "minimum-number-of-changes-to-make-binary-string-beautiful",
    "category": "Greedy",
    "aliases": [],
    "tags": ["string", "greedy", "prefix-sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of character flips required to make a binary string beautiful, where a beautiful string consists of all 0s followed by all 1s.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of flips to make a binary string beautiful.
    
    A string is beautiful if all '0's come before all '1's.
    
    Args:
        s: A binary string consisting of '0's and '1's.
        
    Returns:
        The minimum number of flips required.
        
    Examples:
        >>> solve("01001")
        1
        >>> solve("00011")
        0
        >>> solve("111000")
        3
    """
    # A beautiful string has a split point where everything to the left is '0'
    # and everything to the right is '1'.
    # We can track the number of '1's encountered so far (which would need to be flipped to '0')
    # and the number of '0's remaining to the right (which would need to be flipped to '1').
    
    total_zeros = s.count('0')
    
    # Initial state: assume the split point is at the very beginning (all '1's)
    # We need to flip all '0's to '1's.
    # However, it's easier to think: 
    # flips = (count of '1's seen so far) + (count of '0's remaining to the right)
    
    # Let's use a more direct approach:
    # We want to minimize: (count of '1's in prefix) + (count of '0's in suffix)
    
    # First, calculate the cost if the split is at index 0 (all characters are '1's)
    # This means we must flip all '0's to '1's.
    current_ones_in_prefix = 0
    current_zeros_in_suffix = total_zeros
    
    # The initial cost if the string is all '1's:
    min_flips = current_zeros_in_suffix
    
    for char in s:
        if char == '1':
            # If we encounter a '1', it's part of the prefix. 
            # If we decide this '1' belongs to the '0' section, it must be flipped.
            current_ones_in_prefix += 1
        else:
            # If we encounter a '0', it's no longer in the suffix.
            # It doesn't need to be flipped to '1' anymore.
            current_zeros_in_suffix -= 1
            
        # The cost at this split point is the number of 1s we've passed 
        # (which must become 0) plus the number of 0s left (which must become 1).
        min_flips = min(min_flips, current_ones_in_prefix + current_zeros_in_suffix)
        
    return min_flips
