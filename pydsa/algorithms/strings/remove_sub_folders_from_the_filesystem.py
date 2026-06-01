METADATA = {
    "id": 1233,
    "name": "Remove Sub-Folders from the Filesystem",
    "slug": "remove-sub-folders-from-the-filesystem",
    "category": "String",
    "aliases": [],
    "tags": ["string", "sorting", "trie"],
    "difficulty": "medium",
    "time_complexity": "O(N * L * log N)",
    "space_complexity": "O(N * L)",
    "description": "Given a list of folder paths, remove all sub-folders such that no folder in the result is a sub-folder of another.",
}

def solve(folder: list[str]) -> list[str]:
    """
    Removes sub-folders from a list of filesystem paths.

    A folder is considered a sub-folder if it starts with the parent folder 
    path followed by a forward slash '/'.

    Args:
        folder: A list of strings representing the folder paths.

    Returns:
        A list of strings containing only the top-level folders.

    Examples:
        >>> solve(["/a","/a/b","/c/d","/c/d/e","/c/f"])
        ['/a', '/c/d', '/c/f']
        >>> solve(["/a","/a/b/c","/a/b/d"])
        ['/a']
    """
    if not folder:
        return []

    # Sort folders lexicographically. 
    # This ensures that a parent folder always appears immediately before its sub-folders.
    # Example: ["/a", "/a/b", "/a/b/c", "/b"]
    folder.sort()

    result: list[str] = []
    
    # The first folder in the sorted list is guaranteed to be a root/top-level folder.
    result.append(folder[0])

    for i in range(1, len(folder)):
        last_added_folder = result[-1]
        current_folder = folder[i]

        # Check if the current folder is a sub-folder of the last added folder.
        # A sub-folder must start with the parent path AND be followed by a '/'.
        # We append '/' to the parent to avoid false positives like "/a" being a parent of "/ab".
        parent_prefix = last_added_folder + "/"
        
        if not current_folder.startswith(parent_prefix):
            # If it's not a sub-folder, it's a new top-level folder.
            result.append(current_folder)

    return result
