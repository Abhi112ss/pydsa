METADATA = {
    "id": 3005,
    "name": "Count Elements With Maximum Frequency",
    "slug": "count-elements-with-maximum-frequency",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the total frequency of all elements that appear with the maximum frequency in the array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of frequencies of all elements that have the maximum frequency.

    Args:
        nums: A list of integers.

    Returns:
        The total count of elements that share the maximum frequency found in the list.

    Examples:
        >>> solve([1, 2, 2, 3, 1, 4])
        4
        >>> solve([1, 2, 3, 4, 5])
        5
        >>> solve([1, 1, 1, 1])
        4
    """
    if not nums:
        return 0

    # Step 1: Count the frequency of each element using a hash map
    frequency_map: dict[int, int] = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Step 2: Find the maximum frequency present in the map
    max_frequency: int = 0
    for count in frequency_map.values():
        if count > max_frequency:
            max_frequency = count

    # Step 3: Sum the frequencies of all elements that match the max_frequency
    total_max_frequency_count: int = 0
    for count in frequency_map.values():
        if count == max_frequency:
            total_max_frequency_count += count

    return total_max_frequency_count
