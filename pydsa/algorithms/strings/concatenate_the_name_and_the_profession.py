METADATA = {
    "id": 2504,
    "name": "Concatenate the Name and the Profession",
    "slug": "concatenate_the_name_and_the_profession",
    "category": "Array",
    "aliases": [],
    "tags": ["string_manipulation", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Combine each name with its profession into a formatted string.",
}


def solve(name: list[str], profession: list[str]) -> list[str]:
    """Concatenate each name with its corresponding profession.

    Args:
        name: List of names.
        profession: List of professions, same length as ``name``.

    Returns:
        List where each element is formatted as "<name> is a <profession>".

    Examples:
        >>> solve(["Mickey", "Tom"], ["Mouse", "Cat"])
        ['Mickey is a Mouse', 'Tom is a Cat']
        >>> solve(["John"], ["Engineer"])
        ['John is a Engineer']
    """
    # Store the first occurrence of each name (hash map) – O(n) space.
    first_occurrence: dict[str, str] = {}
    result: list[str] = []

    for current_name, current_profession in zip(name, profession):
        # Record the first time we see a name.
        if current_name not in first_occurrence:
            first_occurrence[current_name] = current_profession
        # Build the concatenated string.
        result.append(f"{current_name} is a {current_profession}")

    return result