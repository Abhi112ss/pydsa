METADATA = {
    "id": 3445,
    "name": "Maximum Difference Between Even and Odd Frequency II",
    "slug": "maximum-difference-between-even-and-odd-frequency-ii",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the maximum possible difference between an even frequency and an odd frequency in a given array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum difference between an even frequency and an odd frequency.

    The difference is defined as (even_frequency - odd_frequency). To maximize this,
    we need to find the maximum even frequency and the minimum odd frequency.

    Args:
        nums: A list of integers.

    Returns:
        The maximum difference (max_even_freq - min_odd_freq). 
        If no even or no odd frequencies exist, the behavior depends on problem constraints,
        but typically we return a value indicating impossibility or 0. 
        Based on the problem logic, we return the max difference.

    Examples:
        >>> solve([1, 1, 2, 2, 2, 3, 3, 3, 3])
        # Frequencies: 1:2 (even), 2:3 (odd), 3:4 (even)
        # Max even: 4, Min odd: 3. Result: 4 - 3 = 1
        1
    """
    if not nums:
        return 0

    # Step 1: Count frequencies of each number
    frequency_map: dict[int, int] = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Initialize trackers for max even and min odd frequencies
    # Using float('inf') and float('-inf') for easy comparison
    max_even_freq: float = float('-inf')
    min_odd_freq: float = float('inf')

    # Step 2: Iterate through frequencies to find max even and min odd
    for freq in frequency_map.values():
        if freq % 2 == 0:
            # Update maximum even frequency found so far
            if freq > max_even_freq:
                max_even_freq = float(freq)
        else:
            # Update minimum odd frequency found so far
            if freq < min_odd_freq:
                min_odd_freq = float(freq)

    # Step 3: Calculate the difference
    # If either group is empty, the problem constraints usually imply 
    # we cannot form a difference. We return 0 or a specific indicator.
    if max_even_freq == float('-inf') or min_odd_freq == float('inf'):
        return 0

    return int(max_even_freq - min_odd_freq)
