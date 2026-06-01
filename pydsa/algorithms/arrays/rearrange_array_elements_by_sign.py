METADATA = {
    "id": 2149,
    "name": "Rearrange Array Elements by Sign",
    "slug": "rearrange-array-elements-by-sign",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Rearrange an array of even length containing an equal number of positive and negative integers such that they alternate signs starting with a positive integer.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Rearranges the input array so that positive and negative integers alternate,
    starting with a positive integer at index 0.

    The input array is guaranteed to have an equal number of positive and 
    negative integers and an even length.

    Args:
        nums: A list of integers containing an equal number of positive 
              and negative values.

    Returns:
        A new list of integers where positive and negative numbers alternate.

    Examples:
        >>> solve([3, 1, -2, -5, 2, -4])
        [3, -2, 1, -5, 2, -4]
        >>> solve([-2, 1])
        [1, -2]
    """
    n = len(nums)
    # Initialize the result array with zeros to pre-allocate space
    result = [0] * n
    
    # Pointers for the next available positive and negative positions
    # Positive numbers go to even indices (0, 2, 4...)
    # Negative numbers go to odd indices (1, 3, 5...)
    positive_idx = 0
    negative_idx = 1

    for num in nums:
        if num > 0:
            # Place positive number at the current even index and move pointer
            result[positive_idx] = num
            positive_idx += 2
        else:
            # Place negative number at the current odd index and move pointer
            result[negative_idx] = num
            negative_idx += 2

    return result
