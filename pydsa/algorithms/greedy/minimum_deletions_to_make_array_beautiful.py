METADATA = {
    "id": 2216,
    "name": "Minimum Deletions to Make Array Beautiful",
    "slug": "minimum-deletions-to-make-array-beautiful",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of deletions required to make an array beautiful, where an array is beautiful if it has an even length and every even index contains an even number.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of deletions to make the array beautiful.
    
    An array is beautiful if:
    1. It has an even length.
    2. Every even index (0, 2, 4...) contains an even number.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of deletions required.

    Examples:
        >>> solve([2, 3, 4, 5, 6])
        1
        >>> solve([2, 1, 2, 1, 2, 1])
        0
        >>> solve([1, 2, 3, 4])
        2
    """
    deletions = 0
    # current_even_index tracks the index we are currently trying to fill 
    # in the "new" beautiful array.
    current_even_index = 0

    for num in nums:
        # A beautiful array requires even numbers at even indices (0, 2, 4...).
        # If the current index we are targeting is even, we must ensure the number is even.
        if current_even_index % 2 == 0:
            if num % 2 == 0:
                # Valid number for an even index, move to the next index.
                current_even_index += 1
            else:
                # Invalid number for an even index, must delete it.
                deletions += 1
        else:
            # If the current index is odd, any number is acceptable.
            # We just move to the next index.
            current_even_index += 1

    # After iterating, if the length of our constructed beautiful array is odd,
    # we must delete one more element to satisfy the even length requirement.
    if current_even_index % 2 != 0:
        deletions += 1

    return deletions
