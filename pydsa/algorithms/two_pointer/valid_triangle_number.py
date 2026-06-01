METADATA = {
    "id": 611,
    "name": "Valid Triangle Number",
    "slug": "valid-triangle-number",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "sorting", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Given an integer array nums, return the number of triplets chosen from the array that can make up a triangle.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of triplets in the array that can form a valid triangle.
    
    A triplet (a, b, c) forms a triangle if and only if:
    a + b > c
    a + c > b
    b + c > a
    
    If the array is sorted such that a <= b <= c, we only need to check if a + b > c.

    Args:
        nums: A list of integers representing the lengths of the sides.

    Returns:
        The total number of valid triangle triplets.

    Examples:
        >>> solve([2, 2, 3, 4])
        3
        >>> solve([4, 2, 3, 5])
        3
        >>> solve([1, 1, 1, 1])
        4
    """
    n = len(nums)
    if n < 3:
        return 0

    # Sort the array to simplify the triangle inequality condition.
    # For a sorted array where i < j < k, we only need to check nums[i] + nums[j] > nums[k].
    nums.sort()
    count = 0

    # Iterate backwards, treating nums[k] as the largest side of the potential triangle.
    for k in range(n - 1, 1, -1):
        left = 0
        right = k - 1
        
        while left < right:
            # If the sum of the two smaller sides is greater than the largest side,
            # then all elements from 'left' to 'right-1' paired with 'right' 
            # will also satisfy the condition because the array is sorted.
            if nums[left] + nums[right] > nums[k]:
                # All elements between left and right (inclusive of left) 
                # work as the first side when paired with nums[right] and nums[k].
                count += (right - left)
                # Move the right pointer to try a smaller 'middle' side.
                right -= 1
            else:
                # The sum is too small, we need a larger 'smallest' side.
                left += 1
                
    return count
