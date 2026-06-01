METADATA = {
    "id": 713,
    "name": "Subarray Product Less Than K",
    "slug": "subarray-product-less-than-k",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the number of contiguous subarrays where the product of all elements in the subarray is strictly less than k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of contiguous subarrays whose product is strictly less than k.

    Args:
        nums: A list of positive integers.
        k: The threshold value for the product.

    Returns:
        The total count of subarrays with a product less than k.

    Examples:
        >>> solve([10, 5, 2, 6], 100)
        8
        >>> solve([1, 2, 3], 0)
        0
    """
    # If k is 0 or 1, no product of positive integers can be strictly less than k
    if k <= 1:
        return 0

    total_count = 0
    current_product = 1
    left_pointer = 0

    # Iterate through the array using a right pointer to expand the window
    for right_pointer in range(len(nums)):
        current_product *= nums[right_pointer]

        # If the product exceeds or equals k, shrink the window from the left
        while current_product >= k and left_pointer <= right_pointer:
            current_product //= nums[left_pointer]
            left_pointer += 1

        # The number of new valid subarrays ending at right_pointer is 
        # equal to the length of the current valid window (right - left + 1)
        total_count += (right_pointer - left_pointer + 1)

    return total_count
