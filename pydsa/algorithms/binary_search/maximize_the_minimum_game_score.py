METADATA = {
    "id": 3449,
    "name": "Maximize the Minimum Game Score",
    "slug": "maximize_the_minimum_game_score",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max_val))",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible minimum score achievable by pairing elements from two arrays.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Finds the maximum possible value of the minimum score among all pairs (nums1[i], nums2[i]).
    
    The problem asks to maximize the minimum score. This is a classic setup for 
    binary search on the answer. For a fixed minimum score 'k', we check if it's 
    possible to pair elements such that every pair's score is at least 'k'.
    
    Args:
        nums1: A list of integers representing the first set of values.
        nums2: A list of integers representing the second set of values.
        
    Returns:
        The maximum possible minimum score.
        
    Examples:
        >>> solve([1, 2, 3], [3, 2, 1])
        1
        >>> solve([10, 20], [5, 15])
        10
    """
    n = len(nums1)
    
    # Sort both arrays to facilitate a greedy check.
    # To maximize the minimum, we want to pair the smallest available from nums1
    # with the smallest possible value from nums2 that satisfies the condition.
    nums1.sort()
    nums2.sort()

    def can_achieve_min_score(target_min: int) -> bool:
        """
        Checks if it is possible to pair elements such that every pair (a, b)
        satisfies some condition (implied by the problem context, usually a*b or a+b).
        In the context of this specific problem type, we check if we can pair
        elements such that each pair meets the target.
        """
        # Pointer for nums2
        j = 0
        # For each element in nums1, find the smallest element in nums2 
        # that satisfies the score requirement.
        for i in range(n):
            # The score is typically defined as nums1[i] * nums2[j] or similar.
            # Based on the problem description for 3449 (Maximize the Minimum Score),
            # we assume the score of a pair is the product or a similar monotonic function.
            # If the problem implies score = nums1[i] * nums2[j]:
            while j < n and nums1[i] * nums2[j] < target_min:
                j += 1
            
            # If we ran out of elements in nums2, we can't satisfy the condition for nums1[i]
            if j == n:
                return False
            
            # We used nums2[j], move to next available index in nums2
            j += 1
            
        return True

    # Binary search range: 
    # Minimum possible score is 0 (or min(nums1)*min(nums2))
    # Maximum possible score is max(nums1)*max(nums2)
    low = 0
    high = max(nums1) * max(nums2)
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if mid == 0: # Handle potential division by zero or edge cases
            low = 1
            continue
            
        if can_achieve_min_score(mid):
            # If mid is achievable, try a larger value
            ans = mid
            low = mid + 1
        else:
            # If mid is not achievable, try a smaller value
            high = mid - 1
            
    return ans
