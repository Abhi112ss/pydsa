METADATA = {
    "id": 2541,
    "name": "Minimum Operations to Make Array Equal II",
    "slug": "minimum-operations-to-make-array-equal-ii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make all elements in an array equal, where an operation consists of incrementing one element and decrementing another.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make all elements in the array equal.
    
    An operation consists of picking two indices i and j, incrementing nums[i] 
    and decrementing nums[j]. This preserves the sum of the array. To minimize 
    the operations, we aim to make all elements equal to the median.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 3])
        1
        >>> solve([1, 1, 1, 1])
        0
        >>> solve([1, 10, 100])
        99
    """
    # Sort the array to easily find the median and use two pointers
    nums.sort()
    
    n = len(nums)
    left_pointer = 0
    right_pointer = n - 1
    total_operations = 0
    
    # The optimal target value is the median. 
    # In a sorted array, the median is at index n // 2.
    # We can use a two-pointer approach to calculate the distance 
    # of elements from the median.
    while left_pointer < right_pointer:
        # To make nums[left_pointer] and nums[right_pointer] equal to the median,
        # we must perform (nums[right_pointer] - nums[left_pointer]) operations.
        # Specifically, we increment the smaller and decrement the larger.
        total_operations += nums[right_pointer] - nums[left_pointer]
        
        left_pointer += 1
        right_pointer -= 1
        
    return total_operations
