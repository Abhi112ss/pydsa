METADATA = {
    "id": 1758,
    "name": "Minimum Changes To Make Alternating Binary String",
    "slug": "minimum_changes_to_make_alternating_binary_string",
    "category": "String",
    "aliases": [],
    "tags": ["string", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the minimum number of flips to make a binary string alternating.",
}


def solve(binary_string: str) -> int:
    """Calculate the minimum number of character flips required to transform
    the given binary string into an alternating pattern.

    Args:
        binary_string: A string consisting only of characters '0' and '1'.

    Returns:
        The minimal number of flips needed so that the string becomes either
        "010101..." or "101010...".

    Examples:
        >>> solve("0100")
        1
        >>> solve("1111")
        2
        >>> solve("000")
        1
    """
    # Counters for mismatches against the two possible alternating patterns.
    flips_start_with_zero = 0  # pattern: 0,1,0,1,...
    flips_start_with_one = 0   # pattern: 1,0,1,0,...

    for index, character in enumerate(binary_string):
        expected_char_zero = '0' if index % 2 == 0 else '1'
        expected_char_one = '1' if index % 2 == 0 else '0'

        if character != expected_char_zero:
            flips_start_with_zero += 1
        if character != expected_char_one:
            flips_start_with_one += 1

    # The answer is the smaller mismatch count between the two patterns.
    return min(flips_start_with_zero, flips_start_with_one)