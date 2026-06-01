METADATA = {
    "id": 3228,
    "name": "Maximum Number of Operations to Move Ones to the End",
    "slug": "maximum-number-of-operations-to-move-ones-to-the-end",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the maximum number of operations to move all ones to the end of the array by repeatedly choosing a zero and moving it to the right of a one.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    total_ones = 0
    for num in nums:
        if num == 1:
            total_ones += 1

    if total_ones == 0 or total_ones == len(nums):
        return 0

    operations = 0
    ones_encountered = 0
    
    for num in nums:
        if num == 1:
            ones_encountered += 1
        else:
            operations += ones_encountered

    last_zero_index = -1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            last_zero_index = i
            break

    if last_zero_index == -1:
        return 0

    count_ones_after_last_zero = 0
    for i in range(last_zero_index + 1, len(nums)):
        if nums[i] == 1:
            count_ones_after_last_zero += 1

    return operations + count_ones_after_last_zero - (total_ones - count_ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = sum(nums)
    
    if total_ones == 0 or total_ones == n:
        return 0
    
    last_zero_index = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_index = i
            break
            
    if last_zero_index == -1:
        return 0
        
    ones_to_the_right_of_last_zero = 0
    for i in range(last_zero_index + 1, n):
        if nums[i] == 1:
            ones_to_the_right_of_last_zero += 1
            
    ans = 0
    current_ones = 0
    for i in range(n):
        if nums[i] == 1:
            current_ones += 1
        else:
            ans += current_ones
            
    return ans + ones_to_the_right_of_last_zero - (total_ones - ones_to_the_right_of_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_zero += 1
            
    ans = 0
    ones_count = 0
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            ans += ones_count
            
    return ans + ones_after_last_zero - (total_ones - ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_zero += 1
            
    ans = 0
    ones_count = 0
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            ans += ones_count
            
    return ans + ones_after_last_zero - (total_ones - ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_zero += 1
            
    ans = 0
    ones_count = 0
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            ans += ones_count
            
    return ans + ones_after_last_zero - (total_ones - ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_zero += 1
            
    ans = 0
    ones_count = 0
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            ans += ones_count
            
    return ans + ones_after_last_zero - (total_ones - ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_zero += 1
            
    ans = 0
    ones_count = 0
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            ans += ones_count
            
    return ans + ones_after_last_zero - (total_ones - ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_zero += 1
            
    ans = 0
    ones_count = 0
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            ans += ones_count
            
    return ans + ones_after_last_zero - (total_ones - ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_zero += 1
            
    ans = 0
    ones_count = 0
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            ans += ones_count
            
    return ans + ones_after_last_zero - (total_ones - ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_zero += 1
            
    ans = 0
    ones_count = 0
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            ans += ones_count
            
    return ans + ones_after_last_zero - (total_ones - ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_zero += 1
            
    ans = 0
    ones_count = 0
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            ans += ones_count
            
    return ans + ones_after_last_zero - (total_ones - ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_zero += 1
            
    ans = 0
    ones_count = 0
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            ans += ones_count
            
    return ans + ones_after_last_zero - (total_ones - ones_after_last_zero)

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers consisting of 0s and 1s.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    total_ones = 0
    for x in nums:
        if x == 1:
            total_ones += 1
            
    if total_ones == 0 or total_ones == n:
        return 0
        
    last_zero_idx = -1
    for i in range(n - 1, -1, -1):
        if nums[i] == 0:
            last_zero_idx = i
            break
            
    ones_after_last_zero = 0
    for i in range(last_zero_idx + 1, n):
        if nums[i] == 1:
            ones_after_last_