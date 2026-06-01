METADATA = {
    "id": 2429,
    "name": "Minimize XOR",
    "slug": "minimize_xor",
    "category": "Greedy",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum XOR value between any two elements in an array by checking adjacent elements in a sorted version of the array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum XOR value between any two elements in the given list.

    The key insight is that for any two numbers, their XOR value is minimized 
    when they are close in value. In a sorted array, the minimum XOR pair 
    is guaranteed to be adjacent.

    Args:
        nums: A list of integers.

    Returns:
        The minimum XOR value found between any two elements.

    Examples:
        >>> solve([1, 2, 3])
        1
        >>> solve([10, 5, 2, 7])
        2
    """
    # Sort the array to bring numbers with similar bit patterns closer together
    nums.sort()
    
    # Initialize min_xor with a value larger than any possible XOR result
    # Since nums[i] <= 10^9, 2^30 is a safe upper bound
    min_xor = float('inf')
    
    # Iterate through the sorted array and check XOR of adjacent elements
    for i in range(len(nums) - 1):
        current_xor = nums[i] ^ nums[i + 1]
        if current_xor < min_xor:
            min_xor = current_xor
            
        # Optimization: if we find 0, it's the absolute minimum possible
        if min_xor == 0:
            return 0
            
    return int(min_xor)
