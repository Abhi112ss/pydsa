METADATA = {
    "id": 1122,
    "name": "Relative Sort Array",
    "slug": "relative-sort-array",
    "category": "Sorting",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Sort an array such that the relative ordering of the elements follows the order given in a second array, and remaining elements are sorted in ascending order.",
}

def solve(arr: list[int], rel: list[int]) -> list[int]:
    """
    Sorts the input array based on the relative order provided in the rel array.

    Args:
        arr: The input list of integers to be sorted.
        rel: The list of integers defining the required relative order.

    Returns:
        A new list containing the elements of arr sorted according to the rules.

    Examples:
        >>> solve([2, 3, 1, 1, 2, 4], [2, 1])
        [2, 2, 1, 1, 3, 4]
        >>> solve([1, 1, 2, 2, 3, 3], [1, 2, 3])
        [1, 1, 2, 2, 3, 3]
    """
    # Count the frequency of each element in the input array
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    result = []

    # First, add elements from 'rel' in the specified order
    for target in rel:
        if target in counts:
            # Append the element as many times as it appeared in the original array
            result.extend([target] * counts[target])
            # Remove from map to track which elements are "left over"
            del counts[target]

    # Collect all remaining elements that were not in 'rel'
    remaining_elements = []
    for num, count in counts.items():
        remaining_elements.extend([num] * count)

    # Sort the remaining elements in ascending order as per requirements
    remaining_elements.sort()
    
    # Combine the ordered elements with the sorted remaining elements
    result.extend(remaining_elements)

    return result
