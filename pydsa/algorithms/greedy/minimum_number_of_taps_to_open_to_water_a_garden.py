METADATA = {
    "id": 1326,
    "name": "Minimum Number of Taps to Open to Water a Garden",
    "slug": "minimum-number-of-taps-to-open-to-water-a-garden",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "dynamic_programming", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of taps required to water a garden of length n.",
}

def solve(n: int, ranges: list[int]) -> int:
    """
    Calculates the minimum number of taps needed to cover the interval [0, n].

    The problem is transformed into a Jump Game II variant. We first create a 
    'max_reach' array where each index represents a starting position and 
    the value represents the furthest position reachable from that start.

    Args:
        n: The length of the garden.
        ranges: A list of integers where ranges[i] is the radius of the i-th tap.

    Returns:
        The minimum number of taps required, or -1 if it is impossible to water the garden.

    Examples:
        >>> solve(5, [3, 4, 1, 1, 0, 0])
        1
        >>> solve(3, [0, 0, 0, 0])
        -1
    """
    # max_reach[i] stores the furthest point we can reach starting from or before index i
    max_reach = [0] * (n + 1)

    for i, radius in enumerate(ranges):
        # Calculate the interval covered by the current tap
        left = max(0, i - radius)
        right = min(n, i + radius)
        
        # For the starting point of this interval, update the furthest reachable point
        max_reach[left] = max(max_reach[left], right)

    taps_count = 0
    current_end = 0
    furthest_reachable = 0

    # Iterate through the garden to find the minimum jumps (taps)
    # We don't need to check index n because once current_end reaches n, we are done
    for i in range(n):
        # Update the furthest point we can reach using any tap encountered so far
        furthest_reachable = max(furthest_reachable, max_reach[i])

        # If we reach a point that cannot be covered by any tap
        if i == furthest_reachable:
            return -1

        # If we have reached the end of the current tap's coverage, 
        # we must "open" a new tap that extends our reach the furthest
        if i == current_end:
            taps_count += 1
            current_end = furthest_reachable

    return taps_count
