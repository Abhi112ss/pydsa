METADATA = {
    "id": 3209,
    "name": "Number of Subarrays With AND Value of K",
    "slug": "number-of-subarrays-with-and-value-of-k",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "bit_manipulation", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(log(max_val))",
    "description": "Count the number of subarrays where the bitwise AND of all elements equals k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays whose bitwise AND result is exactly k.

    The algorithm uses a frequency map to track all possible bitwise AND results 
    ending at the current index. Since bitwise AND is a monotonic decreasing 
    operation (adding an element can only turn bits from 1 to 0), there are at 
    most log2(max(nums)) distinct AND values ending at any given position.

    Args:
        nums: A list of integers.
        k: The target bitwise AND value.

    Returns:
        The total count of subarrays with bitwise AND equal to k.

    Examples:
        >>> solve([1, 1, 1], 1)
        6
        >>> solve([1, 2, 3], 2)
        1
    """
    total_count = 0
    # current_and_counts maps: {bitwise_and_value: frequency_of_subarrays_ending_at_prev_index}
    current_and_counts: dict[int, int] = {}

    for num in nums:
        # next_and_counts will store the AND results of subarrays ending at the current index
        next_and_counts: dict[int, int] = {}
        
        # Case 1: The subarray consisting of only the current element
        next_and_counts[num] = next_and_counts.get(num, 0) + 1
        
        # Case 2: Extend all subarrays ending at the previous index with the current element
        for prev_and_val, count in current_and_counts.items():
            new_and_val = prev_and_val & num
            next_and_counts[new_and_val] = next_and_counts.get(new_and_val, 0) + count
            
        # If the target k is found in the current set of AND results, add its frequency to total
        if k in next_and_counts:
            total_count += next_and_counts[k]
            
        # Move to the next element
        current_and_counts = next_and_counts

    return total_count
