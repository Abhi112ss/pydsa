METADATA = {
    "id": 3398,
    "name": "Smallest Substring With Identical Characters I",
    "slug": "smallest-substring-with-identical-characters-i",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the smallest substring consisting of identical characters.",
}

def solve(s: str) -> int:
    """
    Finds the length of the smallest substring consisting of identical characters.
    Since the problem asks for the smallest substring with identical characters,
    and any single character is a substring of length 1 with identical characters,
    the answer is always 1 if the string is non-empty.
    
    However, based on the problem context of finding the smallest length of 
    consecutive identical characters (blocks), we iterate through the string 
    to find the minimum length of any contiguous block of the same character.

    Args:
        s: The input string.

    Returns:
        The length of the smallest contiguous block of identical characters.

    Examples:
        >>> solve("aabbbc")
        1
        >>> solve("aaabbb")
        3
        >>> solve("abc")
        1
    """
    if not s:
        return 0

    min_block_length = float('inf')
    current_block_length = 0
    previous_char = ""

    for char in s:
        if char == previous_char:
            # Increment the current block length if the character is the same
            current_block_length += 1
        else:
            # If character changes, update the minimum and reset block length
            if current_block_length > 0:
                min_block_length = min(min_block_length, current_block_length)
            
            current_block_length = 1
            previous_char = char

    # Final check for the last block in the string
    min_block_length = min(min_block_length, current_block_length)

    return int(min_block_length)
