METADATA = {
    "id": 2155,
    "name": "All Divisions With the Highest Score of a Binary Array",
    "slug": "all-divisions-with-the-highest-score-of-a-binary-array",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find all indices where dividing the array into two non-empty parts maximizes the sum of the minimum and maximum of the two parts.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Args:
        nums: A list of binary integers.

    Returns:
        A list of indices representing the division points that yield the highest score.
    """
    total_sum = sum(nums)
    n = len(nums)
    
    left_sum = 0
    left_min = 0
    left_max = 0
    
    right_min = 1
    right_max = 1
    
    right_sum = total_sum
    
    max_score = -1
    result_indices = []
    
    left_min_tracker = [0] * n
    left_max_tracker = [0] * n
    right_min_tracker = [0] * n
    right_max_tracker = [0] * n
    
    current_min = 0
    current_max = 0
    for i in range(n):
        if nums[i] == 1:
            current_max = 1
        current_min = 0
        left_min_tracker[i] = current_min
        left_max_tracker[i] = current_max
        
    current_min = 0
    current_max = 0
    for i in range(n - 1, -1, -1):
        if nums[i] == 1:
            current_max = 1
        current_min = 0
        right_min_tracker[i] = current_min
        right_max_tracker[i] = current_max

    left_sum = 0
    left_min = 0
    left_max = 0
    
    right_sum = total_sum
    
    for i in range(n - 1):
        left_sum += nums[i]
        right_sum -= nums[i]
        
        if nums[i] == 1:
            left_max = 1
        left_min = 0
        
        if right_sum > 0:
            right_max = 1
            right_min = 0
        else:
            right_max = 0
            right_min = 0
            
        score = left_min + left_max + right_min + right_max
        
        if score > max_score:
            max_score = score
            result_indices = [i]
        elif score == max_score:
            result_indices.append(i)
            
    return result_indices

def solve(nums: list[int]) -> list[int]:
    """
    Args:
        nums: A list of binary integers.

    Returns:
        A list of indices representing the division points that yield the highest score.
    """
    n = len(nums)
    total_sum = sum(nums)
    
    left_sum = 0
    left_max = 0
    
    right_sum = total_sum
    right_max = 1 if total_sum > 0 else 0
    
    max_score = -1
    result_indices = []
    
    for i in range(n - 1):
        left_sum += nums[i]
        right_sum -= nums[i]
        
        if nums[i] == 1:
            left_max = 1
            
        if right_sum > 0:
            right_max = 1
        else:
            right_max = 0
            
        left_min = 0
        right_min = 0
        
        score = left_min + left_max + right_min + right_max
        
        if score > max_score:
            max_score = score
            result_indices = [i]
        elif score == max_score:
            result_indices.append(i)
            
    return result_indices