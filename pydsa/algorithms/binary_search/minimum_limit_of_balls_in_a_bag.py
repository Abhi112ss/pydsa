METADATA = {
    "id": 1760,
    "name": "Minimum Limit of Balls in a Bag",
    "slug": "minimum-limit-of-balls-in-a-bag",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max(balls)))",
    "space_complexity": "O(1)",
    "description": "Find the minimum possible maximum number of balls in any bag after performing at most 'extra_lives' operations.",
}

def solve(balls: list[int], extra_lives: int) -> int:
    """
    Args:
        balls: A list of integers representing the number of balls in each bag.
        extra_lives: The maximum number of operations allowed to reduce the number of balls in bags.

    Returns:
        The minimum possible maximum number of balls in any bag.
    """
    def can_achieve_limit(limit: int) -> bool:
        operations_needed = 0
        for count in balls:
            if count > limit:
                operations_needed += (count - 1) // limit
        return operations_needed <= extra_lives

    low = 1
    high = max(balls)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = 1
            continue
            
        if can_achieve_limit(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result