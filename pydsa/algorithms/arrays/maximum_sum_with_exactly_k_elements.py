METADATA = {
    "id": 2656,
    "name": "Maximum Sum With Exactly K Elements",
    "slug": "maximum_sum_with_exactly_k_elements",
    "category": "array",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Return the maximum sum obtainable by selecting exactly k elements from the array.",
}


def solve() -> None:
    """Read input, compute the maximum sum of exactly k elements, and print the result.

    Args:
        None (input is read from standard input).

    Returns:
        None (the answer is printed to standard output).

    Input Format:
        The first line contains an integer n, the length of the array.
        The second line contains n space‑separated integers representing the array.
        The third line contains an integer k.

    Example:
        Input:
            5
            1 5 3 2 4
            3
        Output:
            12
        Explanation:
            The three largest elements are 5, 4, and 3; their sum is 12.
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    # Parse input: n, array elements, k
    n = int(data[0])
    nums = list(map(int, data[1 : 1 + n]))
    k = int(data[1 + n])

    # Sort the array in descending order to bring the largest elements to the front
    nums.sort(reverse=True)

    # Sum the first k elements, which are the k largest values
    max_sum = sum(nums[:k])

    print(max_sum)