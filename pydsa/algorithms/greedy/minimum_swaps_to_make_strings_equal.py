METADATA = {
    "id": 1247,
    "name": "Minimum Swaps to Make Strings Equal",
    "slug": "minimum-swaps-to-make-strings-equal",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of swaps to make two strings equal using character swaps within each string.",
}

def solve(s: str, t: str) -> int:
    """
    Calculates the minimum number of swaps required to make two strings equal.

    The strategy relies on counting the occurrences of 'xy' and 'yx' patterns 
    formed by comparing characters at the same index in both strings.
    - Two 'xy' patterns can be resolved in 1 swap.
    - Two 'yx' patterns can be resolved in 1 swap.
    - One 'xy' and one 'yx' pattern require 2 swaps.

    Args:
        s: The first input string.
        t: The second input string.

    Returns:
        The minimum number of swaps required. Returns -1 if it is impossible.

    Examples:
        >>> solve("xx", "yy")
        1
        >>> solve("xy", "yx")
        2
        >>> solve("xx", "xy")
        -1
    """
    xy_count = 0
    yx_count = 0

    # Iterate through both strings to find mismatches
    for char_s, char_t in zip(s, t):
        if char_s != char_t:
            if char_s == 'x' and char_t == 'y':
                xy_count += 1
            else:
                yx_count += 1

    # If the total number of mismatches is odd, it's impossible to pair them up
    # because each swap changes the parity of 'x's and 'y's in both strings.
    if (xy_count + yx_count) % 2 != 0:
        return -1

    # Each pair of identical mismatches (xy, xy) or (yx, yx) takes 1 swap.
    # The remaining mismatches will always be in pairs of (xy, yx) if the total is even.
    # A pair of (xy, yx) takes 2 swaps.
    # Mathematically, this simplifies to:
    # swaps = (xy_count // 2) + (yx_count // 2) + (remaining_xy_and_yx_pairs * 2)
    # Since (xy_count % 2) must equal (yx_count % 2) for the sum to be even,
    # the remainder is either 0 or 1 for both.
    
    swaps = (xy_count // 2) + (yx_count // 2)
    
    # If there's a remainder in both, it means we have one 'xy' and one 'yx' left.
    if xy_count % 2 != 0:
        swaps += 2

    return swaps
