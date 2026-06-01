METADATA = {
    "id": 848,
    "name": "Shifting Letters",
    "slug": "shifting_letters",
    "category": "String",
    "aliases": [],
    "tags": ["prefix_sum", "math", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Apply a series of shifts to a string where each shift affects all subsequent characters.",
}

def solve(s: str, shifts: list[int]) -> str:
    """
    Applies a series of shifts to a string where each shift at index i 
    affects all characters from index i to the end of the string.

    Args:
        s: The input string to be shifted.
        shifts: A list of integers representing the number of shifts at each index.

    Returns:
        The resulting string after all shifts are applied.

    Examples:
        >>> solve("abc", [3, 5, 10])
        'pkq'
        >>> solve("aaaaa", [1, 1, 1, 1, 1])
        'fffff'
    """
    n = len(s)
    if n == 0:
        return ""

    # Calculate the total shift for each position using a suffix sum.
    # Instead of shifting the whole string for every element in 'shifts',
    # we calculate how many total shifts apply to each character.
    total_shifts = [0] * n
    current_suffix_sum = 0
    
    # Iterate backwards to build the suffix sum in O(n)
    for i in range(n - 1, -1, -1):
        current_suffix_sum += shifts[i]
        # We use modulo 26 to prevent integer overflow and keep numbers manageable
        total_shifts[i] = current_suffix_sum % 26

    result_chars = []
    for i in range(n):
        # Convert char to 0-25 scale
        original_pos = ord(s[i]) - ord('a')
        # Apply the pre-calculated total shift for this position
        new_pos = (original_pos + total_shifts[i]) % 26
        # Convert back to character
        result_chars.append(chr(new_pos + ord('a')))

    return "".join(result_chars)
