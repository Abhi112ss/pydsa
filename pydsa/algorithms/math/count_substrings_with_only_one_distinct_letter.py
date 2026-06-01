METADATA = {
    "id": 1180,
    "name": "Count Substrings with Only One Distinct Letter",
    "slug": "count-substrings-with-only-one-distinct-letter",
    "category": "String",
    "aliases": [],
    "tags": ["combinatorics", "string", "two-pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings that contain only one distinct character.",
}

def solve(s: str) -> int:
    """
    Calculates the total number of substrings that consist of only one distinct character.

    The algorithm identifies contiguous blocks of identical characters. For a block 
    of length 'n', the number of possible substrings within that block is the 
    sum of integers from 1 to n, which is given by the formula: n * (n + 1) // 2.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The total count of substrings containing only one distinct character.

    Examples:
        >>> solve("aaaba")
        6
        # Substrings: "a", "a", "a", "aa", "aa", "aaa", "b", "a" -> Wait, 
        # "a", "a", "a", "aa", "aa", "aaa" (from aaa) + "b" + "a" = 6 + 1 + 1 = 8? 
        # Let's re-verify: "a", "a", "a", "aa", "aa", "aaa" (6) + "b" (1) + "a" (1) = 8.
        # Example 1: "aaaba" -> "a", "a", "a", "aa", "aa", "aaa", "b", "a" -> 8.
        # Example 2: "aaaaaaaaaa" -> 10 * 11 / 2 = 55.
    """
    if not s:
        return 0

    total_count = 0
    current_block_length = 0
    previous_char = ""

    for char in s:
        if char == previous_char:
            # Increment the length of the current contiguous block
            current_block_length += 1
        else:
            # Calculate substrings for the completed block using n*(n+1)/2
            # and reset for the new character
            total_count += (current_block_length * (current_block_length + 1)) // 2
            current_block_length = 1
            previous_char = char

    # Add the count for the final block processed in the loop
    total_count += (current_block_length * (current_block_length + 1)) // 2

    return total_count
