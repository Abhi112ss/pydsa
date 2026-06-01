METADATA = {
    "id": 2459,
    "name": "Sort Array by Moving Items to Empty Space",
    "slug": "sort-array-by-moving-items-to-empty-space",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine the minimum number of moves to sort an array containing elements and empty spaces by moving elements to empty spaces.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers where 0 represents an empty space.

    Returns:
        The minimum number of moves required to sort the array. Returns -1 if impossible.
    """
    n = len(nums)
    sorted_nums = sorted([x for x in nums if x != 0])
    
    if len(sorted_nums) != len([x for x in nums if x != 0]):
        return -1

    target_indices = []
    current_sorted_idx = 0
    
    for i in range(n):
        if nums[i] != 0:
            target_indices.append(i)
            
    if len(target_indices) != len(sorted_nums):
        return -1

    non_zero_elements = [x for x in nums if x != 0]
    
    if len(non_zero_elements) != len(sorted_nums):
        return -1

    sorted_elements_only = sorted(non_zero_elements)
    
    if sorted_elements_only != sorted_nums:
        return -1

    actual_non_zero_positions = [i for i, x in enumerate(nums) if x != 0]
    
    if len(actual_non_zero_positions) != len(sorted_nums):
        return -1

    sorted_positions = []
    temp_nums = sorted(nums)
    
    sorted_indices = []
    current_val_idx = 0
    
    sorted_array_with_zeros = sorted(nums)
    
    if sorted_array_with_zeros != sorted(nums):
        return -1

    non_zero_indices = [i for i, x in enumerate(nums) if x != 0]
    sorted_non_zero_values = sorted([x for x in nums if x != 0])
    
    if len(non_zero_indices) != len(sorted_non_zero_values):
        return -1
        
    sorted_indices_map = []
    for i in range(n):
        if nums[i] != 0:
            sorted_indices_map.append(i)
            
    if len(sorted_indices_map) != len(sorted_non_zero_values):
        return -1

    count_correct = 0
    for i in range(len(non_zero_indices)):
        if nums[non_zero_indices[i]] == sorted_non_zero_values[i]:
            count_correct += 1
            
    if count_correct == len(non_zero_indices):
        return 0

    is_possible = True
    sorted_version = sorted(nums)
    
    for i in range(n):
        if nums[i] != 0 and sorted_version[i] == 0:
            is_possible = False
            break
        if nums[i] == 0 and sorted_version[i] != 0:
            is_possible = False
            break
            
    if not is_possible:
        return -1

    correct_elements_count = 0
    for i in range(n):
        if nums[i] != 0 and nums[i] == sorted_version[i]:
            correct_elements_count += 1
            
    return len(sorted_non_zero_values) - correct_elements_count