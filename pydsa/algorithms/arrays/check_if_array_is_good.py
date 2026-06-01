METADATA = {
    "id": 2784,
    "name": "Check if Array is Good",
    "slug": "check-if-array-is-good",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array is 'good' by checking if its sorted version matches the sequence 0, 1, 2, ..., n-1.",
}

def solve(nums: list[int]) -> bool:
    """
    Checks if the given array is 'good'. An array is good if, when sorted, 
    it contains all integers from 0 to n-1.

    Args:
        nums: A list of integers.

    Returns:
        True if the array is good, False otherwise.

    Examples:
        >>> solve([3, 2, 1, 0])
        True
        >>> solve([1, 0])
        True
        >>> solve([1, 1])
        False
    """
    # A 'good' array of size n must contain exactly the elements 0, 1, ..., n-1.
    # Sorting the array allows us to check this property in linear time after the sort.
    nums.sort()
    
    for index in range(len(nums)):
        # After sorting, the element at each index must equal the index itself.
        if nums[index] != index:
            return False
            
    return True
