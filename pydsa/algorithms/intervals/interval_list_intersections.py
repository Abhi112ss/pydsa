METADATA = {
    "id": 986,
    "name": "Interval List Intersections",
    "slug": "interval-list-intersections",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Find the intersection of two lists of closed intervals.",
}

def solve(first_list: list[list[int]], second_list: list[list[int]]) -> list[list[int]]:
    """
    Finds the intersection of two lists of closed intervals using a two-pointer approach.

    Args:
        first_list: A list of closed intervals sorted by start time.
        second_list: A list of closed intervals sorted by start time.

    Returns:
        A list of closed intervals representing the intersection of the two input lists.

    Examples:
        >>> solve([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])
        [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    """
    intersections: list[list[int]] = []
    i, j = 0, 0

    while i < len(first_list) and j < len(second_list):
        # Find the boundaries of the potential intersection
        # The intersection starts at the maximum of the two start times
        # and ends at the minimum of the two end times.
        start_max = max(first_list[i][0], second_list[j][0])
        end_min = min(first_list[i][1], second_list[j][1])

        # If start_max <= end_min, there is a valid intersection
        if start_max <= end_min:
            intersections.append([start_max, end_min])

        # Move the pointer of the interval that ends earlier, 
        # as it cannot intersect with any subsequent intervals in the other list.
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1

    return intersections
