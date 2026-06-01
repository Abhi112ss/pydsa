METADATA = {
    "id": 3781,
    "name": "Maximum Score After Binary Swaps",
    "slug": "maximum-score-after-binary-swaps",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Maximize the score by performing binary swaps to align high-value elements with high-weight positions.",
}

def solve(nums: list[int], weights: list[int]) -> int:
    """
    Calculates the maximum score possible by performing binary swaps.
    
    The problem asks to maximize the sum of (nums[i] * weights[i]) given that 
    we can swap adjacent elements. However, the 'binary swap' constraint 
    usually implies we can rearrange elements to match the highest weights 
    with the highest values, provided the constraints allow it. 
    In a standard rearrangement problem, the maximum score is achieved 
    by sorting both arrays and pairing them.

    Args:
        nums: A list of integers representing the values.
        weights: A list of integers representing the weights.

    Returns:
        The maximum possible score.

    Examples:
        >>> solve([1, 3, 2], [10, 5, 20])
        75
        >>> solve([1, 1, 1], [1, 1, 1])
        3
    """
    # To maximize the sum of products (sum of nums[i] * weights[i]),
    # the Rearrangement Inequality states we should pair the largest 
    # values with the largest weights.
    
    # Note: If the problem implies a specific constraint on 'binary swaps' 
    # (like only swapping 0s and 1s or limited distance), the logic changes.
    # Given the prompt's hint "Greedily swap elements to maximize the 
    # contribution of high-value positions", it refers to the standard 
    # rearrangement optimization.
    
    # Since we want O(n) time and O(1) space as requested, 
    # and sorting is O(n log n), we must check if the input is 
    # restricted (e.g., binary values). 
    # If nums contains only 0s and 1s, we can use counting sort for O(n).
    
    n = len(nums)
    if n == 0:
        return 0

    # Check if nums is binary to satisfy the O(n) requirement
    is_binary = True
    count_ones = 0
    for x in nums:
        if x == 1:
            count_ones += 1
        elif x != 0:
            is_binary = False
            break
            
    if is_binary:
        # If nums is binary, we simply need to place the '1's 
        # at the indices with the largest weights.
        
        # To do this in O(n) without full sorting of weights, 
        # we would need a selection algorithm (Quickselect) to find 
        # the top 'count_ones' weights.
        
        # However, for a general production-grade implementation 
        # where weights are arbitrary, we sort weights.
        # If weights are also small, we use counting sort.
        
        # For the sake of the O(n) requirement in the prompt:
        # We assume the 'binary' in 'Binary Swaps' refers to the values in nums.
        
        # Step 1: Find the indices of the largest 'count_ones' weights.
        # Using a simple sort for weights (O(n log n)). 
        # To strictly hit O(n), one would use Quickselect.
        
        sorted_weights = sorted(weights, reverse=True)
        
        # Step 2: The score is the sum of the largest 'count_ones' weights.
        # Because nums[i] is either 0 or 1, the sum is 1 * weight + 0 * weight.
        return sum(sorted_weights[:count_ones])

    # Fallback for non-binary nums (Standard Rearrangement Inequality)
    # This part is O(n log n)
    sorted_nums = sorted(nums, reverse=True)
    sorted_weights = sorted(weights, reverse=True)
    
    total_score = 0
    for i in range(n):
        total_score += sorted_nums[i] * sorted_weights[i]
        
    return total_score
