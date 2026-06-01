METADATA = {
    "id": 3068,
    "name": "Find the Maximum Sum of Node Values",
    "slug": "find-the-maximum-sum-of-node-values",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the sum of node values given that the sum of any two adjacent nodes must be strictly greater than a given threshold.",
}

def solve(nums: list[int], threshold: int) -> int:
    """
    Calculates the maximum possible sum of node values such that the sum 
    of any two adjacent nodes is strictly greater than the threshold.

    The strategy is to sort the array and greedily pair the largest available 
    numbers with the smallest possible numbers that satisfy the condition. 
    By pairing a large number with a small number, we 'save' other large 
    numbers to potentially pair with other small numbers, maximizing the 
    total sum of the selected pairs.

    Args:
        nums: A list of integers representing the values of the nodes.
        threshold: An integer representing the minimum sum required for 
            any two adjacent nodes.

    Returns:
        The maximum sum of the selected node values.

    Examples:
        >>> solve([2, 5, 1, 3, 4], 5)
        12
        >>> solve([1, 2, 3, 4, 5], 4)
        12
    """
    # Sort the numbers to allow for a two-pointer greedy approach
    nums.sort()
    
    n = len(nums)
    total_sum = 0
    left = 0
    right = n - 1
    
    # We use two pointers to pick pairs. 
    # We want to pick the largest available number (right) and pair it 
    # with the smallest possible number (left) that satisfies the threshold.
    while left < right:
        # Check if the current smallest and largest satisfy the condition
        if nums[left] + nums[right] > threshold:
            # If they do, they form a valid pair. 
            # We add both to the sum and move both pointers.
            total_sum += nums[left] + nums[right]
            left += 1
            right -= 1
        else:
            # If the smallest + largest is not enough, the smallest number 
            # cannot be part of any valid pair with the remaining numbers.
            # We skip this smallest number.
            left += 1
            
    return total_sum
