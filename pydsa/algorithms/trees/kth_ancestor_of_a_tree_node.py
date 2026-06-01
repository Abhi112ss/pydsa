METADATA = {
    "id": 1483,
    "name": "Kth Ancestor of a Tree Node",
    "slug": "kth-ancestor-of-a-tree-node",
    "category": "Design",
    "aliases": [],
    "tags": ["binary_lifting", "trees", "binary_lifting"],
    "difficulty": "hard",
    "time_complexity": "O(N log N) preprocessing, O(log K) per query",
    "space_complexity": "O(N log N)",
    "description": "Design a data structure to find the kth ancestor of a node in a tree using binary lifting.",
}

class KthAncestor:
    def __init__(self, n: int, parent: list[int]):
        """
        Initializes the data structure with the tree structure.

        Args:
            n: The number of nodes in the tree.
            parent: A list where parent[i] is the parent of node i.
        """
        self.n = n
        # Calculate the maximum power of 2 needed for binary lifting
        # log2(n) is approximately the number of bits needed
        self.max_log = n.bit_length()
        
        # up[i][j] stores the (2^j)-th ancestor of node i
        # Using a 2D list for binary lifting table
        self.up = [[-1] * self.max_log for _ in range(n)]
        
        # Base case: the 2^0 (1st) ancestor is the direct parent
        for i in range(n):
            self.up[i][0] = parent[i]
            
        # Precompute the binary lifting table
        # The 2^j-th ancestor is the 2^(j-1)-th ancestor of the 2^(j-1)-th ancestor
        for j in range(1, self.max_log):
            for i in range(n):
                mid_ancestor = self.up[i][j-1]
                if mid_ancestor != -1:
                    self.up[i][j] = self.up[mid_ancestor][j-1]
                else:
                    self.up[i][j] = -1

    def getKthAncestor(self, node: int, k: int) -> int:
        """
        Finds the kth ancestor of the given node.

        Args:
            node: The starting node index.
            k: The distance to the ancestor.

        Returns:
            The index of the kth ancestor, or -1 if it does not exist.

        Examples:
            >>> obj = KthAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
            >>> obj.getKthAncestor(3, 2)
            0
            >>> obj.getKthAncestor(3, 3)
            -1
        """
        current_node = node
        
        # Iterate through the bits of k
        # If the j-th bit of k is set, jump by 2^j ancestors
        for j in range(self.max_log):
            if (k >> j) & 1:
                current_node = self.up[current_node][j]
                # If we jump out of the tree, return -1 immediately
                if current_node == -1:
                    return -1
                    
        return current_node

def solve():
    """
    Example usage of the KthAncestor class.
    """
    # Example 1
    n1 = 7
    parent1 = [-1, 0, 0, 1, 1, 2, 2]
    obj1 = KthAncestor(n1, parent1)
    print(obj1.getKthAncestor(3, 2))  # Expected: 0
    print(obj1.getKthAncestor(3, 3))  # Expected: -1

    # Example 2
    n2 = 5
    parent2 = [-1, 0, 0, 1, 1]
    obj2 = KthAncestor(n2, parent2)
    print(obj2.getKthAncestor(4, 2))  # Expected: 0
    print(obj2.getKthAncestor(4, 3))  # Expected: -1
