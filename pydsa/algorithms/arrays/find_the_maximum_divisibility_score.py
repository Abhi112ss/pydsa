METADATA = {
    "id": 2644,
    "name": "Find the Maximum Divisibility Score",
    "slug": "find-the-maximum-divisibility-score",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum divisibility score by choosing a subset of elements and assigning them to indices such that each element is divisible by its assigned index.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum divisibility score for a subset of size k.
    
    The divisibility score is defined as the sum of (nums[i] // index_i) 
    for all elements in the chosen subset, where index_i is the 1-based 
    position in the subset. To maximize this, we want to pair larger 
    numbers with smaller indices.

    Args:
        nums: A list of integers.
        k: The size of the subset to choose.

    Returns:
        The maximum possible divisibility score.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        6
        >>> solve([10, 2, 5], 2)
        11
    """
    # To maximize the sum of (nums[i] // index), we should pair the 
    # largest available numbers with the smallest possible indices (1, 2, ...).
    # Sorting in descending order allows us to greedily pick the largest 
    # numbers for the smallest indices.
    nums.sort(reverse=True)
    
    max_score = 0
    
    # We pick the top k largest elements.
    # The largest element gets index 1, the second largest gets index 2, etc.
    for i in range(k):
        # i + 1 represents the 1-based index in the subset
        max_score += nums[i] // (i + 1)
        
    return max_score
