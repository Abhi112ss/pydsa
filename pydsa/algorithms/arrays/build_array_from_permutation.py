METADATA = {
    "id": 1920,
    "name": "Build Array from Permutation",
    "slug": "build-array-from-permutation",
    "category": "Array",
    "aliases": [],
    "tags": ["array_traversal", "permutation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Construct an array nums2 such that nums2[i] = nums[nums[i]] using constant extra space.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Constructs the array nums2 where nums2[i] = nums[nums[i]] in-place.

    Args:
        nums: A list of integers representing a permutation of 0 to n-1.

    Returns:
        The modified list representing the built array.

    Examples:
        >>> solve([0, 2, 1, 5, 3, 4])
        [0, 1, 2, 4, 5, 3]
        >>> solve([5, 0, 1, 2, 3, 4])
        [4, 5, 0, 1, 2, 3]
    """
    n = len(nums)

    # We use the encoding trick: nums[i] = nums[i] + (new_value % n) * n
    # This allows us to store two values in one index:
    # The original value is (nums[i] % n)
    # The new value is (nums[i] // n)
    for i in range(n):
        # The target value we want to place at index i is nums[nums[i]]
        # However, nums[nums[i]] might have already been encoded.
        # So we use % n to get the original value of nums[nums[i]].
        target_index = nums[i]
        new_value = nums[target_index] % n
        
        # Encode the new value into the current index
        nums[i] += new_value * n

    # Second pass: Decode the values by dividing by n
    for i in range(n):
        nums[i] //= n

    return nums
