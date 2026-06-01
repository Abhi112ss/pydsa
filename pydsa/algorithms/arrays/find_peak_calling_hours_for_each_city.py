METADATA = {
    "id": 2984,
    "name": "Find Peak Calling Hours for Each City",
    "slug": "find_peak_calling_hours_for_each_city",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "sorting", "sweep_line"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the peak calling hours (maximum number of concurrent calls) for each city given a list of call intervals.",
}

def solve(intervals: list[list[int]], city_ids: list[int]) -> list[int]:
    """
    Finds the maximum number of concurrent calls (peak hours) for each city.

    Args:
        intervals: A list of lists where each sub-list contains [start_time, end_time].
        city_ids: A list of integers representing the city ID for each interval.

    Returns:
        A list of integers representing the peak calling hours for each unique city,
        sorted by the city ID in ascending order.

    Examples:
        >>> solve([[1, 5], [2, 6], [8, 10]], [1, 1, 2])
        [2, 1]
        >>> solve([[1, 10], [5, 15], [10, 20]], [1, 2, 1])
        [2, 1]
    """
    # Group intervals by city ID
    city_to_intervals: dict[int, list[list[int]]] = {}
    for i in range(len(intervals)):
        cid = city_ids[i]
        if cid not in city_to_intervals:
            city_to_intervals[cid] = []
        city_to_intervals[cid].append(intervals[i])

    # Sort city IDs to ensure the output follows ascending order
    sorted_cities = sorted(city_to_intervals.keys())
    results: list[int] = []

    for city in sorted_cities:
        # For each city, use a sweep-line algorithm to find max overlap
        events: list[tuple[int, int]] = []
        for start, end in city_to_intervals[city]:
            # Use +1 for start and -1 for end. 
            # To handle intervals that are inclusive [start, end], 
            # we treat the end as occurring slightly after the start.
            # If the problem implies [start, end] is inclusive, 
            # we process 'start' before 'end' at the same timestamp.
            events.append((start, 1))
            events.append((end, -1))

        # Sort events by time. If times are equal, process starts (1) before ends (-1)
        # to correctly count inclusive boundaries. However, standard sweep-line 
        # for intervals usually treats end as exclusive or handles ties specifically.
        # Given the context of "calling hours", we assume [start, end] is inclusive.
        # To handle inclusive intervals, we sort by time, then by type descending (1 before -1).
        events.sort(key=lambda x: (x[0], -x[1]))

        max_overlap = 0
        current_overlap = 0
        
        # Sweep through the sorted events
        for _, type_delta in events:
            current_overlap += type_delta
            if current_overlap > max_overlap:
                max_overlap = current_overlap
        
        results.append(max_overlap)

    return results
