METADATA = {
    "id": 3465,
    "name": "Find Products with Valid Serial Numbers",
    "slug": "find-products-with-valid-serial-numbers",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of valid product pairs based on specific serial number component frequency requirements.",
}

def solve(serial_numbers: list[int], target_sum: int) -> int:
    """
    Calculates the number of pairs of serial numbers that sum up to a target value.

    Args:
        serial_numbers: A list of integers representing product serial numbers.
        target_sum: The required sum for a valid product pair.

    Returns:
        The total count of pairs (i, j) such that i < j and serial_numbers[i] + serial_numbers[j] == target_sum.

    Examples:
        >>> solve([1, 2, 3, 4, 3], 6)
        2
        >>> solve([1, 1, 1, 1], 2)
        6
    """
    # frequency_map stores the count of each serial number encountered so far
    frequency_map: dict[int, int] = {}
    valid_pair_count: int = 0

    for current_number in serial_numbers:
        # Calculate the complement needed to reach the target_sum
        complement = target_sum - current_number

        # If the complement exists in our map, it means we found valid pairs
        if complement in frequency_map:
            valid_pair_count += frequency_map[complement]

        # Update the frequency of the current number for future pairs
        if current_number in frequency_map:
            frequency_map[current_number] += 1
        else:
            frequency_map[current_number] = 1

    return valid_pair_count
