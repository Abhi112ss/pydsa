METADATA = {
    "id": 2404,
    "name": "Most Frequent Even Element",
    "slug": "most-frequent-even-element",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the most frequent even element in an array, returning the smallest one in case of ties.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the most frequent even element in the given list. 
    If multiple even elements have the same maximum frequency, returns the smallest one.

    Args:
        nums: A list of integers.

    Returns:
        The most frequent even integer. Returns -1 if no even integer exists.

    Examples:
        >>> solve([4, 4, 2, 2, 2, 1])
        2
        >>> solve([1, 3, 5])
        -1
        >>> solve([2, 2, 4, 4])
        2
    """
    # Frequency map to store counts of even numbers only
    even_counts: dict[int, int] = {}
    
    for num in nums:
        if num % 2 == 0:
            even_counts[num] = even_counts.get(num, 0) + 1
            
    if not even_counts:
        return -1
    
    max_frequency = -1
    result_element = float('inf')
    
    # Iterate through the map to find the element with max frequency
    # In case of tie in frequency, pick the smallest element
    for element, count in even_counts.items():
        if count > max_frequency:
            max_frequency = count
            result_element = element
        elif count == max_frequency:
            if element < result_element:
                result_element = element
                
    return int(result_element)
