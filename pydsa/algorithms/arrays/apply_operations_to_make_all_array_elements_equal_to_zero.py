METADATA = {
    "id": 2772,
    "name": "Apply Operations to Make All Array Elements Equal to Zero",
    "slug": "apply-operations-to-make-all-array-elements-equal-to-zero",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of operations required to make all elements in an array zero by applying a specific transformation rule.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations required to make all elements zero.
    """
    operations_count = 0
    array_length = len(nums)
    
    for index in range(array_length):
        if nums[index] != 0:
            operations_count += 1
            nums[index] = 0
            
            if index + 1 < array_length:
                nums[index + 1] = 0
                
    return operations_count