METADATA = {
    "id": 96,
    "name": "Unique Binary Search Trees",
    "slug": "unique-binary-search-trees",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "trees"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Given an integer n, return the number of structurally unique Binary Search Trees (BSTs) that consist of nodes with values from 1 to n.",
}

def solve(n: int) -> int:
    """
    Calculates the number of structurally unique BSTs that can be formed with n nodes.
    
    The problem follows the Catalan number sequence. For a given number of nodes n, 
    if we pick 'i' as the root, there are (i-1) nodes in the left subtree and 
    (n-i) nodes in the right subtree. The total number of unique BSTs for a 
    fixed root is the product of the number of unique left subtrees and 
    unique right subtrees.

    Args:
        n: The number of nodes.

    Returns:
        The total number of unique BSTs.

    Examples:
        >>> solve(3)
        5
        >>> solve(1)
        1
    """
    if n <= 1:
        return 1

    # dp[i] stores the number of unique BSTs that can be formed with i nodes.
    dp = [0] * (n + 1)
    
    # Base cases: 0 nodes (empty tree) or 1 node result in 1 unique structure.
    dp[0] = 1
    dp[1] = 1

    # Fill the DP table for all node counts from 2 up to n.
    for total_nodes in range(2, n + 1):
        # Try each node 'root_val' as the root of the tree.
        # 'root_val' ranges from 1 to total_nodes.
        for root_val in range(1, total_nodes + 1):
            # Left subtree will have (root_val - 1) nodes.
            # Right subtree will have (total_nodes - root_val) nodes.
            left_subtrees = dp[root_val - 1]
            right_subtrees = dp[total_nodes - root_val]
            
            # The number of unique BSTs with 'root_val' as root is the product 
            # of unique left and right subtrees.
            dp[total_nodes] += left_subtrees * right_subtrees

    return dp[n]
