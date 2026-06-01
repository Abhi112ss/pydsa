METADATA = {
    "id": 3221,
    "name": "Maximum Array Hopping Score II",
    "slug": "maximum-array-hopping-score-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score achievable by hopping through an array where each jump's score depends on the value at the destination.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum score achievable by hopping through the array.
    
    A jump can be made from index i to any index j such that i < j <= i + k.
    The score of a jump is the value of the element at the destination index.
    
    Args:
        nums: A list of integers representing the values at each index.
        k: The maximum jump distance.
        
    Returns:
        The maximum total score starting from index 0 and ending at the last index.
        
    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        14
        >>> solve([10, 2, 3, 10], 1)
        25
    """
    n = len(nums)
    if n == 0:
        return 0
        
    # dp[i] stores the maximum score to reach index i starting from index 0.
    # We initialize with a very small number to represent unreachable states,
    # except for the starting index.
    dp = [-float('inf')] * n
    dp[0] = nums[0]
    
    # To achieve O(n) time complexity, we need to efficiently find the 
    # maximum dp[j] in the range [i-k, i-1]. 
    # A sliding window maximum approach using a deque is optimal.
    from collections import deque
    
    # deque will store indices of dp such that dp[indices] are in descending order.
    # This allows us to get the max dp value in the current window in O(1).
    max_deque = deque([0])
    
    for i in range(1, n):
        # 1. Remove indices from the front of the deque that are out of the window [i-k, i-1]
        if max_deque and max_deque[0] < i - k:
            max_deque.popleft()
            
        # 2. The maximum dp value in the window is at the front of the deque.
        # The score at index i is the max score from a previous index + nums[i].
        if max_deque:
            best_prev_idx = max_deque[0]
            dp[i] = dp[best_prev_idx] + nums[i]
            
        # 3. Maintain the deque property: elements are in descending order of dp values.
        # Before adding the current dp[i], remove all indices with smaller dp values.
        if dp[i] != -float('inf'):
            while max_deque and dp[max_deque[-1]] <= dp[i]:
                max_deque.pop()
            max_deque.append(i)
            
    return int(dp[n - 1])
