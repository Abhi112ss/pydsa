METADATA = {
    "id": 3194,
    "name": "Minimum Average of Smallest and Largest Elements",
    "slug": "minimum-average-of-smallest-and-largest-elements",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum average of the smallest and largest elements after repeatedly removing them from the array.",
}

def solve(nums: list[int]) -> float:
    """
    Calculates the minimum average of the smallest and largest elements 
    by repeatedly removing them from the array.

    Args:
        nums: A list of integers representing the elements in the array.

    Returns:
        The minimum average found during the process as a float.

    Examples:
        >>> solve([1, 1, 1, 2, 2, 3, 3, 5])
        2.0
        >>> solve([1, 1, 1, 1])
        1.0
    """
    # Sort the array to easily access smallest and largest elements
    nums.sort()
    
    left_index = 0
    right_index = len(nums) - 1
    min_average = float('inf')
    
    # Use two pointers to simulate the removal of smallest and largest elements
    while left_index < right_index:
        # Calculate the average of the current smallest and largest
        current_average = (nums[left_index] + nums[right_index]) / 2.0
        
        # Update the minimum average found so far
        if current_average < min_average:
            min_average = current_average
            
        # Move pointers inward to simulate removal
        left_index += 1
        right_index -= 1
        
    return min_average
