METADATA = {
    "id": 3819,
    "name": "Rotate Non Negative Elements",
    "slug": "rotate_non_negative_elements",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Rotate only the non-negative elements of an array to the right by k positions while maintaining their relative order and keeping negative elements in their original positions.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Rotates non-negative elements in the array to the right by k positions.

    The relative order of non-negative elements is preserved, and negative 
    elements remain in their original indices.

    Args:
        nums: A list of integers containing both positive/zero and negative values.
        k: The number of positions to rotate the non-negative elements.

    Returns:
        The modified list with non-negative elements rotated.

    Examples:
        >>> solve([1, -2, 3, -4, 5], 1)
        [5, -2, 1, -4, 3]
        >>> solve([0, -1, 2, -3, 4], 2)
        [2, -1, 4, -3, 0]
    """
    # Extract indices and values of all non-negative elements
    non_negative_indices = []
    non_negative_values = []
    
    for index, value in enumerate(nums):
        if value >= 0:
            non_negative_indices.append(index)
            non_negative_values.append(value)
            
    if not non_negative_indices:
        return nums
        
    n_non_neg = len(non_negative_indices)
    # Normalize k to handle cases where k >= number of non-negative elements
    k = k % n_non_neg
    
    # If k is 0, no rotation is needed
    if k == 0:
        return nums

    # Create a temporary list for the rotated non-negative values
    # We use the property that the element at index i moves to (i + k) % n
    rotated_values = [0] * n_non_neg
    for i in range(n_non_neg):
        rotated_values[(i + k) % n_non_neg] = non_negative_values[i]
        
    # Place the rotated values back into the original array at the saved indices
    for i in range(n_non_neg):
        target_index = non_negative_indices[i]
        nums[target_index] = rotated_values[i]
        
    return nums
