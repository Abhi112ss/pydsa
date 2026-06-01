METADATA = {
    "id": 3039,
    "name": "Apply Operations to Make String Empty",
    "slug": "apply-operations-to-make-string-empty",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string_matching", "queue"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a string can be made empty by repeatedly removing the first occurrence of the first character of the string and its subsequent matching characters.",
}

def solve(s: str, target: str) -> bool:
    """
    Determines if the string 's' can be transformed into 'target' by repeatedly 
    removing the first character of the current string and all subsequent 
    identical characters.

    Args:
        s: The initial string.
        target: The target string to match.

    Returns:
        True if 's' can be transformed into 'target', False otherwise.

    Examples:
        >>> solve("abacaba", "abc")
        True
        >>> solve("abacaba", "acb")
        False
    """
    # Pre-calculate the indices of each character in 's' to allow O(1) access
    # to the next occurrence of a specific character.
    char_indices: dict[str, list[int]] = {}
    for index, char in enumerate(s):
        if char not in char_indices:
            char_indices[char] = []
        char_indices[char].append(index)

    # Track the current position in 's' to ensure we only pick characters 
    # that appear after the previously picked character.
    current_s_pointer = 0
    
    # Track the current index within each character's list of indices.
    # This avoids O(n) pop(0) operations.
    char_ptr_map: dict[str, int] = {char: 0 for char in char_indices}

    for target_char in target:
        # If the target character doesn't exist in 's', it's impossible.
        if target_char not in char_indices:
            return False
        
        # Find the next available index for the target character.
        found = False
        indices_list = char_indices[target_char]
        start_ptr = char_ptr_map[target_char]
        
        # Iterate through the pre-calculated indices for this character.
        for i in range(start_ptr, len(indices_list)):
            idx = indices_list[i]
            # The character must appear at or after the current pointer.
            if idx >= current_s_pointer:
                # Update the pointer for this character to skip used indices.
                char_ptr_map[target_char] = i + 1
                # Move the global pointer to the position immediately after this character.
                current_s_pointer = idx + 1
                found = True
                break
        
        if not found:
            return False

    # If we successfully matched all characters in 'target' in order, return True.
    return True
