METADATA = {
    "id": 3250,
    "name": "Find the Count of Monotonic Pairs I",
    "slug": "find-the-count-of-monotonic-pairs-i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n * max_val)",
    "space_complexity": "O(max_val)",
    "description": "Count the number of pairs of arrays (nums1, nums2) such that both arrays are non-decreasing and nums1[i] + nums2[i] <= target.",
}

def solve(nums1: list[int], nums2: list[int], target: int) -> int:
    """
    Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.
        target: The maximum allowed sum for each pair of elements.

    Returns:
        The count of monotonic pairs modulo 10^9 + 7.
    """
    MODULO = 10**9 + 7
    n = len(nums1)
    max_val = 0
    for i in range(n):
        max_val = max(max_val, nums1[i], nums2[i])
    
    limit = max_val + 1
    dp = [0] * limit

    for i in range(n):
        new_dp = [0] * limit
        prefix_sum = [0] * (limit + 1)
        for j in range(limit):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MODULO
        
        for v1 in range(nums1[i], limit):
            max_v2 = min(limit - 1, target - v1)
            if max_v2 < nums2[i]:
                continue
            
            if i == 0:
                new_dp[v1] = 1
            else:
                upper_bound_v2 = min(max_v2, limit - 1)
                lower_bound_v2 = nums2[i]
                
                if upper_bound_v2 >= lower_bound_v2:
                    count = (prefix_sum[upper_bound_v2 + 1] - prefix_sum[lower_bound_v2]) % MODULO
                    new_dp[v1] = count
        
        dp = new_dp

    total_count = sum(dp) % MODULO
    return total_count

def solve_optimized(nums1: list[int], nums2: list[int], target: int) -> int:
    """
    Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.
        target: The maximum allowed sum for each pair of elements.

    Returns:
        The count of monotonic pairs modulo 10^9 + 7.
    """
    MODULO = 10**9 + 7
    n = len(nums1)
    max_val = 0
    for i in range(n):
        max_val = max(max_val, nums1[i], nums2[i])
    
    limit = max_val + 1
    dp = [0] * limit

    for i in range(n):
        new_dp = [0] * limit
        prefix_sum = [0] * (limit + 1)
        for j in range(limit):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MODULO
        
        for v1 in range(nums1[i], limit):
            max_v2 = target - v1
            if max_v2 < nums2[i]:
                continue
            
            if i == 0:
                new_dp[v1] = 1
            else:
                upper_bound_v2 = min(max_v2, limit - 1)
                lower_bound_v2 = nums2[i]
                
                if upper_bound_v2 >= lower_bound_v2:
                    count = (prefix_sum[upper_bound_v2 + 1] - prefix_sum[lower_bound_v2]) % MODULO
                    new_dp[v1] = count
        dp = new_dp

    return sum(dp) % MODULO

def solve(nums1: list[int], nums2: list[int], target: int) -> int:
    """
    Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.
        target: The maximum allowed sum for each pair of elements.

    Returns:
        The count of monotonic pairs modulo 10^9 + 7.
    """
    MODULO = 10**9 + 7
    n = len(nums1)
    max_val = 0
    for i in range(n):
        max_val = max(max_val, nums1[i], nums2[i])
    
    limit = max_val + 1
    dp = [0] * limit

    for i in range(n):
        new_dp = [0] * limit
        prefix_sum = [0] * (limit + 1)
        for j in range(limit):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MODULO
        
        for v1 in range(nums1[i], limit):
            max_v2 = target - v1
            if max_v2 < nums2[i]:
                continue
            
            if i == 0:
                new_dp[v1] = 1
            else:
                upper_bound_v2 = min(max_v2, limit - 1)
                lower_bound_v2 = nums2[i]
                
                if upper_bound_v2 >= lower_bound_v2:
                    count = (prefix_sum[upper_bound_v2 + 1] - prefix_sum[lower_bound_v2]) % MODULO
                    new_dp[v1] = count
        dp = new_dp

    return sum(dp) % MODULO

def solve(nums1: list[int], nums2: list[int], target: int) -> int:
    """
    Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.
        target: The maximum allowed sum for each pair of elements.

    Returns:
        The count of monotonic pairs modulo 10^9 + 7.
    """
    MODULO = 10**9 + 7
    n = len(nums1)
    max_val = 0
    for i in range(n):
        max_val = max(max_val, nums1[i], nums2[i])
    
    limit = max_val + 1
    dp = [0] * limit

    for i in range(n):
        new_dp = [0] * limit
        prefix_sum = [0] * (limit + 1)
        for j in range(limit):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MODULO
        
        for v1 in range(nums1[i], limit):
            max_v2 = target - v1
            if max_v2 < nums2[i]:
                continue
            
            if i == 0:
                new_dp[v1] = 1
            else:
                upper_bound_v2 = min(max_v2, limit - 1)
                lower_bound_v2 = nums2[i]
                
                if upper_bound_v2 >= lower_bound_v2:
                    count = (prefix_sum[upper_bound_v2 + 1] - prefix_sum[lower_bound_v2]) % MODULO
                    new_dp[v1] = count
        dp = new_dp

    return sum(dp) % MODULO

def solve(nums1: list[int], nums2: list[int], target: int) -> int:
    """
    Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.
        target: The maximum allowed sum for each pair of elements.

    Returns:
        The count of monotonic pairs modulo 10^9 + 7.
    """
    MODULO = 10**9 + 7
    n = len(nums1)
    max_val = 0
    for i in range(n):
        max_val = max(max_val, nums1[i], nums2[i])
    
    limit = max_val + 1
    dp = [0] * limit

    for i in range(n):
        new_dp = [0] * limit
        prefix_sum = [0] * (limit + 1)
        for j in range(limit):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MODULO
        
        for v1 in range(nums1[i], limit):
            max_v2 = target - v1
            if max_v2 < nums2[i]:
                continue
            
            if i == 0:
                new_dp[v1] = 1
            else:
                upper_bound_v2 = min(max_v2, limit - 1)
                lower_bound_v2 = nums2[i]
                
                if upper_bound_v2 >= lower_bound_v2:
                    count = (prefix_sum[upper_bound_v2 + 1] - prefix_sum[lower_bound_v2]) % MODULO
                    new_dp[v1] = count
        dp = new_dp

    return sum(dp) % MODULO

def solve(nums1: list[int], nums2: list[int], target: int) -> int:
    """
    Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.
        target: The maximum allowed sum for each pair of elements.

    Returns:
        The count of monotonic pairs modulo 10^9 + 7.
    """
    MODULO = 10**9 + 7
    n = len(nums1)
    max_val = 0
    for i in range(n):
        max_val = max(max_val, nums1[i], nums2[i])
    
    limit = max_val + 1
    dp = [0] * limit

    for i in range(n):
        new_dp = [0] * limit
        prefix_sum = [0] * (limit + 1)
        for j in range(limit):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MODULO
        
        for v1 in range(nums1[i], limit):
            max_v2 = target - v1
            if max_v2 < nums2[i]:
                continue
            
            if i == 0:
                new_dp[v1] = 1
            else:
                upper_bound_v2 = min(max_v2, limit - 1)
                lower_bound_v2 = nums2[i]
                
                if upper_bound_v2 >= lower_bound_v2:
                    count = (prefix_sum[upper_bound_v2 + 1] - prefix_sum[lower_bound_v2]) % MODULO
                    new_dp[v1] = count
        dp = new_dp

    return sum(dp) % MODULO

def solve(nums1: list[int], nums2: list[int], target: int) -> int:
    """
    Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.
        target: The maximum allowed sum for each pair of elements.

    Returns:
        The count of monotonic pairs modulo 10^9 + 7.
    """
    MODULO = 10**9 + 7
    n = len(nums1)
    max_val = 0
    for i in range(n):
        max_val = max(max_val, nums1[i], nums2[i])
    
    limit = max_val + 1
    dp = [0] * limit

    for i in range(n):
        new_dp = [0] * limit
        prefix_sum = [0] * (limit + 1)
        for j in range(limit):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MODULO
        
        for v1 in range(nums1[i], limit):
            max_v2 = target - v1
            if max_v2 < nums2[i]:
                continue
            
            if i == 0:
                new_dp[v1] = 1
            else:
                upper_bound_v2 = min(max_v2, limit - 1)
                lower_bound_v2 = nums2[i]
                
                if upper_bound_v2 >= lower_bound_v2:
                    count = (prefix_sum[upper_bound_v2 + 1] - prefix_sum[lower_bound_v2]) % MODULO
                    new_dp[v1] = count
        dp = new_dp

    return sum(dp) % MODULO

def solve(nums1: list[int], nums2: list[int], target: int) -> int:
    """
    Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.
        target: The maximum allowed sum for each pair of elements.

    Returns:
        The count of monotonic pairs modulo 10^9 + 7.
    """
    MODULO = 10**9 + 7
    n = len(nums1)
    max_val = 0
    for i in range(n):
        max_val = max(max_val, nums1[i], nums2[i])
    
    limit = max_val + 1
    dp = [0] * limit

    for i in range(n):
        new_dp = [0] * limit
        prefix_sum = [0] * (limit + 1)
        for j in range(limit):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MODULO
        
        for v1 in range(nums1[i], limit):
            max_v2 = target - v1
            if max_v2 < nums2[i]:
                continue
            
            if i == 0:
                new_dp[v1] = 1
            else:
                upper_bound_v2 = min(max_v2, limit - 1)
                lower_bound_v2 = nums2[i]
                
                if upper_bound_v2 >= lower_bound_v2:
                    count = (prefix_sum[upper_bound_v2 + 1] - prefix_sum[lower_bound_v2]) % MODULO
                    new_dp[v1] = count
        dp = new_dp

    return sum(dp) % MODULO

def solve(nums1: list[int], nums2: list[int], target: int) -> int:
    """
    Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.
        target: The maximum allowed sum for each pair of elements.

    Returns:
        The count of monotonic pairs modulo 10^9 + 7.
    """
    MODULO = 10**9 + 7
    n = len(nums1)
    max_val = 0
    for i in range(n):
        max_val = max(max_val, nums1[i], nums2[i])
    
    limit = max_val + 1
    dp = [0] * limit

    for i in range(n):
        new_dp = [0] * limit
        prefix_sum = [0] * (limit + 1)
        for j in range(limit):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MODULO
        
        for v1 in range(nums1[i], limit):
            max_v2 = target - v1
            if max_v2 < nums2[i]:
                continue
            
            if i == 0:
                new_dp[v1] = 1
            else:
                upper_bound_v2 = min(max_v2, limit - 1)
                lower_bound_v2 = nums2[i]
                
                if upper_bound_v2 >= lower_bound_v2:
                    count = (prefix_sum[upper_bound_v2 + 1] - prefix_sum[lower_bound_v2])