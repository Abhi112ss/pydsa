METADATA = {
    "id": 1646,
    "name": "Get Maximum in Generated Array",
    "slug": "get_maximum_in_generated_array",
    "category": "algorithms",
    "aliases": [],
    "tags": ["arrays", "dynamic_programming"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Generate an array using a specific recurrence and return the maximum value up to index n.",
}


def solve() -> None:
    """Read an integer n, generate the array as defined by the problem, and print the maximum value.

    Args:
        None (input is read from standard input).

    Returns:
        None (the result is printed to standard output).

    Example:
        Input: 7
        Output: 3

        Input: 2
        Output: 1
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])

    # Edge cases where the array size is trivial.
    if n == 0:
        print(0)
        return
    if n == 1:
        print(1)
        return

    # Initialize the generated array with zeros; nums[0] = 0, nums[1] = 1.
    nums: list[int] = [0] * (n + 1)
    nums[1] = 1
    max_value = 1  # Track the maximum encountered value.

    # Build the array iteratively using the given recurrence.
    for i in range(1, n // 2 + 1):
        even_index = 2 * i
        nums[even_index] = nums[i]  # nums[2*i] = nums[i]
        if nums[even_index] > max_value:
            max_value = nums[even_index]

        odd_index = even_index + 1
        if odd_index <= n:
            nums[odd_index] = nums[i] + nums[i + 1]  # nums[2*i+1] = nums[i] + nums[i+1]
            if nums[odd_index] > max_value:
                max_value = nums[odd_index]

    print(max_value)