METADATA = {
    "id": 2479,
    "name": "Maximum XOR of Two Non-Overlapping Subtrees",
    "slug": "maximum_xor_of_two_non_overlapping_subtrees",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "trie"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum XOR value of two non-overlapping subtrees in a given binary tree.",
}

class TrieNode:
    """A node in the Binary Trie used for XOR maximization."""
    def __init__(self):
        self.children: dict[int, TrieNode] = {}

class Trie:
    """A Binary Trie to store integers and find the maximum XOR for a given value."""
    def __init__(self, bit_length: int = 31):
        self.root = TrieNode()
        self.bit_length = bit_length

    def insert(self, num: int) -> None:
        """Inserts a number into the Trie bit by bit."""
        current = self.root
        for i in range(self.bit_length, -1, -1):
            bit = (num >> i) & 1
            if bit not in current.children:
                current.children[bit] = TrieNode()
            current = current.children[bit]

    def query_max_xor(self, num: int) -> int:
        """Finds the maximum XOR possible for 'num' using values currently in the Trie."""
        current = self.root
        if not current.children:
            return 0
        
        max_xor = 0
        for i in range(self.bit_length, -1, -1):
            bit = (num >> i) & 1
            target = 1 - bit
            # Try to follow the path that flips the current bit to maximize XOR
            if target in current.children:
                max_xor |= (1 << i)
                current = current.children[target]
            elif bit in current.children:
                current = current.children[bit]
            else:
                return 0
        return max_xor

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Calculates the maximum XOR of two non-overlapping subtrees.
    
    Two subtrees are non-overlapping if neither is an ancestor of the other.
    To solve this, we use DFS to compute subtree XORs and entry/exit times 
    to determine subtree ranges. We then use a Trie to find the max XOR 
    between subtrees that do not overlap in their DFS entry/exit intervals.

    Args:
        root: The root of the binary tree.

    Returns:
        The maximum XOR value of two non-overlapping subtrees.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        1 # (Subtree 2 XOR is 2, Subtree 3 XOR is 3. 2^3 = 1)
    """
    if not root:
        return 0

    # subtree_xor[u] stores the XOR sum of all nodes in the subtree rooted at u
    subtree_xor: dict[int, int] = {}
    # entry[u] and exit[u] define the DFS range of the subtree rooted at u
    entry: dict[int, int] = {}
    # exit[u] defines the end of the DFS range
    exit_time: dict[int, int] = {}
    
    timer = 0
    # We use a list to store nodes in order of their entry time to process them
    nodes_by_entry: list[int] = []
    # Map node object ID to its subtree XOR for easy access
    node_to_xor: dict[int, int] = {}
    # Map node object ID to its entry/exit times
    node_to_range: dict[int, tuple[int, int]] = {}

    def dfs_preprocess(node: TreeNode) -> int:
        nonlocal timer
        if not node:
            return 0
        
        node_id = id(node)
        start = timer
        timer += 1
        
        # Calculate XOR sum of current subtree recursively
        current_xor = node.val ^ dfs_preprocess(node.left) ^ dfs_preprocess(node.right)
        
        end = timer
        subtree_xor[node_id] = current_xor
        entry[node_id] = start
        exit_time[node_id] = end
        node_to_xor[node_id] = current_xor
        node_to_range[node_id] = (start, end)
        nodes_by_entry.append(node_id)
        
        return current_xor

    dfs_preprocess(root)

    # To find non-overlapping subtrees, we can use the property that 
    # subtree A and B are non-overlapping if [entryA, exitA] and [entryB, exitB] 
    # are disjoint.
    
    # We sort nodes by their entry time. We can use a sweep-line approach or 
    # a segment tree, but since we need max XOR, a Trie combined with 
    # processing nodes in a specific order is efficient.
    
    # However, the simplest way to ensure non-overlapping is:
    # For every node u, find max XOR of a subtree in its left branch vs 
    # a subtree in its right branch, OR a subtree outside its range.
    # Actually, the problem is simpler: find two nodes u, v such that 
    # u is not an ancestor of v and v is not an ancestor of u.
    
    # Let's use the property: Two subtrees are non-overlapping if one's 
    # exit time is less than the other's entry time.
    
    # Sort nodes by entry time
    sorted_nodes = sorted(nodes_by_entry, key=lambda x: entry[x])
    
    max_val = 0
    
    # Approach: Use two pointers/sweep-line with a Trie.
    # We want to find max(xor[i] ^ xor[j]) where exit[i] < entry[j].
    
    # 1. Sort nodes by exit time to process them as they "finish"
    nodes_by_exit = sorted(nodes_by_entry, key=lambda x: exit_time[x])
    # 2. Sort nodes by entry time to process them as they "start"
    nodes_by_entry_sorted = sorted(nodes_by_entry, key=lambda x: entry[x])
    
    trie = Trie()
    exit_ptr = 0
    
    # Iterate through nodes sorted by entry time. 
    # For each node, all nodes whose exit_time < current_node.entry_time 
    # are guaranteed to be non-overlapping.
    for node_id in nodes_by_entry_sorted:
        curr_entry = entry[node_id]
        
        # Add all subtrees that finished before this one started into the Trie
        while exit_ptr < len(nodes_by_exit) and exit_time[nodes_by_exit[exit_ptr]] <= curr_entry:
            trie.insert(node_to_xor[nodes_by_exit[exit_ptr]])
            exit_ptr += 1
            
        # Query the Trie for the best match for the current subtree
        if exit_ptr > 0:
            max_val = max(max_val, trie.query_max_xor(node_to_xor[node_id]))

    # We must also check the reverse: nodes that start after this one finishes.
    # But the logic above covers all pairs (i, j) where exit[i] <= entry[j].
    # Since the relationship is symmetric, this is sufficient.

    return max_val
