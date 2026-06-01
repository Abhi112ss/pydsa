METADATA = {
    "id": 2012,
    "name": "Sum of Beauty in the Array",
    "slug": "sum-of-beauty-in-the-array",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of the difference between the maximum and minimum frequencies of elements in all possible subarrays.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of beauty for all subarrays of the given array.
    Beauty is defined as the difference between the maximum and minimum 
    frequencies of elements in a subarray.

    Args:
        nums: A list of integers.

    Returns:
        The total sum of beauty values for all subarrays.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        0
        >>> solve([1, 1, 2, 2, 2, 3])
        5
    """
    total_beauty = 0
    n = len(nums)

    # Iterate through every possible starting index of a subarray
    for start_index in range(n):
        # Frequency map for the current subarray starting at start_index
        # Since values are up to 100, a fixed-size array is more efficient than a dict
        frequencies = [0] * 101
        
        # Track max and min frequencies manually to avoid O(k) scan inside the loop
        # However, since the range of values is small (101), we can scan frequencies
        # to find max/min in O(1) relative to N.
        for end_index in range(start_index, n):
            val = nums[end_index]
            frequencies[val] += 1
            
            max_freq = 0
            min_freq = float('inf')
            
            # Scan the frequency array to find max and min frequencies
            # The range is constant (101), so this is O(1) per inner loop iteration
            for count in frequencies:
                if count > 0:
                    if count > max_freq:
                        max_freq = count
                    if count < min_freq:
                        min_freq = count
            
            # If min_freq was never updated (shouldn't happen if count > 0), handle it
            if min_freq == float('inf'):
                min_freq = 0
                
            total_beauty += (max_freq - min_freq)

    return total_beauty
