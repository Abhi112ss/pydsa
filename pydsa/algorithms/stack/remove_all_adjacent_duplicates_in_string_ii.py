METADATA = {
    "id": 1209,
    "name": "Remove All Adjacent Duplicates in String II",
    "slug": "remove-all-adjacent-duplicates-in-string-ii",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove k adjacent duplicate characters from a string repeatedly until no more such removals are possible.",
}

def solve(s: str, k: int) -> str:
    """
    Removes k adjacent duplicate characters from the string repeatedly.

    Args:
        s: The input string containing lowercase English letters.
        k: The number of adjacent duplicate characters to remove.

    Returns:
        The resulting string after all possible removals.

    Examples:
        >>> solve("deeedbbcccbdaa", 3)
        'aa'
        >>> solve("abbaca", 2)
        'ca'
    """
    # The stack will store pairs of [character, consecutive_count]
    # Using a list of lists to allow in-place modification of the count
    stack: list[list] = []

    for char in s:
        if stack and stack[-1][0] == char:
            # If the current character matches the top of the stack, increment count
            stack[-1][1] += 1
            
            # If the count reaches k, remove this character entry from the stack
            if stack[-1][1] == k:
                stack.pop()
        else:
            # Otherwise, push a new character entry with a count of 1
            stack.append([char, 1])

    # Reconstruct the string by repeating each character by its remaining count
    result_parts = []
    for char, count in stack:
        result_parts.append(char * count)

    return "".join(result_parts)
