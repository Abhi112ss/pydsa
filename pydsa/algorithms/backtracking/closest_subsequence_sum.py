METADATA = {
    "id": 1755,
    "name": "Closest Subsequence Sum",
    "slug": "closest-subsequence-sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["meet-in-the-middle", "backtracking", "binary search"],
    "difficulty": "hard",
    "time_complexity": "O(2^(n/2))",
    "space_complexity": "O(2^(n/2))",
    "description": "Find a subsequence sum that is closest to a given target using the meet-in-the-middle approach.",
}

import bisect

def solve(nums: list[int], target: int) -> int:
    """
    Finds the subsequence sum that is closest to the target value.

    Args:
        nums: A list of integers.
        target: The target integer value.

    Returns:
        The sum of a subsequence that is closest to the target.

    Examples:
        >>> solve([1, 2, 4], 5)
        5
        >>> solve([-1, 2, 1, -4], 1)
        1
    """
    n = len(nums)

    def get_all_subset_sums(arr: list[int]) -> list[int]:
        """Generates all possible subset sums for a given array using bit manipulation."""
        sums = [0]
        for num in arr:
            # For every existing sum, create a new sum by adding the current number
            new_sums = []
            for s in sums:
                new_sums.append(s + num)
            sums.extend(new_sums)
        return sums

    # Split the array into two halves to reduce complexity from 2^n to 2^(n/2)
    mid = n // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    # Generate all possible sums for both halves
    left_sums = get_all_subset_sums(left_half)
    right_sums = get_all_subset_sums(right_half)

    # Sort the right sums to enable binary search
    right_sums.sort()

    closest_sum = float('inf')
    min_diff = float('inf')

    # For every sum in the left half, find the best complement in the right half
    for s_left in left_sums:
        needed = target - s_left
        
        # Use binary search to find the closest value to 'needed' in right_sums
        idx = bisect.bisect_left(right_sums, needed)

        # Check the element at idx (the smallest element >= needed)
        if idx < len(right_sums):
            current_sum = s_left + right_sums[idx]
            diff = abs(target - current_sum)
            if diff < min_diff:
                min_diff = diff
                closest_sum = current_sum
            if diff == 0:
                return target

        # Check the element at idx - 1 (the largest element < needed)
        if idx > 0:
            current_sum = s_left + right_sums[idx - 1]
            diff = abs(target - current_sum)
            if diff < min_diff:
                min_diff = diff
                closest_sum = current_sum
            if diff == 0:
                return target

    return int(closest_sum)
