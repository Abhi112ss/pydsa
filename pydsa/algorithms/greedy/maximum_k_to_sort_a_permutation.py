METADATA = {
    "id": 3644,
    "name": "Maximum K to Sort a Permutation",
    "slug": "maximum-k-to-sort-a-permutation",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "permutation", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum integer k such that a permutation can be sorted using at most k swaps where each swap involves elements at indices i and j if |i - j| is a multiple of k.",
}

def solve(permutation: list[int]) -> int:
    """
    Args:
        permutation: A list of integers representing a permutation of 0 to n-1.

    Returns:
        The maximum integer k such that the permutation can be sorted.
    """
    n = len(permutation)
    displaced_indices = []
    for index in range(n):
        if permutation[index] != index:
            displaced_indices.append(index)

    if not displaced_indices:
        return n

    import math

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    common_gcd = 0
    for index in displaced_indices:
        diff = abs(permutation[index] - index)
        if common_gcd == 0:
            common_gcd = diff
        else:
            common_gcd = gcd(common_gcd, diff)

    return common_gcd