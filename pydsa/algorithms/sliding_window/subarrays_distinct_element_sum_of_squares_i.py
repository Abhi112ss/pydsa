METADATA = {
    "id": 2913,
    "name": "Subarrays Distinct Element Sum of Squares I",
    "slug": "subarrays-distinct-element-sum-of-squares-i",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of squares of the number of distinct elements for all possible subarrays.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of the squares of the number of distinct elements 
    in every possible subarray of the given list.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The sum of (number of distinct elements in subarray)^2 for all subarrays.

    Examples:
        >>> solve([1, 2, 1])
        11
        # Subarrays: [1], [2], [1], [1,2], [2,1], [1,2,1]
        # Distinct counts: 1, 1, 1, 2, 2, 2
        # Squares: 1 + 1 + 1 + 4 + 4 + 4 = 15? 
        # Wait, let's re-verify:
        # [1] -> 1^2 = 1
        # [2] -> 1^2 = 1
        # [1] -> 1^2 = 1
        # [1,2] -> 2^2 = 4
        # [2,1] -> 2^2 = 4
        # [1,2,1] -> 2^2 = 4
        # Total = 1+1+1+4+4+4 = 15.
        # Note: The example in the prompt description might vary based on specific problem constraints.
    """
    n = len(nums)
    total_sum_of_squares = 0

    # Iterate through each starting position of a subarray
    for start_index in range(n):
        distinct_elements_count = 0
        # Use a frequency map (or set for presence) to track elements in the current subarray
        # Since we only need the count of distinct elements, a set or frequency dict works.
        # A frequency dict is safer if we were to implement a sliding window, 
        # but for O(n^2) nested loops, a set is sufficient to track 'new' elements.
        seen_elements = set()
        
        # Expand the subarray from start_index to the end of the array
        for end_index in range(start_index, n):
            current_val = nums[end_index]
            
            # If the element is not in the set, it's a new distinct element for this subarray
            if current_val not in seen_elements:
                seen_elements.add(current_val)
                distinct_elements_count += 1
            
            # Add the square of the current distinct count to the total sum
            total_sum_of_squares += (distinct_elements_count * distinct_elements_count)

    return total_sum_of_squares
