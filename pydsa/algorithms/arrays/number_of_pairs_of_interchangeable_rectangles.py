METADATA = {
    "id": 2001,
    "name": "Number of Pairs of Interchangeable Rectangles",
    "slug": "number_of_pairs_of_interchangeable_rectangles",
    "category": "hash_table",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count pairs of rectangles that share the same width-to-height ratio.",
}


def solve(rectangles: list[list[int]]) -> int:
    """Count the number of interchangeable rectangle pairs.

    Two rectangles are interchangeable if `width_i * height_j == width_j * height_i`,
    i.e., they have the same reduced width‑to‑height ratio.

    Args:
        rectangles: A list where each element is a two‑element list
            `[width, height]` describing a rectangle.

    Returns:
        The total number of pairs `(i, j)` with `i < j` that are interchangeable.

    Examples:
        >>> solve([[1, 2], [2, 4], [3, 6]])
        3
        >>> solve([[4, 8], [2, 4], [1, 2], [10, 5], [2, 10]])
        3
    """
    from collections import defaultdict
    from math import gcd

    # Map each reduced ratio to its frequency.
    ratio_counts: dict[tuple[int, int], int] = defaultdict(int)

    for width, height in rectangles:
        common_divisor = gcd(width, height)
        reduced_width = width // common_divisor
        reduced_height = height // common_divisor
        ratio_key = (reduced_width, reduced_height)
        ratio_counts[ratio_key] += 1

    total_pairs = 0
    for count in ratio_counts.values():
        # For each group of size `count`, add the number of distinct pairs.
        total_pairs += count * (count - 1) // 2

    return total_pairs