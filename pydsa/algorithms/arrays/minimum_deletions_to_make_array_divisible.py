METADATA = {
    "id": 2344,
    "name": "Minimum Deletions to Make Array Divisible",
    "slug": "minimum-deletions-to-make-array-divisible",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of deletions required to make all remaining elements in an array divisible by a given integer.",
}

def solve(nums: list[int], divisor: int) -> int:
    """
    Calculates the minimum number of deletions needed so that all remaining 
    elements in the array are divisible by the given divisor.

    Args:
        nums: A list of integers.
        divisor: The integer that all remaining elements must be divisible by.

    Returns:
        The total count of elements that are not divisible by the divisor.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        3
        >>> solve([10, 5, 2, 1], 5)
        2
    """
    deletions_count = 0
    
    # Iterate through each number in the array
    for number in nums:
        # If the number is not divisible by the divisor, it must be deleted
        if number % divisor != 0:
            deletions_count += 1
            
    return deletions_count
