METADATA = {
    "id": 1378,
    "name": "Replace Employee ID With The Unique Identifier",
    "slug": "replace_employee_id_with_the_unique_identifier",
    "category": "hash_table",
    "aliases": [],
    "tags": ["hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Replace each employee ID with its unique identifier using a hash map.",
}


def solve(employee_ids: list[int], mappings: list[list[int]]) -> list[int]:
    """Replace each employee ID with its unique identifier.

    Args:
        employee_ids: A list of integer employee IDs.
        mappings: A list of [employee_id, unique_identifier] pairs.

    Returns:
        A new list where each employee ID is replaced by its unique identifier
        if a mapping exists; otherwise the original ID is retained.

    Examples:
        >>> solve([1, 2, 3], [[2, 20], [3, 30]])
        [1, 20, 30]
        >>> solve([5, 6], [[1, 100]])
        [5, 6]
    """
    # Build a hash map from employee ID to unique identifier for O(1) look‑ups.
    id_to_unique: dict[int, int] = {}
    for employee_id, unique_id in mappings:
        id_to_unique[employee_id] = unique_id

    # Replace each ID using the hash map; keep original if no mapping exists.
    result: list[int] = []
    for original_id in employee_ids:
        result.append(id_to_unique.get(original_id, original_id))

    return result