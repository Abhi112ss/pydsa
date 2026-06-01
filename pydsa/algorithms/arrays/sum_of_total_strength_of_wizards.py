METADATA = {
    "id": 2281,
    "name": "Sum of Total Strength of Wizards",
    "slug": "sum-of-total-strength-of-wizards",
    "category": "Hard",
    "aliases": [],
    "tags": ["monotonic_stack", "prefix_sum", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of the minimum element in every subarray multiplied by the sum of elements in that subarray.",
}

def solve(strength: list[int]) -> int:
    """
    Args:
        strength: A list of integers representing the strength of wizards.

    Returns:
        The total strength sum modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    n = len(strength)
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MODULUS
        
    prefix_of_prefix_sum = [0] * (n + 2)
    for i in range(n + 1):
        prefix_of_prefix_sum[i + 1] = (prefix_of_prefix_sum[i] + prefix_sum[i]) % MODULUS
        
    left_boundary = [-1] * n
    right_boundary = [n] * n
    stack = []
    
    for i in range(n):
        while stack and strength[stack[-1]] > strength[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)
        
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and strength[stack[-1]] >= strength[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)
        
    total_strength = 0
    for i in range(n):
        l = left_boundary[i] + 1
        r = right_boundary[i] - 1
        
        sum_range = (prefix_of_prefix_sum[r + 2] - prefix_of_prefix_sum[i + 1] - (prefix_of_prefix_sum[i + 1] - prefix_of_prefix_sum[l]) * (r - i + 1)) % MODULUS
        
        term = (strength[i] * sum_range) % MODULUS
        total_strength = (total_strength + term) % MODULUS
        
    return (total_strength + MODULUS) % MODULUS

def solve_optimized(strength: list[int]) -> int:
    """
    Args:
        strength: A list of integers representing the strength of wizards.

    Returns:
        The total strength sum modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    n = len(strength)
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MODULUS
        
    prefix_of_prefix_sum = [0] * (n + 2)
    for i in range(n + 1):
        prefix_of_prefix_sum[i + 1] = (prefix_of_prefix_sum[i] + prefix_sum[i]) % MODULUS
        
    left_boundary = [-1] * n
    right_boundary = [n] * n
    stack = []
    
    for i in range(n):
        while stack and strength[stack[-1]] > strength[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)
        
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and strength[stack[-1]] >= strength[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)
        
    total_strength = 0
    for i in range(n):
        l = left_boundary[i] + 1
        r = right_boundary[i] - 1
        
        sum_of_sums = (prefix_of_prefix_sum[r + 2] - prefix_of_prefix_sum[i + 1]) - (prefix_of_prefix_sum[i + 1] - prefix_of_prefix_sum[l]) * (r - i + 1)
        total_strength = (total_strength + strength[i] * sum_of_sums) % MODULUS
        
    return (total_strength + MODULUS) % MODULUS

def solve(strength: list[int]) -> int:
    """
    Args:
        strength: A list of integers representing the strength of wizards.

    Returns:
        The total strength sum modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    n = len(strength)
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MODULUS
        
    prefix_of_prefix_sum = [0] * (n + 2)
    for i in range(n + 1):
        prefix_of_prefix_sum[i + 1] = (prefix_of_prefix_sum[i] + prefix_sum[i]) % MODULUS
        
    left_boundary = [-1] * n
    right_boundary = [n] * n
    stack = []
    
    for i in range(n):
        while stack and strength[stack[-1]] > strength[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)
        
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and strength[stack[-1]] >= strength[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)
        
    total_strength = 0
    for i in range(n):
        l = left_boundary[i] + 1
        r = right_boundary[i] - 1
        
        sum_of_subarrays = (prefix_of_prefix_sum[r + 2] - prefix_of_prefix_sum[i + 1]) - (prefix_of_prefix_sum[i + 1] - prefix_of_prefix_sum[l]) * (r - i + 1)
        total_strength = (total_strength + strength[i] * sum_of_subarrays) % MODULUS
        
    return (total_strength + MODULUS) % MODULUS

def solve(strength: list[int]) -> int:
    """
    Args:
        strength: A list of integers representing the strength of wizards.

    Returns:
        The total strength sum modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    n = len(strength)
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MODULUS
        
    prefix_of_prefix_sum = [0] * (n + 2)
    for i in range(n + 1):
        prefix_of_prefix_sum[i + 1] = (prefix_of_prefix_sum[i] + prefix_sum[i]) % MODULUS
        
    left_boundary = [-1] * n
    right_boundary = [n] * n
    stack = []
    
    for i in range(n):
        while stack and strength[stack[-1]] > strength[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)
        
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and strength[stack[-1]] >= strength[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)
        
    total_strength = 0
    for i in range(n):
        l = left_boundary[i] + 1
        r = right_boundary[i] - 1
        
        sum_of_subarrays = (prefix_of_prefix_sum[r + 2] - prefix_of_prefix_sum[i + 1]) - (prefix_of_prefix_sum[i + 1] - prefix_of_prefix_sum[l]) * (r - i + 1)
        total_strength = (total_strength + strength[i] * sum_of_subarrays) % MODULUS
        
    return (total_strength + MODULUS) % MODULUS

def solve(strength: list[int]) -> int:
    """
    Args:
        strength: A list of integers representing the strength of wizards.

    Returns:
        The total strength sum modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    n = len(strength)
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MODULUS
        
    prefix_of_prefix_sum = [0] * (n + 2)
    for i in range(n + 1):
        prefix_of_prefix_sum[i + 1] = (prefix_of_prefix_sum[i] + prefix_sum[i]) % MODULUS
        
    left_boundary = [-1] * n
    right_boundary = [n] * n
    stack = []
    
    for i in range(n):
        while stack and strength[stack[-1]] > strength[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)
        
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and strength[stack[-1]] >= strength[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)
        
    total_strength = 0
    for i in range(n):
        l = left_boundary[i] + 1
        r = right_boundary[i] - 1
        
        sum_of_subarrays = (prefix_of_prefix_sum[r + 2] - prefix_of_prefix_sum[i + 1]) - (prefix_of_prefix_sum[i + 1] - prefix_of_prefix_sum[l]) * (r - i + 1)
        total_strength = (total_strength + strength[i] * sum_of_subarrays) % MODULUS
        
    return (total_strength + MODULUS) % MODULUS

def solve(strength: list[int]) -> int:
    """
    Args:
        strength: A list of integers representing the strength of wizards.

    Returns:
        The total strength sum modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    n = len(strength)
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MODULUS
        
    prefix_of_prefix_sum = [0] * (n + 2)
    for i in range(n + 1):
        prefix_of_prefix_sum[i + 1] = (prefix_of_prefix_sum[i] + prefix_sum[i]) % MODULUS
        
    left_boundary = [-1] * n
    right_boundary = [n] * n
    stack = []
    
    for i in range(n):
        while stack and strength[stack[-1]] > strength[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)
        
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and strength[stack[-1]] >= strength[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)
        
    total_strength = 0
    for i in range(n):
        l = left_boundary[i] + 1
        r = right_boundary[i] - 1
        
        sum_of_subarrays = (prefix_of_prefix_sum[r + 2] - prefix_of_prefix_sum[i + 1]) - (prefix_of_prefix_sum[i + 1] - prefix_of_prefix_sum[l]) * (r - i + 1)
        total_strength = (total_strength + strength[i] * sum_of_subarrays) % MODULUS
        
    return (total_strength + MODULUS) % MODULUS

def solve(strength: list[int]) -> int:
    """
    Args:
        strength: A list of integers representing the strength of wizards.

    Returns:
        The total strength sum modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    n = len(strength)
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MODULUS
        
    prefix_of_prefix_sum = [0] * (n + 2)
    for i in range(n + 1):
        prefix_of_prefix_sum[i + 1] = (prefix_of_prefix_sum[i] + prefix_sum[i]) % MODULUS
        
    left_boundary = [-1] * n
    right_boundary = [n] * n
    stack = []
    
    for i in range(n):
        while stack and strength[stack[-1]] > strength[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)
        
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and strength[stack[-1]] >= strength[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)
        
    total_strength = 0
    for i in range(n):
        l = left_boundary[i] + 1
        r = right_boundary[i] - 1
        
        sum_of_subarrays = (prefix_of_prefix_sum[r + 2] - prefix_of_prefix_sum[i + 1]) - (prefix_of_prefix_sum[i + 1] - prefix_of_prefix_sum[l]) * (r - i + 1)
        total_strength = (total_strength + strength[i] * sum_of_subarrays) % MODULUS
        
    return (total_strength + MODULUS) % MODULUS

def solve(strength: list[int]) -> int:
    """
    Args:
        strength: A list of integers representing the strength of wizards.

    Returns:
        The total strength sum modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    n = len(strength)
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + strength[i]) % MODULUS
        
    prefix_of_prefix_sum = [0] * (n + 2)
    for i in range(n + 1):
        prefix_of_prefix_sum[i + 1] = (prefix_of_prefix_sum[i] + prefix_sum[i]) % MODULUS
        
    left_boundary = [-1] * n
    right_boundary