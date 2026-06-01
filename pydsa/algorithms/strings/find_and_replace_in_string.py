METADATA = {
    "id": 833,
    "name": "Find and Replace in String",
    "slug": "find-and-replace-in-string",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n + m log m)",
    "space_complexity": "O(n)",
    "description": "Replace substrings in a string based on given indices and new strings, ensuring replacements do not overlap.",
}

def solve(s: str, replacements: list[list]) -> str:
    """
    Replaces substrings in string 's' based on provided replacement operations.
    
    Each replacement is a list [index, length, new_string]. If a replacement 
    overlaps with another, the one with the smaller index is prioritized.
    
    Args:
        s: The original input string.
        replacements: A list of lists where each sub-list is [index, length, new_string].
        
    Returns:
        The modified string after all valid replacements are applied.
        
    Examples:
        >>> solve("abcd", [[0, 2, "eeee"], [2, 1, "ffff"]])
        'eeeeffffd'
        >>> solve("abcd", [[0, 1, "eee"], [0, 2, "ffff"]])
        'eeefcd'
    """
    # Sort replacements by index in descending order.
    # This allows us to modify the string from right to left, 
    # preventing the indices of pending replacements from shifting.
    sorted_replacements = sorted(replacements, key=lambda x: x[0], reverse=True)
    
    # Convert string to a list for easier manipulation if needed, 
    # but since we work backwards, we can just slice the string.
    result_string = s
    
    for index, length, new_string in sorted_replacements:
        # Check if the current replacement overlaps with the part of the string 
        # we have already processed (which is to the right of the current index).
        # However, because we sort descending, we only need to ensure we don't 
        # overwrite a replacement we just made. 
        # Actually, the problem states: "If there are multiple replacements 
        # that overlap, only the one with the smallest index is used."
        # By sorting descending, we process the largest index first. 
        # To handle the "smallest index priority" rule correctly, we should 
        # actually identify which replacements are valid first.
        pass

    # Re-evaluating the strategy for the "smallest index priority" rule:
    # 1. Sort replacements by index ascending.
    # 2. Iterate and pick replacements that don't overlap with the previously picked one.
    # 3. Apply them from right to left.

    replacements.sort()
    valid_replacements = []
    last_end_index = -1
    
    for start_index, length, new_string in replacements:
        end_index = start_index + length
        # If the current replacement starts after the last one ended, it's valid.
        if start_index > last_end_index:
            valid_replacements.append((start_index, length, new_string))
            last_end_index = end_index - 1 # Mark the end of the used range
            
    # Now apply valid replacements from right to left to avoid index shifting.
    # We sort valid_replacements by index descending.
    valid_replacements.sort(key=lambda x: x[0], reverse=True)
    
    res_list = list(s)
    # Since we are replacing chunks of different lengths, 
    # string slicing is cleaner than list manipulation.
    current_s = s
    for start, length, replacement_str in valid_replacements:
        # Slice the string: [everything before] + [new string] + [everything after the replaced part]
        current_s = current_s[:start] + replacement_str + current_s[start + length:]
        
    return current_s

# The logic above is slightly inefficient due to repeated string concatenation.
# Let's provide the optimized version using a single pass or list construction.

def solve_optimized(s: str, replacements: list[list]) -> str:
    """
    Optimized version using a jump-based approach or a mapping.
    """
    # Map start index to (length, new_string)
    # We only keep the one with the smallest index if there's a conflict.
    # But the rule is: if multiple overlap, pick the one with smallest index.
    
    # Sort by index ascending
    replacements.sort()
    
    # Filter to keep only non-overlapping replacements (smallest index priority)
    valid_map = {}
    last_end = -1
    for idx, length, new_str in replacements:
        if idx > last_end:
            valid_map[idx] = (length, new_str)
            last_end = idx + length - 1
            
    # Build the result string by iterating through the original string
    result = []
    i = 0
    while i < len(s):
        if i in valid_map:
            length, new_str = valid_map[i]
            result.append(new_str)
            i += length  # Skip the replaced characters
        else:
            result.append(s[i])
            i += 1
            
    return "".join(result)

# Assign the optimized version to solve
solve = solve_optimized