METADATA = {
    "id": 3392,
    "name": "Count Subarrays of Length Three With a Condition",
    "slug": "count-subarrays-of-length-three-with-a-condition",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays of length three where the first element is strictly greater than the second, or the second is strictly greater than the third.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of subarrays of length three that satisfy the condition:
    (nums[i] > nums[i+1]) OR (nums[i+1] > nums[i+2]).

    Args:
        nums: A list of integers.

    Returns:
        The total count of subarrays of length three meeting the condition.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        0
        >>> solve([5, 4, 3, 2, 1])
        3
        >>> solve([1, 5, 2, 4, 3])
        3
    """
    n = len(nums)
    if n < 3:
        return 0

    count = 0
    
    # Iterate through the array using a fixed-size window of 3
    # The loop runs up to n-3 to ensure i, i+1, and i+2 are valid indices
    for i in range(n - 2):
        first = nums[i]
        second = nums[i + 1]
        third = nums[i + 2]
        
        # Check the condition: (a > b) OR (b > c)
        if first > second or second > third:
            count += 1
            
    return count
