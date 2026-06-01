METADATA = {
    "id": 3315,
    "name": "Construct the Minimum Bitwise Array II",
    "slug": "construct-the-minimum-bitwise-array-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["bit_manipulation", "dp"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(n)",
    "description": "Construct the lexicographically smallest array satisfying bitwise constraints using dynamic programming.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Args:
        nums: A list of integers representing the constraints.
        k: The target number of elements in the resulting array.

    Returns:
        A list of k integers that form the lexicographically smallest array.
    """
    n = len(nums)
    dp = [float('inf')] * (n + 1)
    dp[n] = 0
    
    next_index = [-1] * (n + 1)
    
    for i in range(n - 1, -1, -1):
        current_val = nums[i]
        
        low = i + 1
        high = n
        best_j = -1
        
        while low <= high:
            mid = (low + high) // 2
            if mid <= n:
                if dp[mid] != float('inf'):
                    best_j = mid
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                high = mid - 1
        
        if best_j != -1:
            dp[i] = current_val + dp[best_j]
            next_index[i] = best_j

    result = []
    current_pos = 0
    
    for _ in range(k):
        best_val = float('inf')
        best_idx = -1
        
        for i in range(current_pos, n):
            if dp[i] != float('inf'):
                if nums[i] < best_val:
                    best_val = nums[i]
                    best_idx = i
                elif nums[i] == best_val:
                    if best_idx == -1 or i < best_idx:
                        best_idx = i
        
        if best_idx == -1:
            break
            
        result.append(nums[best_idx])
        current_pos = best_idx + 1
        
    return result