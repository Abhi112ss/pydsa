METADATA = {
    "id": 2633,
    "name": "Convert Object to JSON String",
    "slug": "convert_object_to_json_string",
    "category": "String",
    "aliases": [],
    "tags": ["recursion", "strings", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Implement a function that converts a Python-like object into its JSON string representation following specific formatting rules.",
}

def solve(obj: any) -> str:
    """
    Converts a Python object into a JSON-formatted string.

    Args:
        obj: The object to convert. Can be a string, number, boolean, None, 
             list, or dictionary.

    Returns:
        str: The JSON string representation of the object.

    Examples:
        >>> solve({"a": 1, "b": [True, None]})
        '{"a": 1, "b": [true, null]}'
        >>> solve("hello")
        '"hello"'
    """
    # Handle null/None case
    if obj is None:
        return "null"

    # Handle boolean case (must be lowercase in JSON)
    if isinstance(obj, bool):
        return "true" if obj else "false"

    # Handle string case (must be wrapped in double quotes)
    if isinstance(obj, str):
        return f'"{obj}"'

    # Handle numeric case (int or float)
    if isinstance(obj, (int, float)):
        return str(obj)

    # Handle list case (recursive traversal)
    if isinstance(obj, list):
        elements = []
        for item in obj:
            elements.append(solve(item))
        return "[" + ", ".join(elements) + "]"

    # Handle dictionary case (recursive traversal of keys and values)
    if isinstance(obj, dict):
        pairs = []
        # Sort keys if the problem implies deterministic output, 
        # though standard JSON doesn't strictly require it.
        # For LeetCode simulation, we iterate through items.
        for key, value in obj.items():
            # Keys in JSON are always strings
            key_str = f'"{key}"'
            val_str = solve(value)
            pairs.append(f"{key_str}: {val_str}")
        return "{" + ", ".join(pairs) + "}"

    return ""
