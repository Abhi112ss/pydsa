METADATA = {
    "id": 3691,
    "name": "Maximum Total Subarray Value II",
    "slug": "maximum-total-subarray-value-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "segment_tree"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum value of a subarray based on a specific scoring function using optimized dynamic programming.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Args:
        nums: A list of integers representing the array.
        k: An integer parameter used in the scoring function.

    Returns:
        The maximum total subarray value.
    """
    n = len(nums)
    if n == 0:
        return 0

    tree_size = 1
    while tree_size < n:
        tree_size *= 2
    
    max_tree = [-float('inf')] * (2 * tree_size)
    min_tree = [float('inf')] * (2 * tree_size)

    def update(index: int, val: int):
        idx = index + tree_size
        max_tree[idx] = val
        min_tree[idx] = val
        while idx > 1:
            idx //= 2
            max_tree[idx] = max(max_tree[2 * idx], max_tree[2 * idx + 1])
            min_tree[idx] = min(min_tree[2 * idx], min_tree[2 * idx + 1])

    def query_max(l: int, r: int) -> float:
        res = -float('inf')
        l += tree_size
        r += tree_size
        while l < r:
            if l % 2 == 1:
                res = max(res, max_tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = max(res, max_tree[r])
            l //= 2
            r //= 2
        return res

    def query_min(l: int, r: int) -> float:
        res = float('inf')
        l += tree_size
        r += tree_size
        while l < r:
            if l % 2 == 1:
                res = min(res, min_tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = min(res, min_tree[r])
            l //= 2
            r //= 2
        return res

    dp = [0.0] * n
    overall_max = -float('inf')

    for i in range(n):
        current_val = float(nums[i])
        
        if i == 0:
            dp[i] = current_val
        else:
            prev_max = query_max(0, i)
            prev_min = query_min(0, i)
            
            option1 = current_val + prev_max
            option2 = current_val - prev_min
            option3 = current_val
            
            dp[i] = max(option1, option2, option3)
        
        update(i, dp[i])
        overall_max = max(overall_max, dp[i])

    return int(overall_max) if overall_max != -float('inf') else 0