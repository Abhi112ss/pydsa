METADATA = {
    "id": 2098,
    "name": "Subsequence of Size K With the Largest Even Sum",
    "slug": "subsequence-of-size-k-with-the-largest-even-sum",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the largest even sum of a subsequence of size k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the largest even sum of a subsequence of size k.

    Args:
        nums: A list of integers.
        k: The required size of the subsequence.

    Returns:
        The largest even sum possible, or -1 if no such subsequence exists.

    Examples:
        >>> solve([2, 4, 3, 5, 7], 3)
        14
        >>> solve([1, 2, 3, 4, 5], 2)
        6
        >>> solve([1, 3, 5], 2)
        -1
    """
    # Sort numbers in descending order to greedily pick the largest elements
    nums.sort(reverse=True)
    
    current_sum = 0
    odd_elements = []
    even_elements = []
    
    # Pick the k largest elements
    for i in range(k):
        val = nums[i]
        current_sum += val
        if val % 2 == 0:
            even_elements.append(val)
        else:
            odd_elements.append(val)
            
    # If the sum is already even, it's the maximum possible even sum
    if current_sum % 2 == 0:
        return current_sum
    
    # If the sum is odd, we need to swap one element to change parity
    # We have two options to make the sum even:
    # 1. Replace the smallest odd element in the top k with the largest even element outside top k
    # 2. Replace the smallest even element in the top k with the largest odd element outside top k
    
    # Find the smallest odd/even in the current selection (last elements of the lists)
    # and the largest odd/even outside the selection (first elements in the remaining nums)
    
    min_odd_in = odd_elements[-1] if odd_elements else float('inf')
    min_even_in = even_elements[-1] if even_elements else float('inf')
    
    max_odd_out = float('-inf')
    max_even_out = float('-inf')
    
    # Search for the best candidates outside the top k
    for i in range(k, len(nums)):
        val = nums[i]
        if val % 2 == 0:
            if val > max_even_out:
                max_even_out = val
        else:
            if val > max_odd_out:
                max_odd_out = val
                
    # Option 1: Remove smallest odd, add largest even
    option1 = float('-inf')
    if min_odd_in != float('inf') and max_even_out != float('-inf'):
        option1 = current_sum - min_odd_in + max_even_out
        
    # Option 2: Remove smallest even, add largest odd
    option2 = float('-inf')
    if min_even_in != float('inf') and max_odd_out != float('-inf'):
        option2 = current_sum - min_even_in + max_odd_out
        
    result = max(option1, option2)
    
    return int(result) if result != float('-inf') else -1
