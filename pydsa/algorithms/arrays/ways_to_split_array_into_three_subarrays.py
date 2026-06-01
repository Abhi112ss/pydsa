METADATA = {
    "id": 1712,
    "name": "Ways to Split Array Into Three Subarrays",
    "slug": "ways_to_split_array_into_three_subarrays",
    "category": "array",
    "aliases": [],
    "tags": ["prefix_sum", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the ways to split an array into three contiguous parts with non‑decreasing sums.",
}


def solve(nums: list[int]) -> int:
    """Count the number of ways to split ``nums`` into three contiguous subarrays
    (left, middle, right) such that ``sum(left) <= sum(middle) <= sum(right)``.

    Args:
        nums: List of non‑negative integers.

    Returns:
        The number of valid splits modulo 10**9 + 7.

    Examples:
        >>> solve([1,1,1])
        1
        >>> solve([1,2,2,2,5,0])
        3
    """
    MOD = 10**9 + 7
    n = len(nums)
    if n < 3:
        return 0

    # Build prefix sums: prefix[i] = sum of nums[:i]
    prefix = [0] * (n + 1)
    for index, value in enumerate(nums):
        prefix[index + 1] = prefix[index] + value

    total_sum = prefix[n]
    answer = 0
    left_cut = 0   # smallest possible second cut index (exclusive)
    right_cut = 0  # one past the largest valid second cut index (exclusive)

    # i is the end index of the left subarray (exclusive)
    for i in range(1, n - 1):
        # Ensure left_cut starts at least i
        left_cut = max(left_cut, i)
        # Move left_cut forward until middle sum >= left sum
        while left_cut < n - 1 and prefix[left_cut + 1] - prefix[i] < prefix[i]:
            left_cut += 1

        # right_cut must be at least left_cut
        right_cut = max(right_cut, left_cut)
        # Expand right_cut while middle sum <= right sum
        while right_cut < n - 1 and prefix[right_cut + 1] - prefix[i] <= total_sum - prefix[right_cut + 1]:
            right_cut += 1

        # All indices j in [left_cut, right_cut) are valid second cuts
        answer += max(0, right_cut - left_cut)
        if answer >= MOD:
            answer -= MOD

    return answer