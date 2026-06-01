METADATA = {
    "id": 2574,
    "name": "Left and Right Sum Differences",
    "slug": "left-and-right-sum-differences",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the absolute difference between the sum of elements to the left and the sum of elements to the right for every index in an array.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Calculates the absolute difference between the left and right sums for each index.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers where each element at index i is |sum(nums[0...i-1]) - sum(nums[i+1...n-1])|.

    Examples:
        >>> solve([10, 4, -2, 5, 6])
        [13, 9, 15, 11, 10]
        >>> solve([1, 2, 3])
        [5, 1, 3]
    """
    n = len(nums)
    # Calculate the total sum of the array to derive right sums in O(1)
    total_sum = sum(nums)
    
    results = []
    left_sum = 0
    
    for i in range(n):
        # The right sum is the total sum minus the current element and the left sum
        right_sum = total_sum - left_sum - nums[i]
        
        # Append the absolute difference to the results
        results.append(abs(left_sum - right_sum))
        
        # Update the running left sum for the next iteration
        left_sum += nums[i]
        
    return results
