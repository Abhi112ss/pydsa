METADATA = {
    "id": 3917,
    "name": "Count Indices With Opposite Parity",
    "slug": "count_indices_with_opposite_parity",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "parity"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of indices where the parity of the index is different from the parity of the element at that index.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of indices i such that nums[i] % 2 != i % 2.

    Args:
        nums: A list of integers.

    Returns:
        The count of indices where the parity of the element 
        is different from the parity of the index.

    Examples:
        >>> solve([2, 3, 4, 5])
        4
        >>> solve([1, 2, 3, 4])
        0
        >>> solve([1, 1, 1])
        1
    """
    opposite_parity_count = 0
    
    # Iterate through the array using enumerate to get both index and value
    for index, value in enumerate(nums):
        # Check if the parity of the index (index % 2) 
        # is not equal to the parity of the value (value % 2)
        if (index % 2) != (value % 2):
            opposite_parity_count += 1
            
    return opposite_parity_count
