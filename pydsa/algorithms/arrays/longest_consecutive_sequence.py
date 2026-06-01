METADATA = {
    "id": 128,
    "name": "Longest Consecutive Sequence",
    "slug": "longest-consecutive-sequence",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_set", "union_find", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest consecutive elements sequence in an unsorted array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence in an unsorted array.

    The algorithm uses a hash set to achieve O(n) time complexity. It identifies 
    the start of a sequence by checking if (num - 1) exists in the set. If it 
    doesn't, it counts how many consecutive numbers follow.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest consecutive sequence.

    Examples:
        >>> solve([100, 4, 200, 1, 3, 2])
        4
        >>> solve([0, 3, 7, 2, 5, 8, 4, 6, 1])
        9
    """
    if not nums:
        return 0

    # Convert list to a set for O(1) average time complexity lookups
    num_set = set(nums)
    longest_streak = 0

    for number in num_set:
        # Check if 'number' is the start of a sequence.
        # If 'number - 1' is in the set, 'number' is part of a sequence but not the start.
        if (number - 1) not in num_set:
            current_number = number
            current_streak = 1

            # Incrementally check for the next numbers in the sequence
            while (current_number + 1) in num_set:
                current_number += 1
                current_streak += 1

            # Update the global maximum streak found so far
            if current_streak > longest_streak:
                longest_streak = current_streak

    return longest_streak
