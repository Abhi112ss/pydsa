METADATA = {
    "id": 493,
    "name": "Reverse Pairs",
    "slug": "reverse-pairs",
    "category": "Hard",
    "aliases": [],
    "tags": ["merge_sort", "segment_tree", "fenwick_tree", "divide_and_conquer"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of reverse pairs in an array where nums[i] > 2 * nums[j] and i < j.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of reverse pairs in the input list using a modified merge sort.

    A reverse pair is defined as (i, j) such that 0 <= i < j < len(nums) 
    and nums[i] > 2 * nums[j].

    Args:
        nums: A list of integers.

    Returns:
        The total count of reverse pairs.

    Examples:
        >>> solve([1, 3, 2, 3, 1])
        2
        >>> solve([2, 4, 3, 5, 1])
        3
    """
    if not nums:
        return 0

    def merge_sort_and_count(start: int, end: int) -> int:
        # Base case: single element has no pairs
        if start >= end:
            return 0

        mid = (start + end) // 2
        count = merge_sort_and_count(start, mid) + merge_sort_and_count(mid + 1, end)

        # Count the reverse pairs between the left and right halves
        # Since both halves are sorted, we can use a two-pointer approach
        right_pointer = mid + 1
        for left_pointer in range(start, mid + 1):
            while right_pointer <= end and nums[left_pointer] > 2 * nums[right_pointer]:
                right_pointer += 1
            count += (right_pointer - (mid + 1))

        # Standard merge step to keep the array sorted for the parent recursive calls
        temp_list = []
        left_idx = start
        right_idx = mid + 1

        while left_idx <= mid and right_idx <= end:
            if nums[left_idx] <= nums[right_idx]:
                temp_list.append(nums[left_idx])
                left_idx += 1
            else:
                temp_list.append(nums[right_idx])
                right_idx += 1

        while left_idx <= mid:
            temp_list.append(nums[left_idx])
            left_idx += 1
        while right_idx <= end:
            temp_list.append(nums[right_idx])
            right_idx += 1

        # Copy sorted elements back into the original array
        for i in range(len(temp_list)):
            nums[start + i] = temp_list[i]

        return count

    return merge_sort_and_count(0, len(nums) - 1)
