METADATA = {
    "id": 4,
    "name": "Median of Two Sorted Arrays",
    "slug": "median-of-two-sorted-arrays",
    "category": "Hard",
    "aliases": [],
    "tags": ["binary_search", "divide_and_conquer", "array"],
    "difficulty": "hard",
    "time_complexity": "O(log(min(m, n)))",
    "space_complexity": "O(1)",
    "description": "Find the median of two sorted arrays in logarithmic time.",
}

def solve(nums1: list[int], nums2: list[int]) -> float:
    """
    Finds the median of two sorted arrays using binary search on the partition point.

    Args:
        nums1: The first sorted list of integers.
        nums2: The second sorted list of integers.

    Returns:
        The median value as a float.

    Examples:
        >>> solve([1, 3], [2])
        2.0
        >>> solve([1, 2], [3, 4])
        2.5
    """
    # Ensure nums1 is the smaller array to achieve O(log(min(m, n))) complexity
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m
    half_len = (m + n + 1) // 2

    while low <= high:
        # partition_x is the number of elements contributed by nums1 to the left half
        partition_x = (low + high) // 2
        # partition_y is the number of elements contributed by nums2 to the left half
        partition_y = half_len - partition_x

        # Boundary values for the elements around the partition in nums1
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]

        # Boundary values for the elements around the partition in nums2
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]

        # Check if we have found the correct partition
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # If total number of elements is odd, median is the max of the left side
            if (m + n) % 2 == 1:
                return float(max(max_left_x, max_left_y))
            # If even, median is the average of the max of left and min of right
            else:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
        
        # If max_left_x is too large, we must move the partition in nums1 to the left
        elif max_left_x > min_right_y:
            high = partition_x - 1
        # If max_left_y is too large, we must move the partition in nums1 to the right
        else:
            low = partition_x + 1

    raise ValueError("Input arrays are not sorted or invalid.")
