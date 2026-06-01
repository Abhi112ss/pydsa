METADATA = {
    "id": 3128,
    "name": "Right Triangles",
    "slug": "right_triangles",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_map", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Count the number of right-angled triangles that can be formed using three elements from the given array.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of right-angled triangles that can be formed using 
    three elements from the input list.

    A right triangle satisfies the Pythagorean theorem: a^2 + b^2 = c^2.

    Args:
        nums: A list of positive integers representing side lengths.

    Returns:
        The total count of unique triplets (i, j, k) such that 
        nums[i]^2 + nums[j]^2 = nums[k]^2.

    Examples:
        >>> solve([3, 1, 4, 6, 5])
        1
        >>> solve([1, 1, 1])
        0
    """
    # Pre-calculate squares to avoid repeated multiplication and 
    # use a frequency map for O(1) lookup.
    squares_counts: dict[int, int] = {}
    for num in nums:
        square = num * num
        squares_counts[square] = squares_counts.get(square, 0) + 1

    total_triangles = 0
    n = len(nums)

    # Iterate through all unique pairs (i, j) to treat them as legs 'a' and 'b'.
    # We use indices to ensure we don't pick the same element twice for the legs.
    for i in range(n):
        for j in range(i + 1, n):
            a_squared = nums[i] * nums[i]
            b_squared = nums[j] * nums[j]
            c_squared_needed = a_squared + b_squared

            # Check if the required hypotenuse squared exists in our frequency map.
            if c_squared_needed in squares_counts:
                # The number of ways to pick the third side is the count of that square.
                # However, we must ensure we aren't using the same index if 
                # a^2 + b^2 = a^2 (which is impossible for positive integers) 
                # or if the hypotenuse is one of the legs (also impossible).
                # Since nums[i], nums[j] > 0, c_squared_needed will always be > a_squared and > b_squared.
                # Thus, the index of the hypotenuse cannot be i or j.
                total_triangles += squares_counts[c_squared_needed]

    return total_triangles
