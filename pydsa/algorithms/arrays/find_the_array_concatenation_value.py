METADATA = {
    "id": 2562,
    "name": "Find the Array Concatenation Value",
    "slug": "find_the_array_concatenation_value",
    "category": "array",
    "aliases": [],
    "tags": ["arrays", "prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum obtained by repeatedly concatenating the first and last elements of the array.",
}


def _digit_count(number: int) -> int:
    """Return the count of decimal digits of a non‑negative integer."""
    if number == 0:
        return 1
    count = 0
    while number:
        count += 1
        number //= 10
    return count


def solve() -> None:
    """Read input, compute the array concatenation value, and print the result.

    The input format is:
        n
        a1 a2 ... an

    Args:
        None (reads from standard input).

    Returns:
        None (writes the answer to standard output).

    Example:
        Input:
            5
            12 34 56 78 90
        Output:
            1234 + 5678 + 90 = 7032
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    nums = list(map(int, data[1:1 + n]))

    left_index = 0
    right_index = n - 1
    total_value = 0

    while left_index < right_index:
        left_number = nums[left_index]
        right_number = nums[right_index]
        # Concatenate left_number and right_number as digits.
        concatenated = left_number * (10 ** _digit_count(right_number)) + right_number
        total_value += concatenated
        left_index += 1
        right_index -= 1

    if left_index == right_index:
        total_value += nums[left_index]

    sys.stdout.write(str(total_value))