METADATA = {
    "id": 388,
    "name": "Longest Absolute File Path",
    "slug": "longest-absolute-file-path",
    "category": "String",
    "aliases": [],
    "tags": ["string-parsing", "stack", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest absolute file path in a string representing a file system structure.",
}

def solve(input_str: str) -> int:
    """
    Calculates the length of the longest absolute file path in a given file system string.

    The input string represents a file system where directories and files are 
    separated by newline characters, and indentation (tabs) represents depth.

    Args:
        input_str: A string representing the file system structure.

    Returns:
        The length of the longest absolute file path. Returns 0 if no file is found.

    Examples:
        >>> solve("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
        32
        >>> solve("dir\n\tsubdir1\n\t\tfile1.ext\n\tsubdir2\n\t\tfile2.ext")
        32
    """
    max_length = 0
    # path_lengths[depth] stores the cumulative length of the path up to that depth
    # depth 0 is the root level. We use a dictionary or list to track lengths.
    # Using a dictionary to handle arbitrary depths easily.
    path_lengths = {0: 0}

    # Split by newline to process each directory/file entry individually
    for line in input_str.split("\n"):
        # The number of tabs indicates the depth of the current item
        # lstrip('\t') removes leading tabs to get the actual name
        name = line.lstrip("\t")
        depth = len(line) - len(name)

        if "." in name:
            # If the name contains a '.', it is a file.
            # Calculate total length: length of parent path + current name length
            # Note: path_lengths[depth] is the length of the directory containing this file
            current_file_path_len = path_lengths[depth] + len(name)
            max_length = max(max_length, current_file_path_len)
        else:
            # If it is a directory, update the path length for the next depth level
            # We add 1 to account for the '/' character that separates directories
            path_lengths[depth + 1] = path_lengths[depth] + len(name) + 1

    return max_length
