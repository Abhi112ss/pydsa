METADATA = {
    "id": 3434,
    "name": "Maximum Frequency After Subarray Operation",
    "slug": "maximum-frequency-after-subarray-operation",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array", "kadane"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum frequency of a target value after applying at most one subarray operation that adds a value to all elements in the subarray.",
}

def solve(nums: list[int], target: int, k: int) -> int:
    """
    Calculates the maximum frequency of the target value after performing 
    at most one subarray operation. An operation consists of choosing a 
    subarray and adding a value 'k' to all its elements.

    Args:
        nums: A list of integers.
        target: The integer we want to maximize the frequency of.
        k: The integer value to be added to a chosen subarray.

    Returns:
        The maximum possible frequency of the target value.

    Examples:
        >>> solve([1, 2, 1, 2, 1], 1, 1)
        4
        >>> solve([4, 3, 2, 3, 4], 4, 1)
        3
    """
    # Initial count of the target value already present in the array.
    # Any operation on a subarray will change some elements to (element + k).
    # If (element + k) == target, we gain a target.
    # If element == target, we lose a target (because target + k != target, unless k=0).
    
    initial_target_count = 0
    for num in nums:
        if num == target:
            initial_target_count += 1

    # We want to find a subarray that maximizes:
    # (count of elements where num + k == target) - (count of elements where num == target)
    # Let's define a new array where:
    # val = 1 if (num + k == target)
    # val = -1 if (num == target)
    # val = 0 otherwise
    # We need to find the maximum subarray sum of this derived array.
    
    # Note: If k == 0, the operation does nothing, so the answer is just initial_target_count.
    if k == 0:
        return initial_target_count

    max_gain = 0
    current_running_gain = 0
    
    # We use Kadane's algorithm to find the maximum subarray sum in one pass.
    for num in nums:
        # Determine the contribution of the current element to the potential gain.
        if num + k == target:
            contribution = 1
        elif num == target:
            contribution = -1
        else:
            contribution = 0
            
        # Kadane's logic: either extend the current subarray or start a new one.
        current_running_gain += contribution
        
        if current_running_gain < 0:
            current_running_gain = 0
            
        if current_running_gain > max_gain:
            max_gain = current_running_gain

    return initial_target_count + max_gain
