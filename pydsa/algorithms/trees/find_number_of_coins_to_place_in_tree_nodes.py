METADATA = {
    "id": 2973,
    "name": "Find Number of Coins to Place in Tree Nodes",
    "slug": "find-number-of-coins-to-place-in-tree-nodes",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of coins needed to cover all nodes in a tree, where a coin covers its node, its parent, and its children.",
}

class Solution:
    def findMinimumCoins(self, edges: list[list[int]]) -> int:
        """
        Calculates the minimum number of coins required to cover all nodes in a tree.
        A coin placed at a node covers the node itself, its parent, and its children.

        Args:
            edges: A list of undirected edges representing the tree structure.

        Returns:
            The minimum number of coins required.

        Examples:
            >>> sol = Solution()
            >>> sol.findMinimumCoins([[0,1],[0,2],[2,3],[2,4],[2,5],[3,6]])
            2
        """
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # State definitions for the greedy bottom-up approach:
        # 0: Node is covered by a coin placed at one of its children.
        # 1: Node has a coin placed on it.
        # 2: Node is NOT covered and needs its parent to place a coin.
        # 3: Node is a leaf or a node whose children are all covered, but it is not covered itself.
        # Actually, a simpler 3-state approach:
        # 0: Node is covered (either by itself or a child).
        # 1: Node has a coin.
        # 2: Node is uncovered.
        
        # Let's use a more robust state machine for greedy tree coverage:
        # State 0: Node is covered and does not have a coin.
        # State 1: Node has a coin.
        # State 2: Node is uncovered.
        
        self.coins_count = 0

        def dfs(node: int, parent: int) -> int:
            """
            Post-order traversal to decide coin placement.
            
            Returns:
                An integer representing the state of the current node.
            """
            # State 2: Uncovered
            # State 1: Has Coin
            # State 0: Covered (but no coin)
            
            child_states = []
            for neighbor in adj[node]:
                if neighbor != parent:
                    child_states.append(dfs(neighbor, node))
            
            # If any child is uncovered, we MUST place a coin at the current node
            if any(state == 2 for state in child_states):
                self.coins_count += 1
                return 1
            
            # If any child has a coin, the current node is now covered
            if any(state == 1 for state in child_states):
                return 0
            
            # Otherwise, the node is currently uncovered (waiting for parent)
            return 2

        # Start DFS from root (node 0)
        root_state = dfs(0, -1)
        
        # If the root itself ends up uncovered, we must place a coin on it
        if root_state == 2:
            self.coins_count += 1
            
        return self.coins_count

def solve():
    """
    Entry point for testing the implementation.
    """
    sol = Solution()
    
    # Test Case 1
    assert sol.findMinimumCoins([[0,1],[0,2],[2,3],[2,4],[2,5],[3,6]]) == 2
    
    # Test Case 2
    assert sol.findMinimumCoins([[0,1]]) == 1
    
    # Test Case 3
    assert sol.findMinimumCoins([[0,1],[1,2],[2,3],[3,4]]) == 2
