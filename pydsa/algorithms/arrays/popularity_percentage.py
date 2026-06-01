METADATA = {
    "id": 2720,
    "name": "Popularity Percentage",
    "slug": "popularity_percentage",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the percentage of occurrences for each element in an array.",
}

def solve(nums: list[int]) -> dict[int, float]:
    """
    Calculates the popularity percentage for each unique element in the input list.

    The popularity percentage is defined as the number of occurrences of an 
    element divided by the total number of elements in the list, multiplied by 100.

    Args:
        nums: A list of integers representing the dataset.

    Returns:
        A dictionary where keys are the unique integers from the input list 
        and values are their corresponding popularity percentages as floats.

    Examples:
        >>> solve([1, 2, 2, 3, 3, 3])
        {1: 16.666666666666664, 2: 33.33333333333333, 3: 50.0}
        >>> solve([1, 1, 1, 1])
        {1: 100.0}
        >>> solve([])
        {}
    """
    if not nums:
        return {}

    total_count = len(nums)
    frequency_map: dict[int, int] = {}

    # Count the occurrences of each number using a hash map
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Calculate the percentage for each unique number
    popularity_map: dict[int, float] = {}
    for num, count in frequency_map.items():
        # Percentage = (count / total) * 100
        popularity_map[num] = (count / total_count) * 100

    return popularity_map
