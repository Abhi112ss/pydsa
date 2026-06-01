METADATA = {
    "id": 1422,
    "name": "Maximum Score After Splitting a String",
    "slug": "maximum-score-after-splitting-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "prefix_sum", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum score obtained by splitting a binary string into two non-empty substrings, where score is the sum of zeros in the left part and ones in the right part.",
}

def solve(s: str) -> int:
    """
    Calculates the maximum score possible by splitting a binary string into two non-empty parts.
    
    The score is defined as the number of '0's in the left substring plus the 
    number of '1's in the right substring.

    Args:
        s: A binary string consisting of '0's and '1's.

    Returns:
        The maximum score achievable.

    Examples:
        >>> solve("011101")
        3
        >>> solve("01")
        1
        >>> solve("000111")
        4
    """
    # Total count of ones in the entire string to allow O(1) calculation of right-side ones
    total_ones = s.count('1')
    
    max_score = 0
    zeros_left = 0
    ones_left = 0
    
    # Iterate through the string up to the second to last character 
    # to ensure both substrings are non-empty.
    for i in range(len(s) - 1):
        if s[i] == '0':
            zeros_left += 1
        else:
            ones_left += 1
            
        # The number of ones in the right part is (total_ones - ones_left)
        ones_right = total_ones - ones_left
        
        # Current score = zeros in left + ones in right
        current_score = zeros_left + ones_right
        
        if current_score > max_score:
            max_score = current_score
            
    return max_score
