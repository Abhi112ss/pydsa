METADATA = {
    "id": 985,
    "name": "Sum of Even Numbers After Queries",
    "slug": "sum-of-even-numbers-after-queries",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of even numbers in an array after performing a series of update queries.",
}

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    Calculates the sum of even numbers in the array after each query.

    Args:
        nums: A list of integers representing the initial array.
        queries: A list of queries where each query is [index, val].

    Returns:
        A list of integers representing the sum of even numbers after each query.

    Examples:
        >>> solve([4, 1, 2, 7, 8], [[1, 10], [2, 13], [3, 1], [0, 1]], [[1, 10], [2, 13], [3, 1], [0, 1]])
        [22, 14, 14, 14]
    """
    # Calculate the initial sum of all even numbers in the array
    current_even_sum = sum(x for x in nums if x % 2 == 0)
    results = []

    for index, new_val in queries:
        old_val = nums[index]

        # If the old value was even, subtract it from the running sum
        if old_val % 2 == 0:
            current_even_sum -= old_val

        # Update the array with the new value
        nums[index] = new_val

        # If the new value is even, add it to the running sum
        if new_val % 2 == 0:
            current_even_sum += new_val

        results.append(current_even_sum)

    return results
