METADATA = {
    "id": 3011,
    "name": "Find if Array Can Be Sorted",
    "slug": "find-if-array-can-be-sorted",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine if an array can be sorted by performing at most one operation where all elements at even indices are rearranged.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the array can be sorted by rearranging elements at even indices.
    
    The problem allows us to pick all elements at even indices (0, 2, 4...) 
    and rearrange them in any order. The elements at odd indices (1, 3, 5...) 
    must remain in their original positions.
    
    Args:
        nums: A list of integers.
        
    Returns:
        True if the array can be sorted by rearranging even-indexed elements, 
        False otherwise.
        
    Examples:
        >>> solve([3, 2, 1, 4])
        True
        >>> solve([1, 2, 3, 4])
        True
        >>> solve([1, 3, 2, 4])
        False
    """
    n = len(nums)
    if n <= 2:
        return True

    # Step 1: Extract all elements located at even indices.
    # These are the elements we are allowed to rearrange.
    even_indexed_elements = [nums[i] for i in range(0, n, 2)]
    even_indexed_elements.sort()

    # Step 2: Construct the "best possible" array.
    # We place the sorted even-indexed elements back into the even positions,
    # while keeping the odd-indexed elements exactly where they were.
    reconstructed_array = [0] * n
    even_ptr = 0
    for i in range(n):
        if i % 2 == 0:
            reconstructed_array[i] = even_indexed_elements[even_ptr]
            even_ptr += 1
        else:
            reconstructed_array[i] = nums[i]

    # Step 3: Check if the resulting reconstructed array is sorted.
    # If the array is sorted after our optimal rearrangement, return True.
    for i in range(n - 1):
        if reconstructed_array[i] > reconstructed_array[i + 1]:
            return False

    return True
