METADATA = {
    "id": 71,
    "name": "Simplify Path",
    "slug": "simplify-path",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an absolute Unix-style path, simplify it to the canonical path.",
}

def solve(path: str) -> str:
    """
    Simplifies a Unix-style absolute path to its canonical form.

    The canonical path must:
    1. Start with a single slash '/'.
    2. Not end with a slash unless it is the root '/'.
    3. Not contain double slashes '//'.
    4. Not contain '.' (current directory) or '..' (parent directory) components
       unless they are part of a valid directory name.

    Args:
        path: The input Unix-style absolute path string.

    Returns:
        The simplified canonical path string.

    Examples:
        >>> solve("/home/")
        '/home'
        >>> solve("/../")
        '/'
        >>> solve("/home//foo/")
        '/home/foo'
        >>> solve("/a/./b/../../c/")
        '/c'
    """
    # Split the path by '/' to isolate directory names and special symbols
    # Empty strings (from '//') and '.' (current directory) are ignored
    components = path.split("/")
    stack: list[str] = []

    for component in components:
        if component == "..":
            # If '..', move up one directory by popping from the stack if not empty
            if stack:
                stack.pop()
        elif component == "." or not component:
            # Skip current directory indicators or empty strings from consecutive slashes
            continue
        else:
            # Valid directory name, push it onto the stack
            stack.append(component)

    # Join the components with '/' and ensure it starts with a leading slash
    return "/" + "/".join(stack)
