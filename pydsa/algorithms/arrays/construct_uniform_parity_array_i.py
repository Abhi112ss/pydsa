METADATA = {
    "id": 3875,
    "name": "Construct Uniform Parity Array I",
    "slug": "construct-uniform-parity-array-i",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make all elements in an array have the same parity.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make all elements in the array 
    have the same parity (either all even or all odd).

    An operation consists of changing an element's parity. To minimize operations,
    we count how many even numbers and how many odd numbers exist, then choose
    the smaller count to flip.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 3, 4])
        2
        >>> solve([2, 4, 6])
        0
        >>> solve([1, 3, 5])
        0
    """
    even_count = 0
    odd_count = 0

    # Iterate through the array once to count parities
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # The minimum operations is the minimum of the two counts,
    # as we want to flip the minority parity to match the majority.
    return min(even_count, odd_count)
