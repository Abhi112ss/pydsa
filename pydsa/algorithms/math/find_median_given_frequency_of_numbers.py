METADATA = {
    "id": 571,
    "name": "Find Median Given Frequency of Numbers",
    "slug": "find-median-given-frequency-of-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the median of a dataset represented by values and their corresponding frequencies.",
}

def solve(values: list[int], frequencies: list[int]) -> float:
    """
    Calculates the median of a dataset given the values and their frequencies.

    The median is the middle value in a sorted list. If the total number of 
    elements is even, the median is the average of the two middle elements.

    Args:
        values: A list of integers representing the unique values in the dataset.
        frequencies: A list of integers representing the frequency of each value.

    Returns:
        The median of the dataset as a float.

    Examples:
        >>> solve([1, 2, 3], [1, 1, 1])
        2.0
        >>> solve([1, 2, 3], [1, 2, 1])
        2.0
        >>> solve([1, 2, 3], [1, 1, 2])
        2.5
    """
    if not values or not frequencies:
        return 0.0

    # Combine values and frequencies and sort by value to handle the dataset in order
    data = sorted(zip(values, frequencies))
    
    total_count = sum(frequencies)
    
    # Determine the target indices for the median
    # If total_count is odd, we need the element at index (total_count // 2)
    # If total_count is even, we need the average of (total_count // 2 - 1) and (total_count // 2)
    if total_count % 2 == 1:
        targets = [total_count // 2]
    else:
        targets = [total_count // 2 - 1, total_count // 2]

    median_values = []
    current_cumulative_count = 0
    target_idx = 0

    # Iterate through sorted values and track cumulative frequency
    for val, freq in data:
        start_range = current_cumulative_count
        end_range = current_cumulative_count + freq - 1
        
        # Check if any of our target indices fall within the current value's range
        while target_idx < len(targets) and targets[target_idx] <= end_range:
            # Since the values are sorted, if the target index is within this range,
            # the value at that index must be the current 'val'
            median_values.append(val)
            target_idx += 1
            
        current_cumulative_count += freq
        
        # Optimization: stop if we have found all required median elements
        if target_idx == len(targets):
            break

    return sum(median_values) / len(median_values)
