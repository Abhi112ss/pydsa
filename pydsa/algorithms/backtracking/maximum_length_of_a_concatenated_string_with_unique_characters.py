METADATA = {
    "id": 1239,
    "name": "Maximum Length of a Concatenated String with Unique Characters",
    "slug": "maximum-length-of-a-concatenated-string-with-unique-characters",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "bit_manipulation", "string", "bitmask"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(2^n)",
    "description": "Find the maximum length of a string formed by concatenating a subset of given strings such that all characters in the resulting string are unique.",
}

def solve(arr: list[str]) -> int:
    """
    Finds the maximum length of a concatenated string with unique characters.

    Args:
        arr: A list of strings to choose from.

    Returns:
        The maximum length of a concatenated string containing only unique characters.

    Examples:
        >>> solve(["un", "iq", "ue"])
        4
        >>> solve(["cha", "r", "act", "ers"])
        6
    """
    # Convert each string into a bitmask representing its character set.
    # If a string itself has duplicate characters, we mark it as invalid.
    masks = []
    for s in arr:
        mask = 0
        is_unique = True
        for char in s:
            bit = 1 << (ord(char) - ord('a'))
            # If the bit is already set, the string has duplicate characters
            if mask & bit:
                is_unique = False
                break
            mask |= bit
        if is_unique:
            masks.append((mask, len(s)))

    # We use a set to store all valid bitmasks encountered so far.
    # Each bitmask represents a unique combination of characters.
    valid_masks = {0}
    max_length = 0

    for mask, length in masks:
        # We iterate over a copy of current valid masks to avoid modification during iteration
        current_combinations = list(valid_masks)
        for existing_mask in current_combinations:
            # Check if the current string's characters overlap with the existing combination
            if not (existing_mask & mask):
                new_mask = existing_mask | mask
                valid_masks.add(new_mask)
                
                # Calculate the length of the new combination
                # Since we store masks, we can calculate length by counting bits or 
                # by tracking lengths during the process. Here we track max_length.
                # To be efficient, we can calculate length of new_mask using bin().count('1')
                # or simply track it. Let's use bit counting for simplicity.
                new_length = bin(new_mask).count('1')
                if new_length > max_length:
                    max_length = new_length

    # Handle the case where the input might result in 0 length
    # (though the loop above handles it via the initial 0 mask)
    return max_length
