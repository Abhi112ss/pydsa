METADATA = {
    "id": 2171,
    "name": "Removing Minimum Number of Magic Beans",
    "slug": "removing-minimum-number-of-magic-beans",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "array", "sorting", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of magic beans to remove so that all remaining beans have the same magic power.",
}

def solve(magic_beans: list[int]) -> int:
    """
    Calculates the minimum number of magic beans to remove to ensure all 
    remaining beans have the same magic power.

    The strategy is to find the magic power that appears most frequently 
    and keep all beans of that power, removing all others.

    Args:
        magic_beans: A list of integers representing the magic power of each bean.

    Returns:
        The minimum number of beans to remove.

    Examples:
        >>> solve([7, 1, 3, 3, 3, 5, 7])
        4
        >>> solve([1, 1, 1, 1])
        0
        >>> solve([1, 2, 3, 4, 5])
        4
    """
    if not magic_beans:
        return 0

    # Count the frequency of each magic power value
    counts: dict[int, int] = {}
    for power in magic_beans:
        counts[power] = counts.get(power, 0) + 1

    # Find the maximum frequency among all magic powers
    # The beans we keep will be those with this maximum frequency
    max_frequency = 0
    for frequency in counts.values():
        if frequency > max_frequency:
            max_frequency = frequency

    # The minimum beans to remove is the total count minus the count of the most frequent bean
    return len(magic_beans) - max_frequency
