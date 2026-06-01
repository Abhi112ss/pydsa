METADATA = {
    "id": 1513,
    "name": "Number of Substrings With Only 1s",
    "slug": "number_of_substrings_with_only_1s",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count substrings consisting solely of '1's in a binary string.",
}


def solve(s: str) -> int:
    """Count substrings consisting only of '1's.

    Args:
        s: A binary string containing only characters '0' and '1'.

    Returns:
        The total number of substrings that contain only '1's.

    Examples:
        >>> solve("0110111")
        9
        >>> solve("101")
        2
    """
    total_substrings = 0
    consecutive_ones = 0

    for character in s:
        if character == "1":
            # Extend existing substrings and start a new one ending at this position
            consecutive_ones += 1
            total_substrings += consecutive_ones
        else:
            # Reset count when a '0' is encountered
            consecutive_ones = 0

    return total_substrings