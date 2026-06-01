METADATA = {
    "id": 3275,
    "name": "K-th Nearest Obstacle Queries",
    "slug": "kth-nearest-obstacle-queries",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "sorting", "array"],
    "difficulty": "medium",
    "time_complexity": "O(q log n)",
    "space_complexity": "O(n)",
    "description": "Find the k-th nearest obstacle to a given position using binary search on a sorted list of obstacle positions.",
}

import bisect

def solve(obstacles: list[int], queries: list[list[int]]) -> list[int]:
    """
    Finds the k-th nearest obstacle for each query.

    Args:
        obstacles: A list of integers representing the positions of obstacles.
        queries: A list of queries where each query is [position, k].

    Returns:
        A list of integers representing the k-th nearest obstacle position for each query.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [[3, 1], [3, 2]])
        [3, 2]
        >>> solve([1, 5, 10], [[6, 1], [6, 2]])
        [5, 10]
    """
    # The input obstacles are not guaranteed to be sorted, but the problem 
    # implies we need to find distances, so sorting is the first step.
    # Note: In some LeetCode versions, obstacles are already sorted.
    # We sort to enable binary search.
    sorted_obstacles = sorted(obstacles)
    n = len(sorted_obstacles)
    results = []

    for pos, k in queries:
        # Find the insertion point to locate the closest obstacle to 'pos'
        # idx is the index of the first obstacle >= pos
        idx = bisect.bisect_left(sorted_obstacles, pos)
        
        # We use two pointers to expand outwards from the insertion point.
        # left points to the closest obstacle <= pos
        # right points to the closest obstacle >= pos
        left = idx - 1
        right = idx
        
        last_obstacle = -1
        
        # We need to find the k-th nearest. We iterate k times.
        # In each step, we pick the closer obstacle between left and right.
        # If distances are equal, the smaller position (left) is preferred.
        for _ in range(k):
            if left >= 0 and right < n:
                dist_left = abs(sorted_obstacles[left] - pos)
                dist_right = abs(sorted_obstacles[right] - pos)
                
                # Compare distances; if equal, left is chosen due to problem constraints
                if dist_left <= dist_right:
                    last_obstacle = sorted_obstacles[left]
                    left -= 1
                else:
                    last_obstacle = sorted_obstacles[right]
                    right += 1
            elif left >= 0:
                # Only left side has obstacles remaining
                last_obstacle = sorted_obstacles[left]
                left -= 1
            elif right < n:
                # Only right side has obstacles remaining
                last_obstacle = sorted_obstacles[right]
                right += 1
            else:
                # This case should not be reached if k is valid
                break
        
        results.append(last_obstacle)
        
    return results
