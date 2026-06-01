METADATA = {
    "id": 1793,
    "name": "Maximum Score of a Good Subarray",
    "slug": "maximum-score-of-a-good-subarray",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_stack", "two_pointer"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score of a subarray that contains the index k, where score is min(subarray) * length.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum score of a 'good' subarray containing index k.
    A subarray is good if it includes index k. The score is min(subarray) * length.

    Args:
        nums: A list of integers representing the values.
        k: The required index that must be included in the subarray.

    Returns:
        The maximum score possible for any good subarray.

    Examples:
        >>> solve([1, 4, 3, 7], 0)
        4
        >>> solve([1, 2, 3, 4, 5], 3)
        9
    """
    n = len(nums)
    
    # left_boundary[i] will store the index of the first element to the left of i that is smaller than nums[i]
    left_boundary = [-1] * n
    # right_boundary[i] will store the index of the first element to the right of i that is smaller than nums[i]
    right_boundary = [n] * n
    
    # Monotonic stack to find the nearest smaller element to the left
    stack: list[int] = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)
        
    # Clear stack to reuse for the right side
    stack.clear()
    
    # Monotonic stack to find the nearest smaller element to the right
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)
        
    max_score = 0
    
    # For each element, treat it as the minimum value of a subarray.
    # The largest such subarray is bounded by the nearest smaller elements on both sides.
    for i in range(n):
        # Check if the subarray where nums[i] is the minimum contains index k
        # The range is (left_boundary[i], right_boundary[i]), exclusive.
        # So the subarray is [left_boundary[i] + 1, right_boundary[i] - 1]
        if left_boundary[i] < k < right_boundary[i] or (left_boundary[i] < k < right_boundary[i] is False and (left_boundary[i] < k <= right_boundary[i] - 1 or left_boundary[i] + 1 <= k < right_boundary[i])):
            # Simplified condition: index k must be within the range [left_boundary[i] + 1, right_boundary[i] - 1]
            if left_boundary[i] < k < right_boundary[i]:
                current_length = right_boundary[i] - left_boundary[i] - 1
                max_score = max(max_score, nums[i] * current_length)
                
    # The logic above can be simplified: a subarray where nums[i] is minimum 
    # contains k if and only if left_boundary[i] < k < right_boundary[i].
    # However, the condition is actually: the range [left_boundary[i] + 1, right_boundary[i] - 1] 
    # must contain k.
    
    # Let's re-evaluate the loop for clarity and correctness
    max_score = 0
    for i in range(n):
        start = left_boundary[i] + 1
        end = right_boundary[i] - 1
        if start <= k <= end:
            max_score = max(max_score, nums[i] * (end - start + 1))
            
    return max_score
