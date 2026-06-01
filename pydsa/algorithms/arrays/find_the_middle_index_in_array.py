METADATA = {
    "id": 1991,
    "name": "Find the Middle Index in Array",
    "slug": "find_the_middle_index_in_array",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the leftmost index where the sum of elements on its left equals the sum on its right.",
}


def solve(nums: list[int]) -> int:
    """Find the leftmost middle index where left sum equals right sum.

    Args:
        nums: List of integers representing the array.

    Returns:
        The smallest index i such that sum(nums[:i]) == sum(nums[i+1:]).
        Returns -1 if no such index exists.

    Examples:
        >>> solve([2, 3, -1, 8, 4])
        3
        >>> solve([1, 2, 3])
        -1
    """
    total_sum: int = sum(nums)                     # total sum of the array
    left_sum: int = 0                               # sum of elements to the left of current index

    for index, value in enumerate(nums):
        right_sum: int = total_sum - left_sum - value   # sum of elements to the right
        if left_sum == right_sum:
            return index                                 # leftmost index found
        left_sum += value                               # update left sum for next iteration

    return -1                                            # no middle index exists