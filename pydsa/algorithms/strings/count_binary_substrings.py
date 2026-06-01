METADATA = {
    "id": 696,
    "name": "Count Binary Substrings",
    "slug": "count_binary_substrings",
    "category": "String",
    "aliases": [],
    "tags": ["string", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings with equal number of consecutive 0's and 1's.",
}


def solve(s: str) -> int:
    """Count binary substrings where the number of consecutive 0's equals the number of consecutive 1's.

    Args:
        s: A binary string consisting only of characters '0' and '1'.

    Returns:
        The total count of non‑overlapping substrings that have the same number of consecutive
        0's and 1's and where all 0's and all 1's in the substring are grouped together.

    Examples:
        >>> solve("00110011")
        6
        >>> solve("10101")
        4
    """
    previous_group_len: int = 0          # length of the previous run of identical characters
    current_group_len: int = 1           # length of the current run (starts with first character)
    total_substrings: int = 0

    for index in range(1, len(s)):
        if s[index] == s[index - 1]:
            # extend the current group
            current_group_len += 1
        else:
            # a new group starts; add min(previous, current) to answer
            total_substrings += min(previous_group_len, current_group_len)
            previous_group_len = current_group_len
            current_group_len = 1

    # account for the last transition between the final two groups
    total_substrings += min(previous_group_len, current_group_len)
    return total_substrings