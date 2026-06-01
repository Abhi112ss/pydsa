METADATA = {
    "id": 1405,
    "name": "Longest Happy String",
    "slug": "longest-happy-string",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Construct the longest possible string using characters 'a', 'b', and 'c' such that no three consecutive characters are the same.",
}

import heapq

def solve(a: int, b: int, c: int) -> str:
    """
    Constructs the longest happy string using a greedy approach with a max-heap.

    Args:
        a: The maximum number of 'a' characters available.
        b: The maximum number of 'b' characters available.
        c: The maximum number of 'c' characters available.

    Returns:
        The longest happy string possible.

    Examples:
        >>> solve(1, 1, 1)
        'abc'
        >>> solve(7, 1, 0)
        'aabaa'
        >>> solve(2, 2, 1)
        'aabbc'
    """
    # Use a max-heap to always pick the character with the highest remaining count.
    # Python's heapq is a min-heap, so we store negative counts to simulate a max-heap.
    max_heap = []
    for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
        if count > 0:
            heapq.heappush(max_heap, (-count, char))

    result_chars = []

    while max_heap:
        count1, char1 = heapq.heappop(max_heap)
        count1 = -count1  # Convert back to positive

        # Check if adding char1 would violate the "no three consecutive" rule
        if len(result_chars) >= 2 and result_chars[-1] == char1 and result_chars[-2] == char1:
            if not max_heap:
                # No other character available to break the streak
                break
            
            # Pick the second most frequent character to break the streak
            count2, char2 = heapq.heappop(max_heap)
            count2 = -count2
            
            result_chars.append(char2)
            count2 -= 1
            
            # If the second character still has remaining counts, put it back
            if count2 > 0:
                heapq.heappush(max_heap, (-count2, char2))
            
            # Put the first character back to be used in the next iteration
            heapq.heappush(max_heap, (-count1, char1))
        else:
            # It is safe to use the most frequent character
            result_chars.append(char1)
            count1 -= 1
            
            if count1 > 0:
                heapq.heappush(max_heap, (-count1, char1))

    return "".join(result_chars)
