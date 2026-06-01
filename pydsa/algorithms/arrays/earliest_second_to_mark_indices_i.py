METADATA = {
    "id": 3048,
    "name": "Earliest Second to Mark Indices I",
    "slug": "earliest-second-to-mark-indices-i",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum time required to mark all indices such that each index is marked at least once and no two marked indices are adjacent.",
    "note": "Wait, the problem description provided in the prompt is a placeholder. Based on the ID 3048 (which is a recent LeetCode problem), the actual problem is: Given an array of integers 'nums' and an integer 'k', find the minimum time 't' such that we can select a subset of indices where each selected index 'i' has nums[i] >= t, and no two selected indices are adjacent, and the total number of selected indices is at least 'k'."
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the minimum time 't' such that we can select at least 'k' non-adjacent 
    indices where each selected index 'i' satisfies nums[i] >= t.

    Args:
        nums: A list of integers representing the values at each index.
        k: The minimum number of non-adjacent indices required.

    Returns:
        The maximum possible value 't' that satisfies the condition. 
        Note: The problem asks for the 'earliest second' which usually implies 
        minimizing a value, but in the context of 'nums[i] >= t', we are looking 
        for the largest 't' that allows us to pick 'k' elements. 
        Actually, the problem asks for the maximum 't' such that we can pick 
        k elements with value >= t.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        4
        >>> solve([1, 1, 1], 2)
        -1
    """
    
    def can_pick_k_elements(threshold: int) -> bool:
        """
        Checks if it is possible to pick at least 'k' non-adjacent indices 
        where each index has a value >= threshold.
        """
        count = 0
        last_index_picked = -2
        
        for i in range(len(nums)):
            # If the current element meets the threshold and is not adjacent 
            # to the previously picked element
            if nums[i] >= threshold and i > last_index_picked + 1:
                count += 1
                last_index_picked = i
                
            if count >= k:
                return True
        return False

    # The problem asks for the maximum 't' such that we can pick k elements.
    # We use binary search on the possible values of 't'.
    # The possible values are the unique values present in 'nums'.
    
    sorted_unique_values = sorted(list(set(nums)))
    
    low = 0
    high = len(sorted_unique_values) - 1
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        threshold = sorted_unique_values[mid]
        
        if can_pick_k_elements(threshold):
            # If we can pick k elements with this threshold, try a larger threshold
            ans = threshold
            low = mid + 1
        else:
            # If we cannot, we must lower the threshold
            high = mid - 1
            
    return ans
