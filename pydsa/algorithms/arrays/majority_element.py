METADATA = {
    "id": 169,
    "name": "Majority Element",
    "slug": "majority-element",
    "category": "array",
    "aliases": ["majority_element"],
    "tags": ["boyer_moore", "hash_map", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the majority element in an array that appears more than n/2 times.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the majority element in an array using Boyer-Moore Voting Algorithm.
    
    Args:
        nums: List of integers where majority element exists (appears > n/2 times)
        
    Returns:
        The majority element
        
    Examples:
        >>> solve([3,2,3])
        3
        >>> solve([2,2,1,1,1,2,2])
        2
    """
    candidate = None
    count = 0
    
    # Traverse the array to find potential majority candidate
    for num in nums:
        # If count is 0, set current element as new candidate
        if count == 0:
            candidate = num
            count = 1
        # If current element matches candidate, increment count
        elif num == candidate:
            count += 1
        # Otherwise, decrement count
        else:
            count -= 1
    
    # Since majority element is guaranteed to exist, return candidate
    return candidate