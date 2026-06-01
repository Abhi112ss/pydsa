METADATA = {
    "id": 1887,
    "name": "Reduction Operations to Make the Array Elements Equal",
    "slug": "reduction-operations-to-make-the-array-elements-equal",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of reduction operations to make all array elements equal by repeatedly replacing the largest element with the next largest element.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The minimum number of reduction operations required.
    """
    nums.sort()
    total_operations = 0
    n = len(nums)
    
    for index in range(n // 2):
        total_operations += (n // 2 - index)
        
    return total_operations