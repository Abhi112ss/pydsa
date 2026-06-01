METADATA = {
    "id": 2455,
    "name": "Average Value of Even Numbers That Are Divisible by Three",
    "slug": "average_value_of_even_numbers_that_are_divisible_by_three",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math", "easy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Compute the integer average of numbers that are both even and divisible by three.",
}


def solve() -> None:
    """Read a list of integers from standard input and print the average of numbers
    that are even and divisible by three.

    The input should contain integers separated by whitespace (spaces, newlines, etc.).
    If no such numbers exist, the output is 0.

    Returns:
        None. The result is printed to standard output.

    Example:
        Input:
            1 2 3 4 6 12
        Output:
            9
        Explanation:
            The numbers satisfying the condition are 6 and 12.
            Their sum is 18 and count is 2, so the average is 18 // 2 = 9.
    """
    import sys

    # Parse all integers from stdin; an empty input yields an empty list.
    numbers: list[int] = list(map(int, sys.stdin.read().strip().split()))

    total_sum: int = 0
    qualifying_count: int = 0

    for number in numbers:
        # Check both evenness and divisibility by three.
        if number % 2 == 0 and number % 3 == 0:
            total_sum += number
            qualifying_count += 1

    if qualifying_count == 0:
        average: int = 0
    else:
        # Integer division as defined by the problem.
        average = total_sum // qualifying_count

    print(average)