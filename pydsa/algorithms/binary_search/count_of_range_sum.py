METADATA = {
    "id": 327,
    "name": "Count of Range Sum",
    "slug": "count-of-range-sum",
    "category": "Divide and Conquer",
    "aliases": [],
    "tags": ["divide_and_conquer", "binary_indexed_tree", "segment_tree", "merge_sort"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of range sums that lie within a given range [lower, upper].",
}

def solve(nums: list[int], lower: int, upper: int) -> int:
    """
    Counts the number of range sums that fall within [lower, upper] using 
    a modified merge sort on prefix sums.

    Args:
        nums: A list of integers.
        lower: The lower bound of the range sum.
        upper: The upper bound of the range sum.

    Returns:
        The total count of range sums within the specified bounds.

    Examples:
        >>> solve([1, -1, -1, 1], 0, 0)
        3
        >>> solve([-2, 5, -1], -2, 2)
        3
    """
    # Calculate prefix sums. prefix_sums[i] is the sum of nums[0...i-1]
    # The sum of range [i, j] is prefix_sums[j+1] - prefix_sums[i]
    prefix_sums = [0]
    current_sum = 0
    for num in nums:
        current_sum += num
        prefix_sums.append(current_sum)

    def count_while_sorting(sums: list[int], start: int, end: int) -> int:
        """
        Recursive merge sort function that counts valid pairs during the merge step.
        """
        if end - start <= 1:
            return 0

        mid = (start + end) // 2
        # Count valid pairs in left and right halves
        count = count_while_sorting(sums, start, mid) + count_while_sorting(sums, mid, end)

        # Count pairs (i, j) such that start <= i < mid <= j < end
        # and lower <= sums[j] - sums[i] <= upper
        # This is equivalent to: sums[i] + lower <= sums[j] <= sums[i] + upper
        left_idx = mid
        right_idx = mid
        for i in range(start, mid):
            # Find the first index in the right half where sums[j] >= sums[i] + lower
            while left_idx < end and sums[left_idx] < sums[i] + lower:
                left_idx += 1
            # Find the first index in the right half where sums[j] > sums[i] + upper
            while right_idx < end and sums[right_idx] <= sums[i] + upper:
                right_idx += 1
            # All indices in [left_idx, right_idx) satisfy the condition
            count += (right_idx - left_idx)

        # Standard merge step to keep the prefix_sums array sorted for the next level
        sums[start:end] = sorted(sums[start:end])
        return count

    return count_while_sorting(prefix_sums, 0, len(prefix_sums))
