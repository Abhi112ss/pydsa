METADATA = {
    "id": 354,
    "name": "Russian Doll Envelopes",
    "slug": "russian-doll-envelopes",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["binary_search", "dynamic_programming", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of envelopes that can be nested inside each other.",
}

import bisect

def solve(envelopes: list[list[int]]) -> int:
    """
    Calculates the maximum number of envelopes that can be nested.
    
    The problem is reduced to a 2D version of the Longest Increasing Subsequence (LIS).
    By sorting width in ascending order and height in descending order for the same width,
    we ensure that we cannot pick two envelopes with the same width (since the heights 
    will be in decreasing order, preventing an increasing subsequence). 
    Then, we simply find the LIS of the heights.

    Args:
        envelopes: A list of lists where each inner list contains [width, height].

    Returns:
        The maximum number of nested envelopes.

    Examples:
        >>> solve([[5,4],[6,4],[6,7],[2,3]])
        2
        >>> solve([[1,1],[1,1],[1,1]])
        1
    """
    if not envelopes:
        return 0

    # Sort width ascending. 
    # For same width, sort height descending to avoid picking multiple envelopes 
    # of the same width in the LIS calculation.
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    # Extract heights to perform standard 1D LIS
    heights = [env[1] for env in envelopes]
    
    # tails[i] will store the smallest tail of all increasing subsequences of length i+1
    tails: list[int] = []

    for height in heights:
        # Find the insertion point to maintain sorted order in tails
        # bisect_left finds the first element >= height
        idx = bisect.bisect_left(tails, height)
        
        if idx == len(tails):
            # If height is larger than any tail, it extends the longest subsequence
            tails.append(height)
        else:
            # Otherwise, replace the existing tail to keep it as small as possible
            # This increases the potential for future elements to extend the sequence
            tails[idx] = height

    return len(tails)
