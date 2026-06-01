METADATA = {
    "id": 2834,
    "name": "Find the Minimum Possible Sum of a Beautiful Array",
    "slug": "find-the-minimum-possible-sum-of-a-beautiful-array",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum possible sum of an array of length n where no two elements are equal and no element is a multiple of another.",
}

def solve(n: int) -> int:
    """
    Args:
        n: The length of the array.

    Returns:
        The minimum possible sum of a beautiful array of length n.
    """
    if n <= 0:
        return 0

    start_value = (n // 2) + 1
    total_sum = 0
    
    for i in range(n):
        total_sum += (start_value + i)
        
    return total_sum