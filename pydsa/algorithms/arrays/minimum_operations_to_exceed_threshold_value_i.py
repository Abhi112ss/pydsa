METADATA = {
    "id": 3065,
    "name": "Minimum Operations to Exceed Threshold Value I",
    "slug": "minimum-operations-to-exceed-threshold-value-i",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of elements needed from an array such that their sum is strictly greater than a given threshold.",
}

def solve(nums: list[int], threshold: int) -> int:
    """
    Calculates the minimum number of elements required to make their sum 
    strictly greater than the threshold.

    Args:
        nums: A list of integers representing the available values.
        threshold: The target value that the sum must exceed.

    Returns:
        The minimum number of elements needed to exceed the threshold.

    Examples:
        >>> solve([4, 5, 2, 1], 3)
        1
        >>> solve([1, 1, 1, 1], 2)
        3
    """
    # Sort the array in descending order to greedily pick the largest values first
    nums.sort(reverse=True)
    
    current_sum = 0
    count = 0
    
    for value in nums:
        current_sum += value
        count += 1
        
        # As soon as the sum exceeds the threshold, return the count
        if current_sum > threshold:
            return count
            
    return count
