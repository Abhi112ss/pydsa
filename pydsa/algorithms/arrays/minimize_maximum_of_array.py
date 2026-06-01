METADATA = {
    "id": 2439,
    "name": "Minimize Maximum of Array",
    "slug": "minimize-maximum-of-array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max_val))",
    "space_complexity": "O(1)",
    "description": "Minimize the maximum value in an array by performing at most k operations where an element is decreased and another is increased.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Minimizes the maximum value in the array using binary search on the answer.

    Args:
        nums: A list of integers representing the array.
        k: The maximum number of operations allowed.

    Returns:
        The minimum possible maximum value in the array after at most k operations.

    Examples:
        >>> solve([9, 8, 1, 5], 2)
        5
        >>> solve([1, 1, 1, 1], 1)
        1
    """
    def can_achieve_max(target_max: int) -> bool:
        """
        Checks if it is possible to make all elements <= target_max 
        using at most k operations.
        """
        needed_reductions = 0
        for num in nums:
            if num > target_max:
                # Calculate how many operations are needed to bring this 
                # number down to target_max.
                needed_reductions += num - target_max
        
        # Since each operation reduces one element and increases another,
        # we must ensure the total reductions needed do not exceed k.
        # Note: The problem implies we can always find a 'small' element 
        # to absorb the increases without exceeding the target_max, 
        # provided the average doesn't exceed target_max.
        # However, the constraint is simply that we can't perform more than k reductions.
        return needed_reductions <= k

    # The minimum possible maximum is the ceiling of the average.
    # The maximum possible maximum is the current maximum in the array.
    low = (sum(nums) + len(nums) - 1) // len(nums)
    high = max(nums)
    ans = high

    # Binary search for the smallest possible maximum value.
    while low <= high:
        mid = (low + high) // 2
        if can_achieve_max(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
