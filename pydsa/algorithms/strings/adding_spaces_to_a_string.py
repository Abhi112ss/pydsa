METADATA = {
    "id": 2109,
    "name": "Adding Spaces to a String",
    "slug": "adding-spaces-to-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["string", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Insert spaces into a string at specified indices to create a new string.",
}

def solve(s: str, space_indices: list[int]) -> str:
    """
    Inserts spaces into a string at the given indices.

    Args:
        s: The original input string.
        space_indices: A list of integers representing the indices where 
            spaces should be inserted. The indices are relative to the 
            original string.

    Returns:
        A new string with spaces inserted at the specified indices.

    Examples:
        >>> solve("hello", [1, 3])
        'h ello o'
        >>> solve("a", [0])
        ' a'
        >>> solve("abc", [])
        'abc'
    """
    # Sort indices to ensure we process them in order, 
    # though the problem constraints usually imply they are sorted.
    # If they aren't, sorting takes O(k log k) where k is len(space_indices).
    sorted_indices = sorted(space_indices)
    
    result_parts = []
    last_index = 0
    
    # Iterate through the requested space positions
    for space_idx in sorted_indices:
        # Append the substring from the last processed position to the current space index
        result_parts.append(s[last_index:space_idx])
        # Append the space itself
        result_parts.append(" ")
        # Update the pointer to the character after the space
        last_index = space_idx
        
    # Append the remaining part of the string after the last space
    result_parts.append(s[last_index:])
    
    # Join all parts to avoid O(n^2) string concatenation overhead
    return "".join(result_parts)
