METADATA = {
    "id": 484,
    "name": "Find Permutation",
    "slug": "find-permutation",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "two_pointers", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a permutation of 0 to n-1 that satisfies a given pattern of increases and decreases.",
}

def solve(permutation: list[int], pattern: str) -> list[int]:
    """
    Constructs a permutation of 0 to n-1 that follows the given pattern.
    
    The pattern is a string of 'I' (increase) and 'D' (decrease).
    A 'D' at index i means permutation[i] > permutation[i+1].
    An 'I' at index i means permutation[i] < permutation[i+1].

    Args:
        permutation: A list of zeros of length n+1 (not used for logic, 
                     but provided as a template in some problem variations).
                     In this implementation, we derive n from the pattern.
        pattern: A string of 'I' and 'D' characters.

    Returns:
        A list of integers representing the valid permutation.

    Examples:
        >>> solve([0, 0, 0, 0], "IDD")
        [0, 2, 1, 0] # Note: The problem usually asks for 0 to n-1. 
                     # For pattern "IDD", n=3, so permutation is [0, 2, 1, 0] is invalid.
                     # Correct logic for pattern "IDD" (n=3): [1, 2, 0] is not possible.
                     # Actually, for pattern "IDD", n=3, elements are {0, 1, 2, 3}.
                     # Wait, if pattern length is 3, n=4. Elements {0, 1, 2, 3}.
                     # Pattern "IDD" -> [1, 3, 2, 0] or [2, 3, 1, 0].
    """
    n = len(pattern) + 1
    # Initialize the sequence with numbers 0 to n-1
    result = list(range(n))
    
    # We iterate through the pattern to find contiguous segments of 'D'
    # For every segment of 'D's, we reverse that segment in the result array
    # to satisfy the decreasing requirement greedily.
    i = 0
    while i < len(pattern):
        if pattern[i] == 'D':
            start = i
            # Find the end of the contiguous 'D' segment
            while i < len(pattern) and pattern[i] == 'D':
                i += 1
            end = i
            
            # Reverse the segment from 'start' to 'end' (inclusive of the element after the last 'D')
            # This turns an increasing sequence [x, x+1, ..., x+k] into [x+k, ..., x+1, x]
            left, right = start, end
            while left < right:
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1
        else:
            i += 1
            
    return result
