METADATA = {
    "id": 3444,
    "name": "Minimum Increments for Target Multiples in an Array",
    "slug": "minimum-increments-for-target-multiples-in-an-array",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of increments needed to make every element in an array a multiple of its index (1-indexed).",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of increments required to make each element 
    at index i (1-indexed) a multiple of i.

    Args:
        nums: A list of integers.

    Returns:
        The total number of increments needed.

    Examples:
        >>> solve([1, 2, 3, 4])
        0
        >>> solve([1, 1, 1, 1])
        4
        >>> solve([3, 3, 3, 3])
        2
    """
    total_increments = 0
    
    # Iterate through the array using 1-based indexing for the target multiple
    for index_minus_one, value in enumerate(nums):
        target_multiple = index_minus_one + 1
        
        # Calculate the remainder when the current value is divided by the target multiple
        remainder = value % target_multiple
        
        if remainder != 0:
            # The amount needed to reach the next multiple is (target - remainder)
            # This is the greedy choice to minimize increments for this specific element
            needed = target_multiple - remainder
            total_increments += needed
            
    return total_increments
