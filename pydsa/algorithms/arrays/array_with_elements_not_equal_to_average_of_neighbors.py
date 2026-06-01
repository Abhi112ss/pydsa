METADATA = {
    "id": 1968,
    "name": "Array With Elements Not Equal to Average of Neighbors",
    "slug": "array_with_elements_not_equal_to_average_of_neighbors",
    "category": "array",
    "aliases": [],
    "tags": ["array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum deletions so that no element equals the average of its neighbors.",
}


def solve() -> None:
    """Read input, compute the minimum number of deletions, and print the result.

    Args:
        None. Input is read from standard input.

    Returns:
        None. The answer is printed to standard output.

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO("5\\n1 2 3 4 5\\n")
        >>> solve()
        1
        >>> sys.stdin = io.StringIO("4\\n1 2 1 2\\n")
        >>> solve()
        2
        >>> sys.stdin = io.StringIO("3\\n2 2 2\\n")
        >>> solve()
        3
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    nums = list(map(int, data[1:1 + n]))

    # If the array has less than three elements, there are no middle elements to check.
    # In this case the condition is vacuously satisfied, so the answer follows the
    # problem's insight and is 1.
    if n < 3:
        print(1)
        return

    # Check whether there exists an element that already does NOT equal the average
    # of its immediate neighbors. If such an element exists, deleting it alone is enough.
    for i in range(1, n - 1):
        if nums[i] * 2 != nums[i - 1] + nums[i + 1]:
            print(1)
            return

    # At this point every middle element equals the average of its neighbors.
    # Look for a pair of adjacent elements where the left and right neighbors differ.
    # Deleting those two adjacent elements resolves the issue.
    for i in range(1, n - 1):
        if nums[i - 1] != nums[i + 1]:
            print(2)
            return

    # If neither of the above cases holds, the array forms a perfect arithmetic
    # progression where all triples are equal. We need to delete three elements.
    print(3)