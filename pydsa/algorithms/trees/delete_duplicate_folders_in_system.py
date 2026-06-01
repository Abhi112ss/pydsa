METADATA = {
    "id": 1948,
    "name": "Delete Duplicate Folders in System",
    "slug": "delete-duplicate-folders-in-system",
    "category": "Hard",
    "aliases": [],
    "tags": ["trie", "serialization", "hash_map", "tree"],
    "difficulty": "hard",
    "time_complexity": "O(N * L * log N)",
    "space_complexity": "O(N * L)",
    "description": "Remove all subtrees that have the same structure and content from a file system represented as a tree.",
}

from collections import defaultdict

def solve(paths: list[list[str]]) -> list[list[str]]:
    """
    Args:
        paths: A list of paths where each path is a list of strings representing folder names.

    Returns:
        A list of paths that remain after deleting duplicate folder structures.
    """
    class FolderNode:
        def __init__(self, name: str):
            self.name = name
            self.children = {}
            self.is_deleted = False

    root = FolderNode("")

    for path in paths:
        current = root
        for folder in path:
            if folder not in current.children:
                current.children[folder] = FolderNode(folder)
            current = current.children[folder]

    structure_map = defaultdict(list)

    def serialize(node: FolderNode) -> str:
        if not node.children:
            return ""
        
        child_structures = []
        for child_name in sorted(node.children.keys()):
            child_node = node.children[child_name]
            child_structure = serialize(child_node)
            child_structures.append(f"({child_name}{child_structure})")
        
        serialized_string = "".join(child_structures)
        structure_map[serialized_string].append(node)
        return serialized_string

    serialize(root)

    for structure in structure_map:
        if len(structure_map[structure]) > 1:
            for node in structure_map[structure]:
                node.is_deleted = True

    result = []

    def collect_paths(node: FolderNode, current_path: list[str]):
        if node.is_deleted:
            return
        
        if node.name != "":
            result.append(list(current_path + [node.name]))
            
        for child_name in sorted(node.children.keys()):
            child_node = node.children[child_name]
            collect_paths(child_node, current_path + [node.name])

    for child_name in sorted(root.children.keys()):
        collect_paths(root.children[child_name], [])

    return result