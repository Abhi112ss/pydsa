METADATA = {
    "id": 1190,
    "name": "Reverse Substrings Between Each Pair of Parentheses",
    "slug": "reverse-substrings-between-each-pair-of-parentheses",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reverse the substrings within each pair of matching parentheses, processing from the innermost to the outermost.",
}

def solve(s: str) -> str:
    """
    Reverses the substrings between each pair of matching parentheses using the wormhole technique.

    The algorithm uses a 'wormhole' approach where we pre-calculate the matching 
    indices of parentheses. When we encounter a parenthesis, we jump to its 
    matching partner and reverse our traversal direction.

    Args:
        s: The input string containing lowercase English letters and parentheses.

    Returns:
        The resulting string after all reversals are applied.

    Examples:
        >>> solve("(u(love)i)")
        'iloveu'
        >>> solve("(ed(et(oc))el)")
        'leetcode'
    """
    n = len(s)
    # pair_map stores the index of the matching parenthesis for any given index
    pair_map = [0] * n
    stack = []

    # Step 1: Pre-calculate matching parentheses indices using a stack
    for index, char in enumerate(s):
        if char == '(':
            stack.append(index)
        elif char == ')':
            opening_index = stack.pop()
            pair_map[opening_index] = index
            pair_map[index] = opening_index

    result_chars = list(s)
    current_index = 0
    direction = 1  # 1 for forward, -1 for backward

    # Step 2: Traverse the string using the 'wormhole' jumps
    while 0 <= current_index < n:
        if result_chars[current_index] in ('(', ')'):
            # Jump to the matching parenthesis and flip direction
            current_index = pair_map[current_index]
            direction *= -1
        else:
            # Keep the character and move in the current direction
            # Note: We don't actually modify the string in-place during traversal
            # to avoid complex index management; we just build the result.
            pass
        
        # This specific implementation logic is slightly different: 
        # To achieve O(n), we simulate the traversal.
        # However, a cleaner way to implement the 'wormhole' is to 
        # traverse and build the string based on the direction.
        break # Break to use the correct O(n) traversal logic below

    # Corrected O(n) traversal logic
    final_result = []
    current_index = 0
    direction = 1
    
    while 0 <= current_index < n:
        if s[current_index] in ('(', ')'):
            # When hitting a parenthesis, jump to its partner and reverse direction
            current_index = pair_map[current_index]
            direction *= -1
        else:
            # When hitting a letter, add it to our result and move
            final_result.append(s[current_index])
            
        current_index += direction

    return "".join(final_result)
