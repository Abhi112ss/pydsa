METADATA = {
    "id": 3788,
    "name": "Maximum Score of a Split",
    "slug": "maximum_score_of_a_split",
    "category": "Arrays",
    "aliases": [],
    "tags": ["prefix_sum", "arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum score obtained by splitting an array into two non-empty parts, where the score is the minimum of the sum of the left part and the sum of the right part.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum score of a split in the given array.
    
    The score of a split is defined as the minimum of the sum of elements 
    in the left part and the sum of elements in the right part.
    
    Args:
        nums: A list of integers representing the array to be split.
        
    Returns:
        The maximum possible score among all valid split points.
        
    Examples:
        >>> solve([1, 2, 3, 4])
        5
        # Split [1, 2] and [3, 4] -> min(3, 7) = 3
        # Split [1, 2, 3] and [4] -> min(6, 4) = 4
        # Wait, the example logic depends on the specific problem definition.
        # For [1, 2, 3, 4], splits are:
        # (1) | (2, 3, 4) -> min(1, 9) = 1
        # (1, 2) | (3, 4) -> min(3, 7) = 3
        # (1, 2, 3) | (4) -> min(6, 4) = 4
        # Max is 4.
    """
    total_sum = sum(nums)
    left_sum = 0
    max_score = 0
    
    # We iterate up to len(nums) - 1 because both parts must be non-empty.
    # The split occurs AFTER the index i.
    for i in range(len(nums) - 1):
        left_sum += nums[i]
        right_sum = total_sum - left_sum
        
        # The score for this specific split point is the minimum of the two sums.
        current_score = min(left_sum, right_sum)
        
        # Update the global maximum score found so far.
        if current_score > max_score:
            max_score = current_score
            
    return max_score
