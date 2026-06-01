METADATA = {
    "id": 3454,
    "name": "Separate Squares II",
    "slug": "separate_squares_ii",
    "category": "binary_search",
    "aliases": [],
    "tags": ["binary_search", "geometry"],
    "difficulty": "hard",
    "time_complexity": "O(n log C)",
    "space_complexity": "O(n)",
    "description": "Find the maximum side length of axis‑aligned squares centered at given points such that a straight line can separate all squares without intersecting any of them.",
}

import sys
from typing import List, Tuple

def _can_separate(points: List[Tuple[int, int]], side: int) -> bool:
    """Check if a line can separate squares of given side length.

    The check is performed for vertical and horizontal lines.
    For a vertical line we need a gap between the rightmost edge of the
    left group and the leftmost edge of the right group. The same logic
    applies to a horizontal line.

    Args:
        points: List of (x, y) coordinates.
        side: Candidate side length of the squares.

    Returns:
        True if a separating line exists, False otherwise.
    """
    half = side / 2.0

    # ----- vertical line check -----
    # Sort by x coordinate.
    points_by_x = sorted(points, key=lambda p: p[0])
    # Prefix maximum of right edges.
    prefix_max_right = []
    current_max = -float('inf')
    for x, _ in points_by_x:
        current_max = max(current_max, x + half)
        prefix_max_right.append(current_max)

    # Suffix minimum of left edges.
    suffix_min_left = [0] * len(points_by_x)
    current_min = float('inf')
    for idx in range(len(points_by_x) - 1, -1, -1):
        x, _ = points_by_x[idx]
        current_min = min(current_min, x - half)
        suffix_min_left[idx] = current_min

    # Look for a split where left group's rightmost edge is strictly left of
    # right group's leftmost edge.
    for i in range(len(points_by_x) - 1):
        if prefix_max_right[i] < suffix_min_left[i + 1]:
            return True

    # ----- horizontal line check -----
    points_by_y = sorted(points, key=lambda p: p[1])
    prefix_max_top = []
    current_max = -float('inf')
    for _, y in points_by_y:
        current_max = max(current_max, y + half)
        prefix_max_top.append(current_max)

    suffix_min_bottom = [0] * len(points_by_y)
    current_min = float('inf')
    for idx in range(len(points_by_y) - 1, -1, -1):
        _, y = points_by_y[idx]
        current_min = min(current_min, y - half)
        suffix_min_bottom[idx] = current_min

    for i in range(len(points_by_y) - 1):
        if prefix_max_top[i] < suffix_min_bottom[i + 1]:
            return True

    return False


def solve() -> None:
    """Read input, compute the maximum feasible side length, and print it.

    Input format:
        n
        x1 y1
        x2 y2
        ...
        xn yn

    Output:
        A single integer representing the largest side length for which a
        separating line exists.

    Example:
        Input:
            3
            0 0
            5 0
            10 0
        Output:
            10
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    points: List[Tuple[int, int]] = []
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        points.append((x, y))
        idx += 2

    # Binary search on side length.
    low = 0
    # Upper bound: twice the maximal coordinate span (covers all possibilities).
    max_coord = max(max(abs(x), abs(y)) for x, y in points)
    high = 2 * max_coord + 2  # exclusive upper bound

    while low < high:
        mid = (low + high + 1) // 2
        if _can_separate(points, mid):
            low = mid
        else:
            high = mid - 1

    print(low)