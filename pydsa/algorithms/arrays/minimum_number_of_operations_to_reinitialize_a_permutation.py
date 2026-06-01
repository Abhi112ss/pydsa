METADATA = {
    "id": 1806,
    "name": "Minimum Number of Operations to Reinitialize a Permutation",
    "slug": "minimum-number-of-operations-to-reinitialize-a-permutation",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "permutation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to reinitialize a permutation by counting consecutive matching elements.",
}

def solve(nums: list[int], target: list[int]) -> int:
    """
    Calculates the minimum number of operations to reinitialize the permutation.

    An operation consists of replacing the current permutation with the next 
    cyclic shift of the original permutation.

    Args:
        nums: The current permutation of integers.
        target: The target permutation to match.

    Returns:
        The minimum number of operations required to make nums equal to target.

    Examples:
        >>> solve([4, 3, 2, 1], [4, 3, 2, 1])
        0
        >>> solve([4, 3, 2, 1], [1, 4, 3, 2])
        1
        >>> solve([4, 3, 2, 1], [2, 1, 4, 3])
        2
    """
    n = len(nums)
    operations = 0
    
    # We iterate through the possible number of shifts (0 to n-1)
    # Each shift moves the starting index by 'operations'
    for shift in range(n):
        is_match = True
        
        # Check if the current shift matches the target permutation
        for i in range(n):
            # The element in the shifted array is at index (i + shift) % n
            if nums[(i + shift) % n] != target[i]:
                is_match = False
                break
        
        # If we found a match, return the number of shifts performed
        if is_match:
            return shift
            
    return n

# Note: The problem can also be solved by finding the first index 'i' 
# where nums[i] != target[i] and checking if the cyclic shift works.
# However, the O(n^2) approach above is acceptable given n <= 100.
# For a true O(n) approach, we find the first mismatch and verify the shift.

def solve_optimal(nums: list[int], target: list[int]) -> int:
    """
    An optimized O(n) implementation.
    
    Args:
        nums: The current permutation.
        target: The target permutation.

    Returns:
        The minimum number of operations.
    """
    n = len(nums)
    
    # 1. Find the first index where the elements do not match
    first_mismatch = -1
    for i in range(n):
        if nums[i] != target[i]:
            first_mismatch = i
            break
            
    # If no mismatch is found, 0 operations are needed
    if first_mismatch == -1:
        return 0
        
    # 2. The number of operations must be the index of the first mismatch
    # because the elements are a cyclic shift.
    # We verify if shifting by 'first_mismatch' actually aligns the arrays.
    # In this specific problem, the shift is guaranteed to be valid if it exists.
    
    # Check if the shift works
    for i in range(n):
        if nums[(i + first_mismatch) % n] != target[i]:
            # This case shouldn't be reachable given problem constraints 
            # if a solution is guaranteed, but we handle it for robustness.
            return -1 
            
    return first_mismatch

# Re-assigning solve to the optimal version for the final export
solve = solve_optimal