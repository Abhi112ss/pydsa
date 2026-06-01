METADATA = {
    "id": 3139,
    "name": "Minimum Cost to Equalize Array",
    "slug": "minimum-cost-to-equalize-array",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum cost to make all elements in an array equal by adding or subtracting values.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum cost to make all elements in the array equal.
    
    The cost to change an element x to a target value T is |x - T|.
    To minimize the sum of absolute differences (sum |x_i - T|), 
    the optimal target value T is the median of the array.

    Args:
        nums: A list of integers.

    Returns:
        The minimum total cost as an integer.

    Examples:
        >>> solve([1, 2, 3])
        2
        >>> solve([1, 10, 100])
        99
    """
    # Sort the array to find the median efficiently
    # Sorting takes O(n log n) time
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    
    # The median is the middle element in a sorted list.
    # For even lengths, any value between the two middle elements works;
    # we pick the one at index n // 2 for simplicity.
    median = sorted_nums[n // 2]
    
    total_cost = 0
    # Calculate the sum of absolute differences from the median
    for num in sorted_nums:
        total_cost += abs(num - median)
        
    return total_cost
