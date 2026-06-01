METADATA = {
    "id": 1964,
    "name": "Find the Longest Valid Obstacle Course at Each Position",
    "slug": "find-the-longest-valid-obstacle-course-at-each-position",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "binary_search"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest non-decreasing subsequence ending at each index of the given array.",
}

import bisect

def solve(obstacle_course: list[int]) -> list[int]:
    """
    Calculates the length of the longest valid obstacle course ending at each position.
    
    A valid obstacle course is a non-decreasing subsequence. This function uses
    the patience sorting algorithm (modified Longest Increasing Subsequence) 
    to find the length of the longest non-decreasing subsequence ending at each index.

    Args:
        obstacle_course: A list of integers representing the heights of obstacles.

    Returns:
        A list of integers where the i-th element is the length of the longest 
        valid obstacle course ending at index i.

    Examples:
        >>> solve([1, 2, 3, 4])
        [1, 2, 3, 4]
        >>> solve([3, 1, 5, 2, 4])
        [1, 1, 2, 2, 3]
        >>> solve([1, 1, 1, 1])
        [1, 2, 3, 4]
    """
    n = len(obstacle_course)
    if n == 0:
        return []

    # tails[i] will store the smallest ending element of a non-decreasing 
    # subsequence of length i + 1.
    tails: list[int] = []
    # result[i] stores the length of the longest non-decreasing subsequence ending at i.
    result: list[int] = [0] * n

    for index, height in enumerate(obstacle_course):
        # We use bisect_right because we want a non-decreasing subsequence.
        # bisect_right finds the first element strictly greater than 'height'.
        # This allows multiple elements of the same value to extend the sequence.
        insertion_point = bisect.bisect_right(tails, height)

        if insertion_point < len(tails):
            # If the height can replace an existing tail to make it smaller, do so.
            # This maintains the property that tails[i] is the smallest possible 
            # end element for a subsequence of length i+1.
            tails[insertion_point] = height
        else:
            # If the height is greater than or equal to all current tails,
            # it extends the longest subsequence found so far.
            tails.append(height)
        
        # The length of the longest non-decreasing subsequence ending at this 
        # specific index is the position in the tails array + 1.
        result[index] = insertion_point + 1

    return result
