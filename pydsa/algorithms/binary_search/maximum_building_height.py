METADATA = {
    "id": 1840,
    "name": "Maximum Building Height",
    "slug": "maximum-building-height",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max_height))",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible height of the shortest building after performing allowed operations to level the heights.",
}

def solve(heights: list[int]) -> int:
    """
    Args:
        heights: A list of integers representing the initial heights of buildings.

    Returns:
        The maximum possible height of the shortest building.
    """
    def can_achieve_height(target_height: int) -> bool:
        current_max_allowed_height = float('inf')
        for i in range(len(heights)):
            if i % 2 == 1:
                current_max_allowed_height = min(current_max_allowed_height, heights[i])
            else:
                if heights[i] < target_height:
                    return False
                current_max_allowed_height = min(current_max_allowed_height, heights[i] - target_height)
            
            if current_max_allowed_height < target_height:
                return False
        return True

    low = 1
    high = max(heights)
    result = 1

    while low <= high:
        mid = (low + high) // 2
        
        possible = True
        limit = float('inf')
        for i in range(len(heights)):
            if i % 2 == 1:
                limit = min(limit, heights[i])
            else:
                if heights[i] < mid:
                    possible = False
                    break
                limit = min(limit, heights[i] - mid)
            
            if limit < mid:
                possible = False
                break
        
        if possible:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return result