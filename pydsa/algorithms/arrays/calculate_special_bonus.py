METADATA = {
    "id": 1873,
    "name": "Calculate Special Bonus",
    "slug": "calculate_special_bonus",
    "category": "array",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Compute the total special bonus based on daily points with neighbor comparisons.",
}

def solve(points: list[int]) -> int:
    """Calculate the special bonus for a sequence of daily points.

    Args:
        points: A list of integers where points[i] represents the points earned on day i.

    Returns:
        An integer representing the total special bonus calculated according to the rules:
        - For the first day, compare with the second day only.
        - For the last day, compare with the penultimate day only.
        - For all other days, compare with both immediate neighbors.
        Add points[i] to the bonus if it is strictly greater than its neighbor(s);
        subtract points[i] from the bonus if it is strictly less than its neighbor(s);
        otherwise, do nothing.

    Examples:
        >>> solve([1, 2, 3, 4])
        -2
        >>> solve([5, 1, 5])
        9
    """
    if not points:
        return 0

    total_bonus = 0
    last_index = len(points) - 1

    for day_index in range(len(points)):
        current_point = points[day_index]

        if day_index == 0:
            # Only compare with the next day
            neighbor_point = points[1]
            if current_point > neighbor_point:
                total_bonus += current_point
            elif current_point < neighbor_point:
                total_bonus -= current_point
        elif day_index == last_index:
            # Only compare with the previous day
            neighbor_point = points[last_index - 1]
            if current_point > neighbor_point:
                total_bonus += current_point
            elif current_point < neighbor_point:
                total_bonus -= current_point
        else:
            # Compare with both immediate neighbors
            left_neighbor = points[day_index - 1]
            right_neighbor = points[day_index + 1]
            if current_point > left_neighbor and current_point > right_neighbor:
                total_bonus += current_point
            elif current_point < left_neighbor and current_point < right_neighbor:
                total_bonus -= current_point

    return total_bonus