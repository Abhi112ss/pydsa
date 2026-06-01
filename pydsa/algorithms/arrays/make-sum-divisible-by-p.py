METADATA = {
    "id": 1590,
    "name": "Make Sum Divisible by P",
    "slug": "make_sum_divisible_by_p",
    "category": "array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the smallest subarray to remove so that the remaining sum is divisible by p.",
}


def solve(nums: list[int], p: int) -> int:
    """Find the length of the smallest subarray to remove so that the remaining sum is divisible by p.

    Args:
        nums: List of positive integers.
        p: Positive integer divisor.

    Returns:
        The length of the shortest subarray that can be removed to make the sum of the remaining
        elements divisible by p. Returns -1 if no such subarray exists (i.e., the whole array would
        need to be removed).

    Examples:
        >>> solve([3,1,4,2], 6)
        1
        >>> solve([6,3,5,2], 9)
        2
        >>> solve([1,2,3], 3)
        0
    """
    total_mod = sum(nums) % p
    # If total sum already divisible by p, no removal needed.
    if total_mod == 0:
        return 0

    # Map from prefix modulo value to earliest index where it occurs.
    prefix_index: dict[int, int] = {0: -1}
    current_mod = 0
    min_length = len(nums) + 1  # Initialize with impossible large value.

    for index, value in enumerate(nums):
        current_mod = (current_mod + value) % p
        # Desired previous modulo to achieve required removal remainder.
        target_mod = (current_mod - total_mod) % p
        if target_mod in prefix_index:
            candidate_length = index - prefix_index[target_mod]
            if candidate_length < min_length:
                min_length = candidate_length
        # Store earliest occurrence of current_mod.
        if current_mod not in prefix_index:
            prefix_index[current_mod] = index

    # If min_length equals impossible value or equals array length, removal not possible.
    if min_length > len(nums) - 1:
        return -1
    return min_length