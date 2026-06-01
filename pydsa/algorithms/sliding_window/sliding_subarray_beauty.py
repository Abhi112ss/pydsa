METADATA = {
    "id": 2653,
    "name": "Sliding Subarray Beauty",
    "slug": "sliding-subarray-beauty",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "frequency_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n * 26)",
    "space_complexity": "O(1)",
    "description": "Find the sum of the smallest integer in each subarray of size k that is greater than zero.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the sum of the smallest positive integer in every sliding window of size k.

    Args:
        nums: A list of integers representing the input array.
        k: The size of the sliding window.

    Returns:
        The sum of the smallest positive integers (1-25) in each window.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        4
        >>> solve([3, 1, 2, 4, 5], 3)
        3
    """
    # Since the problem constraints state nums[i] is between 1 and 26,
    # we can use a fixed-size frequency array of size 27.
    # index 0 is unused, indices 1-26 store counts of those numbers.
    frequency = [0] * 27
    total_beauty_sum = 0

    for i in range(len(nums)):
        # Add the current element to the frequency map
        frequency[nums[i]] += 1

        # Once the window reaches size k, start processing
        if i >= k - 1:
            # Find the smallest integer > 0 in the current window
            # We only need to check up to 26 because of problem constraints
            for val in range(1, 27):
                if frequency[val] > 0:
                    total_beauty_sum += val
                    break
            
            # Remove the element that is sliding out of the window
            # The element to remove is at index (i - k + 1)
            out_of_bounds_val = nums[i - k + 1]
            frequency[out_of_bounds_val] -= 1

    return total_beauty_sum
