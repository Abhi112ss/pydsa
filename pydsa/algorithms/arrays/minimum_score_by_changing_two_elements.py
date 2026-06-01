METADATA = {
    "id": 2567,
    "name": "Minimum Score by Changing Two Elements",
    "slug": "minimum-score-by-changing-two-elements",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum score of an array after changing at most two elements to any value.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum score of an array after changing at most two elements.
    The score is defined as max(nums) - min(nums).

    Args:
        nums: A list of integers.

    Returns:
        The minimum possible score after changing at most two elements.

    Examples:
        >>> solve([1, 1, 4, 2, 3])
        1
        >>> solve([1, 2, 3, 4, 5])
        1
        >>> solve([1, 10, 100])
        0
    """
    n = len(nums)
    
    # If there are 3 or fewer elements, we can change all of them 
    # (or enough to make them equal), resulting in a score of 0.
    if n <= 3:
        return 0

    # Sorting allows us to easily pick the smallest and largest elements.
    # Changing elements is most effective when targeting the current extremes.
    nums.sort()

    # After sorting, the original range is nums[n-1] - nums[0].
    # We can change up to 2 elements. This means we can effectively 
    # "remove" up to 2 elements from the ends of the sorted array.
    
    # There are 4 primary strategies to minimize the range:
    # 1. Remove the two smallest: range becomes nums[n-1] - nums[2]
    # 2. Remove the two largest: range becomes nums[n-3] - nums[0]
    # 3. Remove the smallest and the largest: range becomes nums[n-2] - nums[1]
    # 4. Remove one from each end, but we must consider if there's a 
    #    middle element that could become the new min/max.
    #    Actually, the 3 cases above cover all optimal "end-removal" scenarios.
    
    # Case 1: Remove nums[0] and nums[1]
    option1 = nums[n - 1] - nums[2]
    
    # Case 2: Remove nums[n-1] and nums[n-2]
    option2 = nums[n - 3] - nums[0]
    
    # Case 3: Remove nums[0] and nums[n-1]
    option3 = nums[n - 2] - nums[1]

    return min(option1, option2, option3)
