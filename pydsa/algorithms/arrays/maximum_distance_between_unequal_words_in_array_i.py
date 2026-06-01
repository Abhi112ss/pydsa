METADATA = {
    "id": 3696,
    "name": "Maximum Distance Between Unequal Words in Array I",
    "slug": "maximum_distance_between_unequal_words_in_array_i",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the maximum absolute difference between indices of two unequal words in an array.",
}

def solve(words: list[str]) -> int:
    """
    Calculates the maximum distance between two indices i and j such that 
    words[i] is not equal to words[j].

    Args:
        words: A list of strings representing the input array.

    Returns:
        The maximum absolute difference |i - j| where words[i] != words[j].
        Returns 0 if no such pair exists.

    Examples:
        >>> solve(["a", "b", "a"])
        2
        >>> solve(["a", "a", "a"])
        0
        >>> solve(["a", "b", "c", "d"])
        3
    """
    n = len(words)
    max_distance = 0

    # Iterate through all possible pairs (i, j)
    # Since we want the maximum distance, we check every combination
    for i in range(n):
        for j in range(i + 1, n):
            # Check if the words at the current indices are unequal
            if words[i] != words[j]:
                # Calculate the distance and update the maximum found so far
                current_distance = j - i
                if current_distance > max_distance:
                    max_distance = current_distance

    return max_distance
