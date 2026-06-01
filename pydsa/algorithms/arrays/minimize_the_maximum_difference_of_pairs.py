METADATA = {
    "id": 2616,
    "name": "Minimize the Maximum Difference of Pairs",
    "slug": "minimize-the-maximum-difference-of-pairs",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log(max_val))",
    "space_complexity": "O(1)",
    "description": "Minimize the maximum difference between pairs of elements chosen from a sorted array.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the minimum possible value of the maximum difference between k pairs.

    Args:
        nums: A list of integers.
        k: The number of pairs to form.

    Returns:
        The minimum possible maximum difference.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6], 2)
        1
        >>> solve([1, 10, 15, 20], 2)
        5
    """
    nums.sort()
    n = len(nums)

    def can_form_k_pairs(max_diff: int) -> bool:
        """
        Checks if it is possible to form at least k pairs such that 
        the difference of each pair is at most max_diff.
        """
        count = 0
        i = 0
        # Greedy approach: iterate through the sorted array and pick 
        # the first available pair that satisfies the max_diff constraint.
        while i < n - 1:
            if nums[i + 1] - nums[i] <= max_diff:
                count += 1
                # Skip the next element as it is now part of a pair
                i += 2
            else:
                i += 1
            
            if count >= k:
                return True
        return False

    # Binary search range: 
    # Minimum possible difference is 0.
    # Maximum possible difference is the range of the array.
    low = 0
    high = nums[-1] - nums[0]
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can_form_k_pairs(mid):
            # If mid is feasible, try to find a smaller maximum difference
            ans = mid
            high = mid - 1
        else:
            # If mid is not feasible, we need a larger difference
            low = mid + 1

    return ans
