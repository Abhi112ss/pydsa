METADATA = {
    "id": 2997,
    "name": "Minimum Number of Operations to Make Array XOR Equal to K",
    "slug": "minimum-number-of-operations-to-make-array-xor-equal-to-k",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make the XOR sum of an array equal to k by changing elements to any non-negative integer.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum number of operations to make the XOR sum of the array equal to k.
    
    An operation consists of replacing any element in the array with any non-negative integer.
    If the current XOR sum is already k, 0 operations are needed.
    If the current XOR sum is not k, we can change exactly one element to make the 
    total XOR sum equal to k.

    Args:
        nums: A list of non-negative integers.
        k: The target XOR sum.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 3], 1)
        0
        >>> solve([1, 2, 3], 4)
        1
        >>> solve([1, 1, 1], 0)
        1
    """
    current_xor_sum = 0
    
    # Calculate the XOR sum of all elements in the array
    for num in nums:
        current_xor_sum ^= num
        
    # If the current XOR sum matches the target k, no changes are needed
    if current_xor_sum == k:
        return 0
    
    # If current_xor_sum != k, we can always pick one element 'x' 
    # and replace it with 'x ^ current_xor_sum ^ k'.
    # This single change will make the total XOR sum equal to k.
    return 1
