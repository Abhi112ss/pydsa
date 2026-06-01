METADATA = {
    "id": 428,
    "name": "Serialize and Deserialize N-ary Tree",
    "slug": "serialize_and_deserialize_n_ary_tree",
    "category": "trees",
    "aliases": ["serialize n ary tree", "deserialize n ary tree"],
    "tags": ["tree", "depth_first_search", "breadth_first_search", "string", "design"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Design an algorithm to serialize and deserialize an N-ary tree.",
}

class Node:
    def __init__(self, val: int | None = None, children: list['Node'] | None = None):
        self.val = val
        self.children = children if children is not None else []

class Codec:
    def serialize(self, root: Node | None) -> str:
        if not root:
            return ""
        
        result = []
        
        def dfs(node: Node):
            if not node:
                return
            result.append(str(node.val))
            result.append(str(len(node.children)))
            for child in node.children:
                dfs(child)
                
        dfs(root)
        return ",".join(result)

    def deserialize(self, data: str) -> Node | None:
        if not data:
            return None
            
        tokens = data.split(",")
        iterator = iter(tokens)
        
        def build() -> Node:
            val = int(next(iterator))
            num_children = int(next(iterator))
            node = Node(val)
            for _ in range(num_children):
                node.children.append(build())
            return node
            
        return build()

def solve(root: Node | None) -> Node | None:
    """
    Serializes and then deserializes an N-ary tree.
    
    Args:
        root: The root of the N-ary tree.
        
    Returns:
        The root of the deserialized N-ary tree.
    """
    codec = Codec()
    return codec.deserialize(codec.serialize(root))