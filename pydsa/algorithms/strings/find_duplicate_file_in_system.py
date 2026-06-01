METADATA = {
    "id": 609,
    "name": "Find Duplicate File in System",
    "slug": "find-duplicate-file-in-system",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string_parsing"],
    "difficulty": "medium",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n * k)",
    "description": "Find all groups of duplicate files in a system given their paths and contents.",
}

def solve(files: list[str]) -> list[list[str]]:
    """
    Finds all groups of duplicate files based on their content.

    Args:
        files: A list of strings where each string represents a file path 
               and its content in the format "root/path/filename.ext content".

    Returns:
        A list of lists, where each inner list contains the paths of files 
        that have the same content. Only lists with more than one file are returned.

    Examples:
        >>> solve(["root/a 1", "root/c 1", "root/b 1"])
        [['root/a', 'root/c', 'root/b']]
        >>> solve(["root/a 1", "root/c 2", "root/b 1"])
        [['root/a', 'root/b']]
    """
    # Map content string to a list of file paths that share that content
    content_to_paths: dict[str, list[str]] = {}

    for file_info in files:
        # Split the string into exactly two parts: path and content
        # We use maxsplit=1 because the content itself might contain spaces
        parts = file_info.split(" ", 1)
        if len(parts) < 2:
            continue
            
        file_path, content = parts

        # Group paths by their content
        if content not in content_to_paths:
            content_to_paths[content] = []
        content_to_paths[content].append(file_path)

    # Filter the dictionary to only include contents that appear in multiple files
    result: list[list[str]] = []
    for paths in content_to_paths.values():
        if len(paths) > 1:
            result.append(paths)

    return result
