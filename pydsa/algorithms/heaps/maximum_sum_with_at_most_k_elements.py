METADATA = {
    "id": 3462,
    "name": "Maximum Sum With at Most K Elements",
    "slug": "maximum-sum-with-at-most-k-elements",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "heap", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum possible by choosing at most k elements from the given array.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum sum possible by selecting at most k elements from the array.
    
    To maximize the sum, we should greedily pick the largest positive numbers 
    available in the array, up to a maximum of k elements.

    Args:
        nums: A list of integers.
        k: The maximum number of elements that can be selected.

    Returns:
        The maximum sum of at most k elements.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        12
        >>> solve([-1, -2, -3], 2)
        0
        >>> solve([10, -5, 20, 0], 1)
        20
    """
    # Sort the array in descending order to access largest elements first
    nums.sort(reverse=True)
    
    max_sum = 0
    count = 0
    
    # Iterate through the sorted list and pick elements as long as 
    # they are positive and we haven't exceeded the limit k
    for value in nums:
        if count < k and value > 0:
            max_sum += value
            count += 1
        else:
            # Since the list is sorted descending, if we hit a non-positive 
            # number or reach k, we can stop early.
            break
            
    return max_sum
