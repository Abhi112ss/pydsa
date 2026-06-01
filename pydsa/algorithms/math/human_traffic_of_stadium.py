METADATA = {
    "id": 601,
    "name": "Human Traffic of Stadium",
    "slug": "human-traffic-of-stadium",
    "category": "Database/Algorithm",
    "aliases": [],
    "tags": ["window_function", "consecutive_values", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all rows where the value is greater than or equal to 100 and is part of a sequence of at least 3 consecutive rows with values >= 100.",
}

def solve(traffic_data: list[dict]) -> list[dict]:
    """
    Finds all rows where the value is >= 100 and is part of a sequence 
    of at least 3 consecutive rows with values >= 100.

    Args:
        traffic_data: A list of dictionaries, where each dictionary represents 
                      a row with 'day' (int) and 'traffic' (int) keys.
                      The input is assumed to be sorted by 'day'.

    Returns:
        A list of dictionaries containing the rows that meet the criteria,
        sorted by 'day'.

    Examples:
        >>> data = [
        ...     {"day": 1, "traffic": 10}, {"day": 2, "traffic": 100},
        ...     {"day": 3, "traffic": 105}, {"day": 4, "traffic": 110},
        ...     {"day": 5, "traffic": 50}, {"day": 6, "traffic": 120}
        ... ]
        >>> solve(data)
        [{'day': 2, 'traffic': 100}, {'day': 3, 'traffic': 105}, {'day': 4, 'traffic': 110}]
    """
    if not traffic_data:
        return []

    # Sort data by day to ensure we are checking consecutive temporal sequences
    sorted_data = sorted(traffic_data, key=lambda x: x["day"])
    n = len(sorted_data)
    
    # result_indices will store the indices of rows that satisfy the condition
    result_indices = set()
    
    # We use a sliding window/counter approach to find contiguous blocks
    # of rows where traffic >= 100 and days are consecutive.
    i = 0
    while i < n:
        if sorted_data[i]["traffic"] >= 100:
            start_index = i
            # Expand the window as long as traffic is >= 100 and days are consecutive
            while (i + 1 < n and 
                   sorted_data[i + 1]["traffic"] >= 100 and 
                   sorted_data[i + 1]["day"] == sorted_data[i]["day"] + 1):
                i += 1
            
            end_index = i
            # Check if the length of the current contiguous block is at least 3
            if (end_index - start_index + 1) >= 3:
                for idx in range(start_index, end_index + 1):
                    result_indices.add(idx)
        i += 1

    # Construct the final list from the identified indices
    final_result = [sorted_data[idx] for idx in sorted(list(result_indices))]
    return final_result
