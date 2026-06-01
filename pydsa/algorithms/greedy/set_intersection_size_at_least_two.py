METADATA = {
    "id": 757,
    "name": "Set Intersection Size At Least Two",
    "slug": "set-intersection-size-at-least-two",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of elements to pick from a collection of intervals such that each interval contains at least two picked elements.",
}

def solve(intervals: list[list[int]]) -> int:
    """
    Finds the minimum number of elements to pick such that each interval 
    contains at least two elements.

    The algorithm uses a greedy approach by sorting intervals by their end points.
    For each interval, we check how many elements have already been picked.
    If fewer than two are picked, we greedily pick elements from the end of 
    the current interval to maximize the chance of covering future intervals.

    Args:
        intervals: A list of intervals where intervals[i] = [start_i, end_i].

    Returns:
        The minimum number of elements required.

    Examples:
        >>> solve([[1, 3], [2, 5], [4, 6]])
        3
        >>> solve([[1, 2], [2, 3], [3, 4]])
        4
    """
    # Sort intervals by their end points to allow greedy selection from the end
    intervals.sort(key=lambda x: x[1])
    
    picked_elements = set()
    
    for start, end in intervals:
        # Count how many elements from the current interval are already in our set
        count = 0
        if start in picked_elements:
            count += 1
        if end in picked_elements:
            count += 1
            
        # If we don't have 2 elements yet, we need to add more
        if count == 0:
            # Case 1: No elements picked. Pick the last two elements of the interval.
            # This maximizes the overlap with subsequent intervals.
            picked_elements.add(end - 1)
            picked_elements.add(end)
        elif count == 1:
            # Case 2: Only one element picked. Pick the end element.
            # If the end element was already picked (start == end), this logic 
            # is handled by the count check, but since intervals are [start, end],
            # we pick the end element if it's not the one already picked.
            if end not in picked_elements:
                picked_elements.add(end)
            else:
                # If end was already picked, pick the element just before it
                picked_elements.add(end - 1)
                
    return len(picked_elements)
