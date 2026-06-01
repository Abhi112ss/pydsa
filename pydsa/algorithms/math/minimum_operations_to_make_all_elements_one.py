METADATA = {
    "id": 2654,
    "name": "Minimum Number of Operations to Make All Array Elements Equal to 1",
    "slug": "minimum-number-of-operations-to-make-all-array-elements-equal-to-1",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make all elements in an array equal to 1 using specific mathematical operations.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations required to make all elements equal to 1.
    """
    total_operations = 0
    for value in nums:
        if value == 1:
            continue
        
        current_value = value
        count = 0
        
        while current_value > 1:
            if current_value % 2 == 0:
                current_value //= 2
            else:
                current_value -= 1
            count += 1
            
        total_operations += count
        
    return total_operations