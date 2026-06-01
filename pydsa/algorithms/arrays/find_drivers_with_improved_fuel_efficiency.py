METADATA = {
    "id": 3601,
    "name": "Find Drivers with Improved Fuel Efficiency",
    "slug": "find_drivers_with_improved_fuel_efficiency",
    "category": "array",
    "aliases": [],
    "tags": ["array", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the indices of drivers whose fuel efficiency exceeds the average efficiency of all previous drivers.",
}


def solve() -> None:
    """Read driver fuel efficiencies and output indices of drivers with improved efficiency.

    The input consists of:
    - An integer `n` representing the number of drivers.
    - A line with `n` space‑separated integers `efficiencies`, where `efficiencies[i]`
      is the fuel efficiency of the i‑th driver.

    A driver is considered to have *improved* fuel efficiency if its efficiency is
    strictly greater than the average efficiency of all drivers that appeared
    before it.

    The function prints a single line containing the 0‑based indices of all such
    drivers, separated by spaces. If no driver satisfies the condition, an empty
    line is printed.

    Returns:
        None

    Examples:
        >>> # Example 1
        >>> # Input:
        >>> # 5
        >>> # 10 12 9 15 20
        >>> # Drivers 1 (12) and 3 (15) have efficiencies greater than the
        >>> # average of all previous drivers.
        >>> # Output:
        >>> # 1 3
        >>> # (When run via the command line, the function reads from stdin and
        >>> # writes to stdout.)
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    efficiencies = list(map(int, data[1:1 + n]))

    prefix_sum = 0
    improved_indices: list[int] = []

    for index, efficiency in enumerate(efficiencies):
        if index > 0:
            average_before = prefix_sum / index
            if efficiency > average_before:
                improved_indices.append(index)  # store 0‑based index
        prefix_sum += efficiency  # update running sum for next iteration

    # Output result
    print(" ".join(map(str, improved_indices)))