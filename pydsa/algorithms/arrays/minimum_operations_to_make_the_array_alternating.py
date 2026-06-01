METADATA = {
    "id": 2170,
    "name": "Minimum Operations to Make the Array Alternating",
    "slug": "minimum-operations-to-make-the-array-alternating",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "greedy", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to make an array alternating by changing elements at even and odd indices.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum operations to make the array alternating.
    
    An array is alternating if nums[i] != nums[i+1] for all valid i.
    To minimize operations, we want to keep the most frequent elements 
    at even and odd positions, provided they are not the same value.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of elements to change.

    Examples:
        >>> solve([4, 1, 1, 2])
        1
        >>> solve([14, 14, 14, 14])
        2
        >>> solve([1, 2, 2, 2, 2])
        2
    """
    n = len(nums)
    if n <= 1:
        return 0

    # Count frequencies for even and odd indices separately
    even_counts: dict[int, int] = {}
    odd_counts: dict[int, int] = {}

    for i in range(n):
        val = nums[i]
        if i % 2 == 0:
            even_counts[val] = even_counts.get(val, 0) + 1
        else:
            odd_counts[val] = odd_counts.get(val, 0) + 1

    def get_top_two(counts: dict[int, int]) -> list[tuple[int, int]]:
        """Returns the two most frequent elements as (value, frequency) tuples."""
        # We need the top two to handle the case where the most frequent 
        # element in even indices is the same as the most frequent in odd indices.
        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        # Pad with dummy values (value -1, freq 0) to ensure we always have at least two
        top_two = sorted_items[:2]
        while len(top_two) < 2:
            top_two.append((-1, 0))
        return top_two

    even_top = get_top_two(even_counts)
    odd_top = get_top_two(odd_counts)

    # Case 1: The most frequent even element is different from the most frequent odd element.
    # We keep both and the operations needed is total length minus their combined counts.
    if even_top[0][0] != odd_top[0][0]:
        max_kept = even_top[0][1] + odd_top[0][1]
    else:
        # Case 2: The most frequent elements are the same.
        # We have two choices:
        # 1. Keep the most frequent even and the second most frequent odd.
        # 2. Keep the second most frequent even and the most frequent odd.
        option_1 = even_top[0][1] + odd_top[1][1]
        option_2 = even_top[1][1] + odd_top[0][1]
        max_kept = max(option_1, option_2)

    return n - max_kept
