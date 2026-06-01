METADATA = {
    "id": 2618,
    "name": "Check if Object Instance of Class",
    "slug": "check_if_object_instance_of_class",
    "category": "javascript",
    "aliases": [],
    "tags": ["javascript", "prototype", "object"],
    "difficulty": "easy",
    "time_complexity": "O(depth)",
    "space_complexity": "O(1)",
    "description": "Determine whether a given object is an instance of a specified class by traversing its prototype chain.",
}


def check_if_instance_of(obj: object, target_class: type) -> bool:
    """Iteratively traverse the object's class hierarchy to see if *target_class* appears.

    Args:
        obj: The object whose ancestry is being inspected.
        target_class: The class to match against.

    Returns:
        True if *target_class* is found in the inheritance chain of *obj*, otherwise False.
    """
    current_class = obj.__class__
    # Walk up the inheritance chain (similar to JavaScript prototype traversal)
    while current_class is not None:
        if current_class is target_class:
            return True
        current_class = current_class.__base__  # move to the parent class
    return False


def solve() -> None:
    """Read an object expression and a class expression from stdin and print the result.

    Expected input format (two lines):
        <Python expression that evaluates to an object>
        <Python expression that evaluates to a class>

    The function evaluates the expressions, checks the instance relationship,
    and writes 'true' or 'false' (lower‑case) to stdout.

    Example:
        >>> class A: pass
        >>> a = A()
        >>> input_data = "a\\nA"
        >>> # after feeding input_data to stdin, solve() prints "true"
    """
    import sys

    input_lines = sys.stdin.read().splitlines()
    if len(input_lines) < 2:
        return

    object_expr = input_lines[0].strip()
    class_expr = input_lines[1].strip()

    # Evaluate the expressions in the caller's global namespace.
    # This allows previously defined classes/objects to be referenced.
    obj = eval(object_expr, globals(), {})
    target_class = eval(class_expr, globals(), {})

    result = check_if_instance_of(obj, target_class)
    sys.stdout.write(str(result).lower())