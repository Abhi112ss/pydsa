METADATA = {
    "id": 2866,
    "name": "Beautiful Towers II",
    "slug": "beautiful-towers-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["arrays", "monotonic_stack", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum total height of a beautiful tower by selecting a peak index and ensuring heights are non-decreasing to the left and non-increasing to the right.",
}

def solve(heights: list[int]) -> int:
    """
    Calculates the maximum height of a beautiful tower.
    
    A beautiful tower is defined by a peak index 'i' such that for all 
    j < k < i, heights[j] <= heights[k], and for all i < j < k, 
    heights[j] >= heights[k]. The actual height at any index is 
    constrained by the minimum height encountered from the peak.

    Args:
        heights: A list of integers representing the initial heights.

    Returns:
        The maximum possible total height of a beautiful tower.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        15
        >>> solve([5, 4, 3, 2, 1])
        15
        >>> solve([1, 3, 2, 4, 1])
        10
    """
    n = len(heights)
    if n == 0:
        return 0

    def get_max_prefix_sums(arr: list[int]) -> list[int]:
        """
        Computes the maximum possible sum of heights for a non-decreasing 
        sequence ending at each index using a monotonic stack.
        """
        m = len(arr)
        prefix_sums = [0] * m
        stack = []  # Stores indices of elements in increasing order
        current_running_sum = 0

        for i in range(m):
            # Maintain a monotonic increasing stack
            while stack and arr[stack[-1]] > arr[i]:
                last_idx = stack.pop()
                # Calculate how many elements were previously 'capped' by the popped element
                prev_idx = stack[-1] if stack else -1
                # Subtract the contribution of the popped element's height
                # and replace it with the current (smaller) height
                current_running_sum -= (last_idx - prev_idx) * arr[last_idx]
            
            # Calculate the contribution of the current element
            prev_idx = stack[-1] if stack else -1
            current_running_sum += (i - prev_idx) * arr[i]
            
            # Note: The logic above is slightly flawed for a simple running sum.
            # Let's use the standard DP + Monotonic Stack approach:
            # prefix_sums[i] = prefix_sums[prev_idx] + (i - prev_idx) * arr[i]
            stack.append(i)
        
        # Re-implementing correctly for clarity and correctness
        stack = []
        dp = [0] * m
        for i in range(m):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if not stack:
                dp[i] = (i + 1) * arr[i]
            else:
                prev_idx = stack[-1]
                dp[i] = dp[prev_idx] + (i - prev_idx) * arr[i]
            stack.append(i)
        return dp

    # Calculate max sum for non-decreasing sequence from left to peak
    left_sums = get_max_prefix_sums(heights)
    
    # Calculate max sum for non-increasing sequence from right to peak
    # This is equivalent to non-decreasing from right to left
    right_sums = get_max_prefix_sums(heights[::-1])[::-1]

    max_total_height = 0
    for i in range(n):
        # Total height = sum(left) + sum(right) - heights[i] (since peak is counted twice)
        # However, the DP approach calculates the sum of the sequence ending/starting at i.
        # The sequence is: [non-decreasing up to i] + [non-increasing from i]
        current_height = left_sums[i] + right_sums[i] - heights[i]
        if current_height > max_total_height:
            max_total_height = current_height

    return max_total_height
