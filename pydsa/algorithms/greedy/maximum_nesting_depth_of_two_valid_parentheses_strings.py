METADATA = {
    "id": 1111,
    "name": "Maximum Nesting Depth of Two Valid Parentheses Strings",
    "slug": "maximum-nesting-depth-of-two-valid-parentheses-strings",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "stack", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Distribute parentheses from a single valid string into two separate valid strings to maximize the sum of their maximum nesting depths.",
}

def solve(s: str) -> list[int]:
    """
    Distributes parentheses from a valid string into two separate valid strings
    to maximize the sum of their maximum nesting depths.

    The strategy is to assign parentheses to the two strings based on the 
    current nesting level. If the current depth is even, we assign to string A; 
    if odd, we assign to string B. This ensures both resulting strings are valid.

    Args:
        s: A valid parentheses string.

    Returns:
        A list of two integers representing the maximum nesting depth of 
        the two constructed strings.

    Examples:
        >>> solve("(()())")
        [2, 1]
        >>> solve("((()))")
        [3, 0]
        >>> solve("()()()")
        [1, 1]
    """
    depth_a = 0
    depth_b = 0
    
    current_nesting_level = 0
    
    # Track the maximum depth reached for each constructed string
    max_depth_a = 0
    max_depth_b = 0
    
    # Track current depth within each specific string to calculate max depth
    current_depth_a = 0
    current_depth_b = 0

    for char in s:
        if char == '(':
            current_nesting_level += 1
            # Distribute based on whether the current level is even or odd
            if current_nesting_level % 2 == 1:
                current_depth_a += 1
                max_depth_a = max(max_depth_a, current_depth_a)
            else:
                current_depth_b += 1
                max_depth_b = max(max_depth_b, current_depth_b)
        else:
            # When closing, we must decrement the depth of the string 
            # that the corresponding opening parenthesis belonged to.
            if current_nesting_level % 2 == 1:
                current_depth_a -= 1
            else:
                current_depth_b -= 1
            current_nesting_level -= 1

    return [max_depth_a, max_depth_b]
