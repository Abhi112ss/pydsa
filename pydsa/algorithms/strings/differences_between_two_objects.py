METADATA = {
    "id": 2700,
    "name": "Differences Between Two Objects",
    "slug": "differences_between_two_objects",
    "category": "design",
    "aliases": [],
    "tags": ["design_patterns", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return a sorted list of strings describing added, removed, or changed keys between two nested dictionaries.",
}


def solve(original: dict, modified: dict) -> list[str]:
    """Identify differences between two nested dictionaries.

    Args:
        original: The original dictionary.
        modified: The dictionary after modifications.

    Returns:
        A lexicographically sorted list of strings, each describing an added,
        removed, or changed key. Keys are represented by a dot‑separated path.

    Examples:
        >>> solve({"a": 1, "b": 2}, {"a": 1, "b": 3, "c": 4})
        ['Added key: c', 'Changed key: b']
        >>> solve({"x": {"y": 5}}, {"x": {"y": 6, "z": 7}})
        ['Added key: x.z', 'Changed key: x.y']
    """
    differences: list[str] = []

    def compare(dict_original: dict, dict_modified: dict, path: list[str]) -> None:
        """Recursively compare two dictionaries and record differences."""
        # Keys present only in the original dictionary → removed
        for key in dict_original:
            if key not in dict_modified:
                full_path = ".".join(path + [key])
                differences.append(f"Removed key: {full_path}")

        # Keys present only in the modified dictionary → added
        for key in dict_modified:
            if key not in dict_original:
                full_path = ".".join(path + [key])
                differences.append(f"Added key: {full_path}")

        # Keys present in both dictionaries → check for changes or recurse
        for key in dict_original:
            if key in dict_modified:
                value_original = dict_original[key]
                value_modified = dict_modified[key]
                full_path = ".".join(path + [key])
                both_dicts = isinstance(value_original, dict) and isinstance(value_modified, dict)
                if both_dicts:
                    # Recurse into nested dictionaries
                    compare(value_original, value_modified, path + [key])
                elif value_original != value_modified:
                    differences.append(f"Changed key: {full_path}")

    compare(original, modified, [])
    differences.sort()
    return differences