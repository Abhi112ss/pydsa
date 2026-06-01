METADATA = {
    "id": 2670,
    "name": "Find the Distinct Difference Array",
    "slug": "find_the_distinct_difference_array",
    "category": "array",
    "aliases": [],
    "tags": ["array", "set"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return an array where each element is the difference between distinct counts in the prefix and suffix of the input array.",
}


def solve() -> None:
    """Read an integer array from standard input and print its distinct difference array.

    Args:
        None (input is read from stdin):
            The first line contains an integer n, the length of the array.
            The second line contains n space‑separated integers.

    Returns:
        None (the result is printed to stdout):
            A single line with n space‑separated integers representing the distinct
            difference array.

    Examples:
        >>> # Input:
        >>> # 5
        >>> # 1 2 3 4 5
        >>> # Output:
        >>> # -4 -2 0 2 4
        >>> # Explanation:
        >>> # Prefix distinct counts: [1,2,3,4,5]
        >>> # Suffix distinct counts: [5,4,3,2,1]
        >>> # Differences: [1-5, 2-4, 3-3, 4-2, 5-1] = [-4,-2,0,2,4]
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    length = int(data[0])
    numbers = list(map(int, data[1:1 + length]))

    # Compute distinct counts for each prefix.
    prefix_distinct_counts: list[int] = []
    seen_prefix: set[int] = set()
    for index in range(length):
        element = numbers[index]
        seen_prefix.add(element)  # add maintains uniqueness
        prefix_distinct_counts.append(len(seen_prefix))

    # Compute distinct counts for each suffix (starting after each index).
    suffix_distinct_counts: list[int] = [0] * length
    seen_suffix: set[int] = set()
    for index in range(length - 1, -1, -1):
        element = numbers[index]
        seen_suffix.add(element)
        suffix_distinct_counts[index] = len(seen_suffix)

    # The suffix count for position i should exclude the element at i,
    # so shift the suffix array by one position.
    # For the last position, the suffix after it is empty (count 0).
    shifted_suffix_counts: list[int] = [0] * length
    for index in range(length - 1):
        shifted_suffix_counts[index] = suffix_distinct_counts[index + 1]
    shifted_suffix_counts[length - 1] = 0

    # Compute the distinct difference array.
    distinct_difference: list[int] = [
        prefix_distinct_counts[index] - shifted_suffix_counts[index]
        for index in range(length)
    ]

    print(" ".join(map(str, distinct_difference)))
