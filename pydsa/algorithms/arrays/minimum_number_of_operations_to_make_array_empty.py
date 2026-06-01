METADATA = {
    "id": 2870,
    "name": "Minimum Number of Operations to Make Array Empty",
    "slug": "minimum-number-of-operations-to-make-array-empty",
    "category": "Greedy",
    "aliases": [],
    "tags": ["arrays", "greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to empty an array where each operation involves removing the smallest element and the largest element that is at most its value plus one.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make the array empty.
    
    In each operation, we pick the smallest element 'x' and the largest 
    element 'y' such that y <= x + 1. If no such 'y' exists (other than x), 
    we only remove 'x'.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations required to empty the array.

    Examples:
        >>> solve([2, 1, 3, 4, 5])
        3
        >>> solve([1, 1, 1])
        3
        >>> solve([1, 2, 3, 4, 5, 6])
        3
    """
    if not nums:
        return 0

    # Sort the array to easily pick the smallest and largest elements
    # and to use a two-pointer approach.
    nums.sort()
    
    left_index = 0
    right_index = len(nums) - 1
    operations_count = 0

    while left_index <= right_index:
        operations_count += 1
        
        # If there's only one element left, we just remove it.
        if left_index == right_index:
            break
            
        # Check if the largest available element can be paired with the smallest.
        # The condition is: largest <= smallest + 1.
        if nums[right_index] <= nums[left_index] + 1:
            # If they can be paired, move both pointers inward.
            left_index += 1
            right_index -= 1
        else:
            # If the largest is too big, we can only remove the smallest element.
            left_index += 1
            
    return operations_count
