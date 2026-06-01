METADATA = {
    "id": 3012,
    "name": "Minimize Length of Array Using Operations",
    "slug": "minimize-length-of-array-using-operations",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Minimize the length of an array by repeatedly removing two identical elements.",
}

def solve(nums: list[int]) -> int:
    """
    Minimizes the length of the array by removing pairs of identical elements.

    The core logic is that for any element appearing 'k' times, we can 
    remove pairs until either 0 or 1 element remains. If 'k' is even, 
    0 remain; if 'k' is odd, 1 remains.

    Args:
        nums: A list of integers representing the initial array.

    Returns:
        The minimum possible length of the array after all possible operations.

    Examples:
        >>> solve([1, 2, 3, 1, 2, 3])
        0
        >>> solve([1, 1, 1, 2, 2, 3])
        2
        >>> solve([1, 2, 3])
        3
    """
    # Count the frequency of each number in the array
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    remaining_elements = 0
    
    # For each unique number, check if an odd number of occurrences remains
    # after removing all possible pairs.
    for frequency in counts.values():
        # If frequency is odd, one instance of this number must remain.
        # If frequency is even, all instances can be paired and removed.
        remaining_elements += (frequency % 2)

    return remaining_elements
