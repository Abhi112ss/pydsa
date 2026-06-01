METADATA = {
    "id": 1685,
    "name": "Sum of Absolute Differences in a Sorted Array",
    "slug": "sum_of_absolute_differences_in_a_sorted_array",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return an array where each element is the sum of absolute differences between that element and all other elements in the sorted array.",
}


def solve(nums: list[int]) -> list[int]:
    """Calculate the sum of absolute differences for each element in a sorted array.

    Args:
        nums: A list of integers sorted in non‑decreasing order.

    Returns:
        A list where the i‑th element is the sum of |nums[i] - nums[j]| for all j.

    Examples:
        >>> solve([2, 3, 5])
        [4, 3, 5]
        >>> solve([1, 2, 3, 4])
        [6, 4, 4, 6]
    """
    length = len(nums)
    total_sum = sum(nums)                     # total sum of all elements
    prefix_sum = 0
    result = [0] * length

    for index, value in enumerate(nums):
        left_count = index                     # number of elements to the left
        right_count = length - index - 1       # number of elements to the right

        left_sum = prefix_sum                  # sum of elements to the left
        right_sum = total_sum - prefix_sum - value  # sum of elements to the right

        # contribution from left side + contribution from right side
        result[index] = value * left_count - left_sum + right_sum - value * right_count

        prefix_sum += value                    # update prefix sum for next iteration

    return result