METADATA = {
    "id": 1893,
    "name": "Check if All the Integers in a Range Are Covered",
    "slug": "check_if_all_the_integers_in_a_range_are_covered",
    "category": "array",
    "aliases": [],
    "tags": ["difference_array", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n + max_val)",
    "space_complexity": "O(max_val)",
    "description": "Determine whether every integer in a target range is covered by at least one of the given intervals.",
}

def solve(ranges: list[list[int]], left: int, right: int) -> bool:
    """Check if all integers in the target range [left, right] are covered.

    Args:
        ranges: A list of intervals where each interval is represented as
                [interval_left, interval_right].
        left:   The left bound of the target range (inclusive).
        right:  The right bound of the target range (inclusive).

    Returns:
        True if every integer in [left, right] is covered by at least one interval,
        otherwise False.

    Examples:
        >>> solve([[1,2],[3,4],[5,6]], 2, 5)
        False
        >>> solve([[1,10]], 2, 5)
        True
    """
    if left > right:
        return True  # empty target range is trivially covered

    # Determine the maximum coordinate needed for the difference array.
    max_coordinate = right
    for interval in ranges:
        interval_right = interval[1]
        if interval_right > max_coordinate:
            max_coordinate = interval_right

    # Initialize difference array.
    diff = [0] * (max_coordinate + 2)  # +2 to safely handle r+1 index

    # Apply each interval to the difference array.
    for interval in ranges:
        interval_left, interval_right = interval
        diff[interval_left] += 1
        diff[interval_right + 1] -= 1  # mark the end of coverage

    # Compute prefix sums and verify coverage for the target range.
    current_coverage = 0
    for position in range(max_coordinate + 1):
        current_coverage += diff[position]
        if left <= position <= right:
            if current_coverage == 0:
                return False  # uncovered integer found

    return True