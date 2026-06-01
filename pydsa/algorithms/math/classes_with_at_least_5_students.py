METADATA = {
    "id": 596,
    "name": "Classes With at Least 5 Students",
    "slug": "classes_with_at_least_5_students",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "logic"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return class IDs that have at least five distinct students.",
}


def solve(records: list[list[int]]) -> list[int]:
    """Return the list of class IDs that have at least five distinct students.

    Args:
        records: A list where each element is a two‑element list
                 [class_id, student_id] representing a student's enrollment.

    Returns:
        A sorted list of class IDs that have five or more unique students.

    Examples:
        >>> solve([[1, 101], [1, 102], [1, 103], [1, 104], [1, 105],
        ...        [2, 201], [2, 202], [2, 203]])
        [1]
        >>> solve([[3, 301], [3, 301], [3, 302], [3, 303], [3, 304],
        ...        [3, 305], [4, 401], [4, 402], [4, 403], [4, 404]])
        [3]
    """
    # Map each class ID to a set of its unique student IDs.
    class_to_students: dict[int, set[int]] = {}
    for class_id, student_id in records:
        if class_id not in class_to_students:
            class_to_students[class_id] = set()
        class_to_students[class_id].add(student_id)

    # Collect class IDs with at least five distinct students.
    qualifying_classes: list[int] = [
        class_id for class_id, students in class_to_students.items()
        if len(students) >= 5
    ]

    # Return the result sorted in ascending order.
    qualifying_classes.sort()
    return qualifying_classes