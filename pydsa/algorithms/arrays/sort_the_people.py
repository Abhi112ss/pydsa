METADATA = {
    "id": 2418,
    "name": "Sort the People",
    "slug": "sort-the-people",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort names based on their corresponding wealth in descending order.",
}

def solve(names: list[str], wealth: list[int]) -> list[str]:
    """
    Sorts the names based on the wealth values in descending order.

    Args:
        names: A list of strings representing the names of people.
        wealth: A list of integers representing the wealth of each person.

    Returns:
        A list of names sorted by wealth from highest to lowest.

    Examples:
        >>> solve(["Alice", "Bob"], [15, 6])
        ['Alice', 'Bob']
        >>> solve(["Alice", "Bob", "Charlie"], [15, 6, 10])
        ['Alice', 'Charlie', 'Bob']
    """
    # Combine names and wealth into pairs to maintain the association during sorting
    people_pairs = list(zip(names, wealth))

    # Sort the pairs based on the wealth (the second element of the tuple)
    # We use reverse=True because the problem asks for descending order
    people_pairs.sort(key=lambda pair: pair[1], reverse=True)

    # Extract only the names from the sorted pairs
    sorted_names = [name for name, amount in people_pairs]

    return sorted_names
