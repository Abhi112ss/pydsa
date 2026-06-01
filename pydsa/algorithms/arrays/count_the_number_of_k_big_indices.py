METADATA = {
    "id": 2519,
    "name": "Count the Number of K-Big Indices",
    "slug": "count-the-number-of-k-big-indices",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "suffix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count indices where the sum of elements to the left is strictly greater than the sum of elements to the right.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Args:
        nums: A list of integers.
        k: An integer representing the starting index to consider.

    Returns:
        The count of k-big indices.
    """
    total_sum = sum(nums)
    left_sum = 0
    k_big_count = 0
    
    for index in range(len(nums)):
        right_sum = total_sum - left_sum - nums[index]
        
        if index >= k and left_sum > right_sum:
            k_big_count += 1
            
        left_sum += nums[index]
        
    return k_big_count