METADATA = {
    "id": 1909,
    "name": "Remove One Element to Make the Array Strictly Increasing",
    "slug": "remove-one-element-to-make-the-array-strictly-increasing",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array can become strictly increasing by removing at most one element.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the array can be made strictly increasing by removing at most one element.

    Args:
        nums: A list of integers.

    Returns:
        True if the array can be made strictly increasing by removing one element, False otherwise.

    Examples:
        >>> solve([1, 2, 10, 5, 7])
        True
        >>> solve([2, 3, 1, 2])
        False
        >>> solve([1, 1, 1])
        False
    """
    violation_count = 0
    index_of_violation = -1

    # Step 1: Find the first occurrence where the strictly increasing property is violated
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            violation_count += 1
            index_of_violation = i
            
            # If more than one violation is found, it's impossible to fix with one removal
            if violation_count > 1:
                return False

    # If no violations were found, the array is already strictly increasing
    if violation_count == 0:
        return True

    # Step 2: Check if removing either nums[i] or nums[i+1] fixes the array
    # i is the index of the first element in the violation pair (nums[i], nums[i+1])
    i = index_of_violation
    
    # Case A: Try removing nums[i]
    # This is valid if i is the first element (index 0) OR if the previous element 
    # is smaller than the element after the violation (nums[i-1] < nums[i+1])
    can_remove_current = (i == 0) or (nums[i - 1] < nums[i + 1])
    
    # Case B: Try removing nums[i+1]
    # This is valid if i+1 is the last element OR if the current element 
    # is smaller than the element after the violation (nums[i] < nums[i+2])
    can_remove_next = (i + 1 == len(nums) - 1) or (nums[i] < nums[i + 2])

    return can_remove_current or can_remove_next
