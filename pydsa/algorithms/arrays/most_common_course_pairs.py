METADATA = {
    "id": 3764,
    "name": "Most Common Course Pairs",
    "slug": "most_common_course_pairs",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the most frequently occurring pair of courses in a given sequence.",
}

def solve(courses: list[int], k: int) -> list[int]:
    """
    Finds the most common pair of courses in a sequence of length k.

    Args:
        courses: A list of integers representing course IDs.
        k: The size of the window/sequence to consider for pairs.

    Returns:
        A list containing the two course IDs that form the most frequent pair.
        If multiple pairs have the same frequency, the one appearing first is returned.

    Examples:
        >>> solve([1, 2, 1, 2, 3], 2)
        [1, 2]
        >>> solve([1, 1, 2, 2, 1, 1], 2)
        [1, 1]
    """
    if not courses or k < 2:
        return []

    # Dictionary to store the frequency of each pair (tuple)
    pair_counts: dict[tuple[int, int], int] = {}
    
    # Track the first occurrence index to handle ties correctly if required
    # (Though standard problem interpretation usually implies first seen)
    max_frequency = 0
    most_common_pair = []

    # Iterate through the list to find all adjacent pairs
    # Note: The problem implies sliding window of size 2 or specific sequence pairs
    for i in range(len(courses) - 1):
        # Create a tuple representing the pair
        current_pair = (courses[i], courses[i + 1])
        
        # Update the frequency in the hash map
        pair_counts[current_pair] = pair_counts.get(current_pair, 0) + 1
        
        # Update the global maximum if this pair's frequency is higher
        # Using '>' ensures we keep the first pair encountered in case of ties
        if pair_counts[current_pair] > max_frequency:
            max_frequency = pair_counts[current_pair]
            most_common_pair = list(current_pair)

    return most_common_pair
