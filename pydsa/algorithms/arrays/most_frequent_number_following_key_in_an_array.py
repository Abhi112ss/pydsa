METADATA = {
    "id": 2190,
    "name": "Most Frequent Number Following Key In an Array",
    "slug": "most-frequent-number-following-key-in-an-array",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the most frequent number that appears immediately after a specific key in an array.",
}

def solve(nums: list[int], key: int) -> int:
    """
    Finds the most frequent number that follows the given key in the array.

    Args:
        nums: A list of integers.
        key: The integer key to look for.

    Returns:
        The most frequent integer that appears immediately after the key.
        If there is a tie, the smallest integer is returned.

    Examples:
        >>> solve([1, 100, 2, 1, 100, 3, 1, 100], 1)
        100
        >>> solve([1, 100, 2, 1, 100, 3, 1, 100], 100)
        2
    """
    counts: dict[int, int] = {}

    # Iterate through the array up to the second to last element
    # to ensure there is an element following the current index.
    for i in range(len(nums) - 1):
        if nums[i] == key:
            next_val = nums[i + 1]
            counts[next_val] = counts.get(next_val, 0) + 1

    # If no number follows the key, the problem constraints usually 
    # imply this won't happen, but we handle the empty case.
    if not counts:
        return -1

    # Find the number with the maximum frequency.
    # In case of ties, we need the smallest number.
    # We can achieve this by sorting keys or using a custom key in max().
    # A more efficient way is to iterate once through the dictionary.
    max_freq = -1
    result = float('inf')

    for val, freq in counts.items():
        if freq > max_freq:
            max_freq = freq
            result = val
        elif freq == max_freq:
            # If frequencies are equal, pick the smaller value
            if val < result:
                result = val

    return int(result)
