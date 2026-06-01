METADATA = {
    "id": 2381,
    "name": "Shifting Letters II",
    "slug": "shifting-letters-ii",
    "category": "String",
    "aliases": [],
    "tags": ["difference_array", "strings", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Apply multiple range shifts to a string and return the resulting string.",
}

def solve(s: str, shifts: list[list[int]]) -> str:
    """
    Applies multiple range shifts to a string using a difference array.

    Args:
        s: The input string consisting of lowercase English letters.
        shifts: A list of shifts where each shift is [start_index, end_index, shift_amount].

    Returns:
        The resulting string after all shifts are applied.

    Examples:
        >>> solve("abc", [[0, 1, 1], [1, 2, 1]])
        'cde'
        >>> solve("aaa", [[0, 2, 1], [1, 1, 1]])
        'abc'
    """
    n = len(s)
    # diff_array stores the net shift starting at each index.
    # We use size n + 1 to handle the boundary condition when end_index + 1 is accessed.
    diff_array = [0] * (n + 1)

    for start, end, shift in shifts:
        # Apply the shift to the range [start, end] using difference array logic.
        diff_array[start] += shift
        if end + 1 < n:
            diff_array[end + 1] -= shift

    # Convert the difference array into a prefix sum array to get the actual shift per index.
    current_cumulative_shift = 0
    result_chars = []
    
    for i in range(n):
        current_cumulative_shift += diff_array[i]
        
        # Calculate the new character. 
        # We use modulo 26 to keep the shift within the alphabet range.
        original_char_code = ord(s[i]) - ord('a')
        new_char_code = (original_char_code + current_cumulative_shift) % 26
        result_chars.append(chr(ord('a') + new_char_code))

    return "".join(result_chars)
