METADATA = {
    "id": 2779,
    "name": "Maximum Beauty of an Array After Applying Operation",
    "slug": "maximum-beauty-of-an-array-after-applying-operation",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "sorting", "two-pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum difference between the maximum and minimum elements of an array after applying at most k operations where each operation increases or decreases an element by 1.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Args:
        nums: A list of integers representing the array.
        k: An integer representing the maximum number of operations allowed.

    Returns:
        The maximum possible beauty of the array.
    """
    nums.sort()
    n = len(nums)
    max_beauty = 0
    left = 0
    
    for right in range(n):
        while nums[right] - nums[left] > 2 * k:
            left += 1
        
        current_beauty = nums[right] - nums[left]
        if current_beauty > max_beauty:
            max_beauty = current_beauty
            
    return max_beauty