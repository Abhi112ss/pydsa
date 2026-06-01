METADATA = {
    "id": 1623,
    "name": "All Valid Triplets That Can Represent a Country",
    "slug": "all_valid_triplets_that_can_represent_a_country",
    "category": "array",
    "aliases": [],
    "tags": ["two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Counts the number of index triplets (i, j, k) with i < j < k such that nums[i] + nums[j] > nums[k].",
}


def solve(nums: list[int]) -> int:
    """Count the number of valid triplets representing a country.

    A triplet (i, j, k) is valid if i < j < k and
    nums[i] + nums[j] > nums[k] after sorting the array.

    Args:
        nums: List of non‑negative integers.

    Returns:
        The total number of valid triplets.

    Examples:
        >>> solve([2, 3, 4, 5])
        3
        >>> solve([1, 1, 1, 1])
        4
    """
    # Sort to enable the two‑pointer technique on ordered values.
    nums.sort()
    triplet_count = 0
    n = len(nums)

    # Iterate over each possible largest side index.
    for largest_index in range(2, n):
        left = 0
        right = largest_index - 1
        # Use two pointers to find all pairs (left, right) satisfying the condition.
        while left < right:
            if nums[left] + nums[right] > nums[largest_index]:
                # All elements between left and right form valid pairs with right.
                triplet_count += right - left
                right -= 1
            else:
                left += 1

    return triplet_count