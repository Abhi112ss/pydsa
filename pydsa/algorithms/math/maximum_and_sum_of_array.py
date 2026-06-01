METADATA = {
    "id": 2172,
    "name": "Maximum AND Sum of Array",
    "slug": "maximum-and-sum-of-array",
    "category": "Greedy",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Maximize the bitwise AND sum of an array after distributing a set of integers to its elements.",
}

def solve(nums: list[int], alist: list[int]) -> int:
    """
    Args:
        nums: A list of integers representing the base values.
        alist: A list of integers to be distributed among the elements of nums.

    Returns:
        The maximum possible bitwise AND sum of the modified nums array.
    """
    nums.sort(reverse=True)
    alist.sort(reverse=True)
    
    nums_count = len(nums)
    alist_count = len(alist)
    
    nums_idx = 0
    alist_idx = 0
    
    while nums_idx < nums_count and alist_idx < alist_count:
        nums[nums_idx] &= alist[alist_idx]
        nums_idx += 1
        alist_idx += 1
        
    total_sum = 0
    for value in nums:
        total_sum += value
        
    return total_sum