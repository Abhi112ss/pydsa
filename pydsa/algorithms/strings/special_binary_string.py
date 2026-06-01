METADATA = {
    "id": 761,
    "name": "Special Binary String",
    "slug": "special-binary-string",
    "category": "String",
    "aliases": [],
    "tags": ["recursion", "greedy", "sorting", "stack"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Rearrange a special binary string to achieve the lexicographically largest possible order.",
}

def solve(s: str) -> str:
    """
    Rearranges a special binary string to its lexicographically largest form.
    
    A special binary string is defined such that:
    1. It is non-empty.
    2. It has an equal number of 0s and 1s.
    3. Every prefix has at least as many 1s as 0s.
    This is analogous to a valid parentheses string where '1' is '(' and '0' is ')'.
    
    Args:
        s: The input special binary string.
        
    Returns:
        The lexicographically largest special binary string possible.
        
    Examples:
        >>> solve("11011000")
        '11110000'
        >>> solve("1010")
        '1100'
        >>> solve("110010")
        '110010'
    """
    stack: list[str] = []
    
    # We use a stack to find the innermost "special" components.
    # A component is special if it's enclosed by a matching '1' and '0'.
    for char in s:
        if char == '1':
            stack.append(char)
        else:
            # When we encounter '0', we have completed a nested special component.
            # We collect all elements until the matching '1' is found.
            current_component = []
            while stack and stack[-1] == '1':
                # This logic is slightly different: we actually need to track 
                # the nested structures. A better way is to treat the stack 
                # as a way to capture the substring between matching 1 and 0.
                break # Placeholder for logic flow
            
            # Correct approach: Use stack to store substrings/components
            # instead of just characters to handle nesting.
            pass

    # Re-implementing with a more robust stack-based component extraction
    # to handle the recursive nature of the problem.
    
    def get_largest(input_str: str) -> str:
        stack: list[list[str]] = [[]]
        
        for char in input_str:
            if char == '1':
                # Start a new nested level
                stack.append([])
            else:
                # End the current level. Pop the inner component, 
                # sort its children, wrap it in '1' and '0', 
                # and add it to the parent level.
                inner_component = stack.pop()
                # Sort the components within this level to ensure lexicographical greatness
                inner_component.sort(reverse=True)
                
                # Reconstruct the special string for this level
                # We represent a component as a single string in the list
                reconstructed = "1" + "".join(inner_component) + "0"
                stack[-1].append(reconstructed)
        
        # The top level contains all top-level special components.
        # Sort them descending to get the largest string.
        top_level = stack[0]
        top_level.sort(reverse=True)
        return "".join(top_level)

    return get_largest(s)
