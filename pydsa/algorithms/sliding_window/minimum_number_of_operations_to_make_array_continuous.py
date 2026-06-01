METADATA = {
    "id": 2009,
    "name": "Minimum Number of Operations to Make Array Continuous",
    "slug": "minimum-number-of-operations-to-make-array-continuous",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "sliding_window", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to make an array continuous by replacing elements such that the range of values is at most n-1.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make an array continuous.
    
    An array is continuous if its length is n and the difference between 
    the maximum and minimum elements is at most n - 1.
    
    Args:
        nums: A list of integers.
        
    Returns:
        The minimum number of operations required.
        
    Examples:
        >>> solve([4, 2, 5, 3])
        0
        >>> solve([4, 2, 5, 6])
        1
        >>> solve([1, 4, 1, 1])
        2
    """
    n = len(nums)
    if n <= 1:
        return 0

    # Step 1: Sort and remove duplicates. 
    # Duplicates don't help in expanding the range of unique values,
    # so we treat them as elements that must be replaced.
    sorted_unique = sorted(list(set(nums)))
    m = len(sorted_unique)
    
    max_elements_in_window = 0
    right = 0
    
    # Step 2: Use a sliding window to find the maximum number of existing 
    # elements that can fit into a range of size [start, start + n - 1].
    for left in range(m):
        # The target range end for the current starting element
        target_end = sorted_unique[left] + n - 1
        
        # Expand the right boundary of the window as long as the element 
        # fits within the valid continuous range.
        while right < m and sorted_unique[right] <= target_end:
            right += 1
        
        # The number of elements currently in the valid window is (right - left)
        current_window_size = right - left
        if current_window_size > max_elements_in_window:
            max_elements_in_window = current_window_size
            
    # The minimum operations is the total elements needed (n) 
    # minus the maximum number of elements we can keep.
    return n - max_elements_in_window
