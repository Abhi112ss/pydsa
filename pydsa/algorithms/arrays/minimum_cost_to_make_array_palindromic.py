METADATA = {
    "id": 2967,
    "name": "Minimum Cost to Make Array Palindromic",
    "slug": "minimum-cost-to-make-array-palindromic",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum cost to make an array palindromic by summing the absolute differences of symmetric elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum cost to make the given array a palindrome.
    
    The cost to make two elements equal is the absolute difference between them.
    To minimize the total cost, we pair elements from the start and end of the 
    array and sum their absolute differences.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The minimum total cost to make the array palindromic.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        6
        # |1-5| + |2-4| = 4 + 2 = 6
        
        >>> solve([1, 2, 3, 2, 1])
        0
        # |1-1| + |2-2| = 0
    """
    total_cost = 0
    left_index = 0
    right_index = len(nums) - 1

    # Iterate from both ends towards the center
    while left_index < right_index:
        # The cost to make nums[left] and nums[right] equal is |nums[left] - nums[right]|
        total_cost += abs(nums[left_index] - nums[right_index])
        
        # Move pointers closer to the middle
        left_index += 1
        right_index -= 1

    return total_cost
