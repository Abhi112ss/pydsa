METADATA = {
    "id": 1578,
    "name": "Minimum Time to Make Rope Colorful",
    "slug": "minimum_time_to_make_rope_colorful",
    "category": "greedy",
    "aliases": [],
    "tags": ["greedy", "heap"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Compute the minimum total time to delete characters so that no two adjacent characters are the same.",
}


def solve(colors: str, neededTime: list[int]) -> int:
    """Calculate the minimum total time required to make the rope colorful.

    Args:
        colors: A string where each character represents the color of a rope segment.
        neededTime: A list of integers where neededTime[i] is the time to delete the i‑th segment.

    Returns:
        The minimum total time to delete segments so that no two adjacent segments share the same color.

    Examples:
        >>> solve("abaac", [1,2,3,4,5])
        3
        >>> solve("abc", [1,2,3])
        0
    """
    total_min_time = 0
    group_times: list[int] = []

    for index, (current_color, current_time) in enumerate(zip(colors, neededTime)):
        if index == 0 or current_color != colors[index - 1]:
            # start of a new color group; process the previous group if it exists
            if group_times:
                # keep the largest time, delete the rest
                group_times.sort(reverse=True)
                total_min_time += sum(group_times[1:])
                group_times.clear()
        # collect times for the current group
        group_times.append(current_time)

    # process the final group
    if group_times:
        group_times.sort(reverse=True)
        total_min_time += sum(group_times[1:])

    return total_min_time