METADATA = {
    "id": 1509,
    "name": "Minimum Difference Between Largest and Smallest Value in Three Moves",
    "slug": "minimum-difference-between-largest-and-smallest-value-in-three-moves",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum possible difference between the largest and smallest elements in an array after performing at most three moves.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum difference between the largest and smallest values 
    after changing at most three elements to any value.

    The optimal strategy is to sort the array and then decide which three 
    elements to "remove" (by changing them to match the boundaries) to 
    minimize the range. The possible scenarios are:
    1. Change the 3 smallest elements.
    2. Change the 3 largest elements.
    3. Change the 2 smallest and 1 largest element.
    4. Change the 1 smallest and 2 largest elements.

    Args:
        nums: A list of integers.

    Returns:
        The minimum difference between the maximum and minimum elements.

    Examples:
        >>> solve([1, 3, 3, 2, 2])
        0
        >>> solve([1, 1, 1, 1])
        0
        >>> solve([1, 10, 10, 10])
        0
        >>> solve([1, 2, 3, 4, 5, 6])
        3
    """
    n = len(nums)
    
    # If there are 4 or fewer elements, we can make all of them equal
    # by changing 3 elements to match the 4th.
    if n <= 4:
        return 0

    nums.sort()

    # After sorting, we want to find the minimum (nums[right] - nums[left])
    # where we have "skipped" 3 elements in total from the ends.
    # The possible windows of size (n - 3) are:
    # 1. Skip 3 smallest: nums[3] to nums[n-1]
    # 2. Skip 2 smallest, 1 largest: nums[2] to nums[n-2]
    # 3. Skip 1 smallest, 2 largest: nums[1] to nums[n-3]
    # 4. Skip 3 largest: nums[0] to nums[n-4]
    
    # We can generalize this: we are looking for a window of size (n - 3)
    # that starts at index i and ends at index i + (n - 4).
    # Since we can skip at most 3 elements, the starting index i can be 0, 1, 2, or 3.
    
    min_diff = float('inf')
    
    # The number of elements remaining in our window is n - 3.
    # The index of the last element in a window starting at 'i' is i + (n - 4).
    # However, it's easier to think about the number of elements we 'keep'.
    # We keep k = n - 3 elements.
    k = n - 3
    
    # We iterate through all possible starting positions for a window of size k
    # that leaves at most 3 elements outside the window.
    for i in range(4):
        # The window starts at i and ends at i + k - 1
        current_diff = nums[i + k - 1] - nums[i]
        if current_diff < min_diff:
            min_diff = current_diff
            
    return int(min_diff)
