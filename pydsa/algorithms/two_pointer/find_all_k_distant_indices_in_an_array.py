METADATA = {
    "id": 2200,
    "name": "Find All K-Distant Indices in an Array",
    "slug": "find-all-k-distant-indices-in-an-array",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n)",
    "description": "Find all indices in the first array such that the absolute difference between the index and any index in the second array is at least k.",
}

def solve(arr1: list[int], arr2: list[int], k: int) -> list[int]:
    """
    Finds all indices in arr1 that are at least k distance away from any index in arr2.

    Args:
        arr1: The first input array.
        arr2: The second input array.
        k: The minimum required distance.

    Returns:
        A list of indices from arr1 that satisfy the distance condition.

    Examples:
        >>> solve([4, 1, 2], [1, 3], 3)
        [0]
        >>> solve([4, 1, 2], [1, 3], 4)
        []
    """
    n = len(arr1)
    m = len(arr2)
    result = []
    
    # Pointer for the current index in arr2 we are comparing against
    arr2_idx = 0
    
    for i in range(n):
        # Move the arr2 pointer forward until we find an index in arr2 
        # that is not 'too far behind' the current index i.
        # We want to find the first index in arr2 such that arr2[arr2_idx] + k > i.
        # However, the condition is |i - j| >= k, which means j <= i - k OR j >= i + k.
        # It is easier to find if there exists ANY j such that |i - j| < k.
        # If such a j exists, i is invalid.
        
        # Advance arr2_idx to the first index that could potentially be within distance k of i
        # i.e., the first index where arr2[arr2_idx] >= i - k + 1
        while arr2_idx < m and arr2[arr2_idx] < i - k + 1:
            arr2_idx += 1
            
        # Now, check if the current arr2_idx is within the 'forbidden' range [i - k + 1, i + k - 1]
        # Since we advanced arr2_idx, we only need to check if the current arr2[arr2_idx] 
        # is less than or equal to i + k - 1.
        is_valid = True
        if arr2_idx < m and arr2[arr2_idx] <= i + k - 1:
            is_valid = False
            
        if is_valid:
            result.append(i)
            
    return result
