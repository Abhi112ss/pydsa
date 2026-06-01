METADATA = {
    "id": 2934,
    "name": "Minimum Operations to Maximize Last Elements in Arrays",
    "slug": "minimum-operations-to-maximize-last-elements-in-arrays",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of operations to make the last element of an array equal to the maximum element in the array by repeatedly replacing the last element with the sum of the last two elements.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers representing the array.

    Returns:
        The minimum number of operations required to make the last element equal to the maximum element.
    """
    n = len(nums)
    if n == 0:
        return 0
    
    max_val = nums[0]
    for i in range(1, n):
        if nums[i] > max_val:
            max_val = nums[i]
            
    if nums[-1] == max_val:
        return 0
        
    operations = 0
    current_last = nums[-1]
    second_last = nums[-2]
    
    while current_last < max_val:
        current_last, second_last = current_last + second_last, current_last
        operations += 1
        
    return operations