METADATA = {
    "id": 1691,
    "name": "Maximum Height by Stacking Cuboids",
    "slug": "maximum_height_by_stacking_cuboids",
    "category": "dynamic_programming",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum possible height by stacking cuboids after rotating each to optimal orientation.",
}


def solve() -> None:
    """Compute the maximum stack height of cuboids.

    The input is read from standard input.
    The first line contains an integer *n*, the number of cuboids.
    Each of the next *n* lines contains three integers representing the
    dimensions of a cuboid.

    The function prints a single integer: the greatest total height achievable
    by stacking a subset of the cuboids, where each cuboid may be rotated
    arbitrarily before stacking.

    Example:
        Input:
            3
            50 45 20
            95 37 23
            45 23 55
        Output:
            190
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    iterator = iter(data)
    n = int(next(iterator))
    cuboids: list[list[int]] = []
    for _ in range(n):
        dimensions = [int(next(iterator)), int(next(iterator)), int(next(iterator))]
        # Rotate each cuboid so that its dimensions are in non‑decreasing order
        dimensions.sort()
        cuboids.append(dimensions)

    # Sort cuboids lexicographically to enable a DP over increasing sequences
    cuboids.sort()

    dp: list[int] = [0] * n
    max_height = 0
    for i in range(n):
        # Height contributed by the current cuboid when placed alone
        dp[i] = cuboids[i][2]
        for j in range(i):
            # Check if cuboid j can be placed below cuboid i
            if (cuboids[j][0] <= cuboids[i][0] and
                cuboids[j][1] <= cuboids[i][1] and
                cuboids[j][2] <= cuboids[i][2]):
                # Update dp[i] with the best height achievable ending with cuboid i
                if dp[j] + cuboids[i][2] > dp[i]:
                    dp[i] = dp[j] + cuboids[i][2]
        if dp[i] > max_height:
            max_height = dp[i]

    print(max_height)