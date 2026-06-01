METADATA = {
    "id": 2028,
    "name": "Find Missing Observations",
    "slug": "find-missing-observations",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given the observed counts of dice rolls, find the missing counts to reach the expected frequency for each face.",
}

def solve(observations: list[int], expected: list[int]) -> list[int]:
    """
    Calculates the missing observations required to match the expected counts.

    Args:
        observations: A list of integers representing the observed frequency of each face.
        expected: A list of integers representing the expected frequency of each face.

    Returns:
        A list of integers representing the missing observations for each face.

    Examples:
        >>> solve([1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2])
        [1, 1, 1, 1, 1, 1]
        >>> solve([1, 2, 3, 4, 5, 6], [2, 2, 2, 2, 2, 2])
        [1, 0, -1, -2, -3, -4]
    """
    # The problem asks for the difference between expected and observed.
    # Since the size of the dice faces is constant (usually 6), 
    # the space complexity is O(1).
    
    missing_counts = []
    
    # Iterate through the faces using the length of the expected list.
    # We assume observations and expected have the same length.
    for i in range(len(expected)):
        # The missing count is simply the target frequency minus what we saw.
        # If the result is negative, it means we observed more than expected.
        diff = expected[i] - observations[i]
        missing_counts.append(diff)
        
    return missing_counts
