METADATA = {
    "id": 1166,
    "name": "Design File System",
    "slug": "design-file-system",
    "category": "Design",
    "aliases": [],
    "tags": ["trie", "hash_map", "design"],
    "difficulty": "medium",
    "time_complexity": "O(L) per operation, where L is the length of the path",
    "space_complexity": "O(N * L), where N is the number of paths stored",
    "description": "Design a file system that supports creating paths with values and retrieving values by path.",
}

class FileSystem:
    def __init__(self) -> None:
        """
        Initializes the file system using a hash map for O(1) average lookup.
        The root path is implicitly handled by the map.
        """
        self.paths: dict[str, int] = {}

    def createPath(self, path: str, value: int) -> bool:
        """
        Creates a new path with the given value. 
        A path can only be created if its parent path already exists.

        Args:
            path: The full path string to create.
            value: The integer value to associate with the path.

        Returns:
            True if the path was successfully created, False if the path 
            already exists or the parent path does not exist.

        Examples:
            >>> fs = FileSystem()
            >>> fs.createPath("/a", 1)
            True
            >>> fs.createPath("/a/b", 2)
            True
            >>> fs.createPath("/c/d", 3)
            False
        """
        # Check if path is empty or just a root slash (invalid per constraints)
        if not path or path == "/":
            return False
        
        # If path already exists, we cannot create it again
        if path in self.paths:
            return False

        # Find the parent path by stripping the last component
        # e.g., "/a/b/c" -> "/a/b"
        last_slash_index = path.rfind("/")
        parent_path = path[:last_slash_index]

        # If parent_path is empty string, it means the path was "/something"
        # The root "/" is considered to exist implicitly for top-level paths
        if parent_path != "" and parent_path not in self.paths:
            return False

        # Store the path and its value
        self.paths[path] = value
        return True

    def getPathValue(self, path: str) -> int:
        """
        Retrieves the value associated with a given path.

        Args:
            path: The path to look up.

        Returns:
            The integer value associated with the path, or -1 if the path does not exist.

        Examples:
            >>> fs = FileSystem()
            >>> fs.createPath("/a", 1)
            True
            >>> fs.getPathValue("/a")
            1
            >>> fs.getPathValue("/b")
            -1
        """
        # Return the value if it exists, otherwise return -1
        return self.paths.get(path, -1)

def solve():
    """
    Example usage of the FileSystem class.
    """
    fs = FileSystem()
    print(fs.createPath("/a", 1))      # Expected: True
    print(fs.createPath("/a/b", 2))    # Expected: True
    print(fs.createPath("/c/d", 3))    # Expected: False
    print(fs.getPathValue("/a/b"))     # Expected: 2
    print(fs.getPathValue("/c/d"))     # Expected: -1
