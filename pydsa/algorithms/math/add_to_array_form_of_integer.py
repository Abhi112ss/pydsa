METADATA = {
    "id": 989,
    "name": "Add to Array-Form of Integer",
    "slug": "add_to_array_form_of_integer",
    "category": "array",
    "aliases": [],
    "tags": ["array", "math"],
    "difficulty": "easy",
    "time_complexity": "O(max(n, log k))",
    "space_complexity": "O(max(n, log k))",
    "description": "Add an integer k to the integer represented by an array of its digits.",
}


def solve() -> None:
    """Read an array-form integer and an integer k, add them, and output the result.

    Args:
        None (input is read from stdin):
            - First line: space‑separated digits of the array-form integer (e.g., "1 2 0").
            - Second line: integer k (e.g., "34").

    Returns:
        None (the result is printed to stdout as space‑separated digits).

    Example:
        Input:
            1 2 0
            34
        Output:
            1 5 4
    """
    import sys

    data = sys.stdin.read().strip().splitlines()
    if len(data) < 2:
        return

    # Parse the array-form integer.
    num = [int(token) for token in data[0].strip().split()] if data[0].strip() else []
    # Parse k.
    k = int(data[1].strip())

    index = len(num) - 1
    result_digits: list[int] = []

    # Process digits from least significant to most significant.
    while index >= 0 or k > 0:
        if index >= 0:
            k += num[index]  # add current digit to k (acts as carry)
        result_digits.append(k % 10)  # store current result digit
        k //= 10  # update carry
        index -= 1

    # The digits were collected in reverse order; reverse them to obtain the final array.
    result_digits.reverse()
    print(" ".join(map(str, result_digits)))
