METADATA = {
    "id": 2357,
    "name": "Make Array Zero by Subtracting Equal Amounts",
    "slug": "make-array-zero-by-subtracting-equal-amounts",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the number of operations required to make all elements in an array zero by repeatedly subtracting the minimum non-zero element from all non-zero elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of operations to make all elements in the array zero.
    
    The core insight is that in each operation, we subtract the current minimum 
    non-zero value from all non-zero elements. This effectively removes one 
    unique non-zero value from the set of values in the array per operation.
    Therefore, the total number of operations is equal to the count of 
    unique positive integers in the array.

    Args:
        nums: A list of integers.

    Returns:
        The total number of operations required to make all elements zero.

    Examples:
        >>> solve([1, 3, 5])
        3
        >>> solve([2, 1, 3, 0, 1, 2])
        3
        >>> solve([0, 0, 0])
        0
    """
    # Use a set to find all unique elements in the array
    unique_elements = set(nums)
    
    # Remove 0 from the set if it exists, as 0 does not require an operation
    if 0 in unique_elements:
        unique_elements.remove(0)
        
    # The number of operations is the count of unique non-zero elements
    return len(unique_elements)
