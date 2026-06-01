METADATA = {
    "id": 894,
    "name": "All Possible Full Binary Trees",
    "slug": "all-possible-full-binary-trees",
    "category": "Tree",
    "aliases": [],
    "tags": ["recursion", "memoization", "dynamic programming", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(2^n)",
    "description": "Given an integer n, return all possible full binary trees with n nodes.",
}

def solve(n: int) -> list[list]:
    """
    Args:
        n: The number of nodes in the full binary tree.

    Returns:
        A list of all possible full binary tree structures represented as nested lists.
    """
    memo = {}

    def build_trees(nodes: int) -> list[list]:
        if nodes % 2 == 0:
            return []
        
        if nodes == 1:
            return [[]]
        
        if nodes in memo:
            return memo[nodes]
        
        results = []
        for left_count in range(1, nodes, 2):
            right_count = nodes - 1 - left_count
            
            left_subtrees = build_trees(left_count)
            right_subtrees = build_trees(right_count)
            
            for left in left_subtrees:
                for right in right_subtrees:
                    results.append([left, right])
        
        memo[nodes] = results
        return results

    return build_trees(n)