METADATA = {
    "id": 315,
    "name": "Count of Smaller Numbers After Self",
    "slug": "count-of-smaller-numbers-after-self",
    "category": "Hard",
    "aliases": [],
    "tags": ["merge_sort", "binary_indexed_tree", "segment_tree"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given an integer array nums, return an integer array res where res[i] is the number of smaller elements to the right of nums[i].",
}

def solve(nums: list[int]) -> list[int]:
    """
    Counts the number of smaller elements to the right of each element using a modified merge sort.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers where each index i contains the count of smaller elements 
        to the right of nums[i].

    Examples:
        >>> solve([5, 2, 6, 1])
        [2, 1, 1, 0]
        >>> solve([-1])
        [0]
    """
    n = len(nums)
    counts = [0] * n
    # We store tuples of (value, original_index) to track where counts should be updated
    indexed_nums = [(val, i) for i, val in enumerate(nums)]

    def merge_sort(arr: list[tuple[int, int]]) -> list[tuple[int, int]]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])

        return merge(left_half, right_half)

    def merge(left: list[tuple[int, int]], right: list[tuple[int, int]]) -> list[tuple[int, int]]:
        merged = []
        left_idx = 0
        right_idx = 0
        # right_count tracks how many elements from the right half have been 
        # placed into the merged array before the current element from the left half.
        # Since the right half is sorted, if right[right_idx] < left[left_idx], 
        # then right[right_idx] is smaller than all remaining elements in left.
        right_count = 0

        while left_idx < len(left) and right_idx < len(right):
            # If the element in the right half is smaller than the element in the left half
            if right[right_idx][0] < left[left_idx][0]:
                merged.append(right[right_idx])
                right_idx += 1
                right_count += 1
            else:
                # If the element in the left half is smaller or equal, 
                # it "jumps over" all elements currently counted in right_count
                counts[left[left_idx][1]] += right_count
                merged.append(left[left_idx])
                left_idx += 1

        # Clean up remaining elements in left half
        while left_idx < len(left):
            counts[left[left_idx][1]] += right_count
            merged.append(left[left_idx])
            left_idx += 1

        # Clean up remaining elements in right half
        while right_idx < len(right):
            merged.append(right[right_idx])
            right_idx += 1

        return merged

    merge_sort(indexed_nums)
    return counts
