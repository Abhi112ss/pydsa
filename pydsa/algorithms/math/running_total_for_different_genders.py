METADATA = {
    "id": 1308,
    "name": "Running Total for Different Genders",
    "slug": "running_total_for_different_genders",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the running total of values partitioned by gender and ordered by date.",
}

def solve(entries: list[dict]) -> list[dict]:
    """
    Calculates the running total of values for each gender, ordered by date.

    Args:
        entries: A list of dictionaries, where each dictionary contains 
                 'gender' (str), 'date' (str), and 'value' (int).

    Returns:
        A list of dictionaries with the same keys, but including a 'running_total' 
        key representing the cumulative sum for that gender up to that date.

    Examples:
        >>> entries = [
        ...     {"gender": "M", "date": "2023-01-01", "value": 10},
        ...     {"gender": "F", "date": "2023-01-01", "value": 5},
        ...     {"gender": "M", "date": "2023-01-02", "value": 20}
        ... ]
        >>> solve(entries)
        [
            {"gender": "M", "date": "2023-01-01", "value": 10, "running_total": 10},
            {"gender": "F", "date": "2023-01-01", "value": 5, "running_total": 5},
            {"gender": "M", "date": "2023-01-02", "value": 20, "running_total": 30}
        ]
    """
    if not entries:
        return []

    # Sort entries primarily by gender and secondarily by date to ensure 
    # that when we iterate, we process all entries of one gender in chronological order.
    # This allows us to use a simple running sum per gender.
    sorted_entries = sorted(entries, key=lambda x: (x["gender"], x["date"]))

    # We need to keep track of the original order to return the results in the same order
    # as the input, or if the problem implies returning the sorted version.
    # Standard LeetCode behavior for "Running Total" usually implies returning 
    # the results corresponding to the input sequence.
    
    # To maintain original order while calculating prefix sums based on sorted logic:
    # 1. Map each entry to its sorted position or calculate sums using a dictionary.
    
    gender_running_sums = {}
    # We use a dictionary to store the cumulative sum for each gender encountered so far.
    # However, the running total is dependent on the chronological order within that gender.
    
    # Step 1: Sort a copy to calculate the prefix sums correctly.
    # We create a list of (original_index, entry) to reconstruct the list later.
    indexed_entries = []
    for index, entry in enumerate(entries):
        indexed_entries.append({
            "index": index,
            "gender": entry["gender"],
            "date": entry["date"],
            "value": entry["value"]
        })

    # Sort by gender then date
    indexed_entries.sort(key=lambda x: (x["gender"], x["date"]))

    # Step 2: Calculate running totals in the sorted order
    current_sums = {}
    for item in indexed_entries:
        gender = item["gender"]
        val = item["value"]
        
        # Update the cumulative sum for the specific gender
        current_sums[gender] = current_sums.get(gender, 0) + val
        item["running_total"] = current_sums[gender]

    # Step 3: Restore original order and format output
    indexed_entries.sort(key=lambda x: x["index"])
    
    result = []
    for item in indexed_entries:
        result.append({
            "gender": item["gender"],
            "date": item["date"],
            "value": item["value"],
            "running_total": item["running_total"]
        })

    return result
