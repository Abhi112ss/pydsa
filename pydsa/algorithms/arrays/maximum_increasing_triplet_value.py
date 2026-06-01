METADATA = {
    "id": 3073,
    "name": "Maximum Increasing Triplet Value",
    "slug": "maximum-increasing-triplet-value",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum value of (nums[i] * nums[j] * nums[k]) such that i < j < k and nums[i] < nums[j] < nums[k].",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum product of an increasing triplet in the array.

    The algorithm uses a greedy approach to maintain the smallest possible 
    first and second elements of a potential triplet. This maximizes the 
    potential for a third element to be larger and for the product to be maximized.

    Args:
        nums: A list of integers.

    Returns:
        The maximum product of an increasing triplet, or -1 if no such triplet exists.

    Examples:
        >>> solve([2, 5, 3, 4, 1])
        -1
        >>> solve([1, 2, 3, 4, 5])
        60
        >>> solve([10, 1, 2, 3, 10])
        60
    """
    # Initialize the smallest and second smallest elements to infinity
    first_min = float('inf')
    second_min = float('inf')
    max_product = -1

    for num in nums:
        if num <= first_min:
            # Found a new smallest element
            first_min = num
        elif num <= second_min:
            # Found an element larger than first_min but smaller than current second_min
            second_min = num
        else:
            # num is greater than both first_min and second_min, forming a triplet
            # Calculate product and update max_product
            current_product = first_min * second_min * num
            if current_product > max_product:
                max_product = int(current_product)

    return max_product
