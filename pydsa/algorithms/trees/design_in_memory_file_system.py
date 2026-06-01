METADATA = {
    "id": 588,
    "name": "Design In-Memory File System",
    "slug": "design_in_memory_file_system",
    "category": "Design",
    "aliases": [],
    "tags": ["trie", "design", "hash_map"],
    "difficulty": "hard",
    "time_complexity": "O(depth + entries)",
    "space_complexity": "O(total_nodes)",
    "description": "Design a file system that supports creating directories, creating files, reading content, and listing directory contents.",
}

class FileSystemNode:
    """Represents a node in the file system tree (either a directory or a file)."""
    
    def __init__(self, is_file: bool = False):
        self.is_file = is_file
        self.content = ""
        # Using a dict to store children; keys are names, values are FileSystemNode
        self.children: dict[str, "FileSystemNode"] = {}

class FileSystem:
    def __init__(self):
        """Initializes the file system with a root directory."""
        self.root = FileSystemNode(is_file=False)

    def _traverse(self, path: str) -> tuple[FileSystemNode, list[str]]:
        """
        Helper to traverse the path and return the target node and the path components.
        
        Args:
            path: The absolute path string.
            
        Returns:
            A tuple containing the target node and the list of path components.
        """
        parts = [p for p in path.split("/") if p]
        current = self.root
        for part in parts:
            if part not in current.children:
                return current, parts # Return current if path doesn't exist
            current = current.children[part]
        return current, parts

    def _get_node_at_path(self, path: str) -> FileSystemNode:
        """Navigates to the node at the given path. Assumes path exists."""
        parts = [p for p in path.split("/") if p]
        current = self.root
        for part in parts:
            current = current.children[part]
        return current

    def ls(self, path: str) -> list[str]:
        """
        Returns the list of files and directories in the given path.
        If the path is a file, returns a list containing only the file name.

        Args:
            path: The path to list.

        Returns:
            A list of strings representing names in the directory or the file name.
        """
        parts = [p for p in path.split("/") if p]
        current = self.root
        
        # Traverse to the node
        for part in parts:
            if part not in current.children:
                return []
            current = current.children[part]

        if current.is_file:
            return [parts[-1]]
        
        # Return sorted list of children names for directories
        return sorted(current.children.keys())

    def mkdir(self, path: str) -> None:
        """
        Creates a directory at the given path.

        Args:
            path: The path to create.
        """
        parts = [p for p in path.split("/") if p]
        current = self.root
        for part in parts:
            if part not in current.children:
                current.children[part] = FileSystemNode(is_file=False)
            current = current.children[part]

    def add_file(self, path: str, content: str) -> None:
        """
        Creates a file at the given path with the specified content.

        Args:
            path: The path to create the file.
            content: The content of the file.
        """
        parts = [p for p in path.split("/") if p]
        current = self.root
        
        # Traverse to the parent directory
        for i in range(len(parts) - 1):
            part = parts[i]
            if part not in current.children:
                current.children[part] = FileSystemNode(is_file=False)
            current = current.children[part]
            
        # Create the file node at the last part
        file_name = parts[-1]
        if file_name not in current.children:
            current.children[file_name] = FileSystemNode(is_file=True)
        
        current.children[file_name].content = content

    def read_file(self, path: str) -> str:
        """
        Reads the content of the file at the given path.

        Args:
            path: The path to the file.

        Returns:
            The content of the file.
        """
        node = self._get_node_at_path(path)
        return node.content

def solve():
    """
    Example usage of the FileSystem class.
    """
    fs = FileSystem()
    fs.mkdir("/a/b/c")
    fs.add_file("/a/b/c/d", "hello")
    print(fs.ls("/a/b/c"))      # Expected: ["d"]
    print(fs.read_file("/a/b/c/d")) # Expected: "hello"
    fs.mkdir("/a/b/c/e")
    print(fs.ls("/a/b/c"))      # Expected: ["d", "e"]
