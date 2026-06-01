METADATA = {
    "id": 663,
    "name": "Equal Tree Partition",
    "slug": "equal-tree-partition",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "hash_set", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a binary tree can be partitioned into two subtrees with equal sums.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> bool:
    """
    Determines if a binary tree can be split into two subtrees with equal sums.

    Args:
        root: The root node of the binary tree.

    Returns:
        True if the tree can be partitioned into two equal sum subtrees, False otherwise.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        False
        >>> root = TreeNode(1, TreeNode(2, TreeNode(1), TreeNode(1)), TreeNode(1))
        >>> solve(root)
        True
    """
    if not root:
        return False

    subtree_sums = set()

    def calculate_subtree_sum(node: TreeNode) -> int:
        """
        Recursively calculates the sum of the subtree rooted at 'node'
        and stores all encountered sums in a set.
        """
        if not node:
            return 0
        
        # Post-order traversal to compute sum of current subtree
        current_sum = (
            node.val + 
            calculate_subtree_sum(node.left) + 
            calculate_subtree_sum(node.right)
        )
        
        # Store the sum of the subtree rooted at this node
        subtree_sums.add(current_sum)
        return current_sum

    # Step 1: Calculate the total sum of the entire tree
    total_sum = calculate_subtree_sum(root)

    # Step 2: Check if total sum is even and if half of it exists as a subtree sum.
    # Note: The total_sum itself is in subtree_sums, but we need a proper partition,
    # so we must ensure the partition is made by cutting an edge, meaning the 
    # resulting subtree sum must be exactly total_sum / 2.
    # Since calculate_subtree_sum adds the root's sum last, we check if 
    # total_sum / 2 exists in the set. If total_sum is odd, it's impossible.
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    
    # We need to find if any subtree (other than the root itself) equals target.
    # However, the set contains the root sum (total_sum). 
    # If target is in the set, it implies a subtree exists that equals half the total.
    # Because target < total_sum (unless total_sum is 0), this naturally excludes 
    # the root unless the tree is empty or specific edge cases occur.
    # To be safe, we can check if target exists in the set after the root sum is added.
    # But if target == total_sum, it's not a partition.
    # Since target = total_sum / 2, target == total_sum only if total_sum == 0.
    # If total_sum is 0, we need to ensure there's a subtree that sums to 0 
    # that is NOT the root itself.
    
    # Re-calculating logic for the 0 case:
    # If total_sum is 0, we need to find if any node (except root) has sum 0.
    # We can modify the set logic or just check if target is in the set 
    # and handle the root sum carefully.
    
    # Let's refine: The set contains all subtree sums. The root sum is total_sum.
    # If target is in the set and target != total_sum, it's a valid partition.
    # If target == total_sum (only happens if total_sum is 0), we need to see 
    # if there's another 0 in the set.
    
    if target == total_sum:
        # This handles the case where total_sum is 0.
        # We need to know if there's at least one other subtree that sums to 0.
        # We can count occurrences or check if the set logic is sufficient.
        # Actually, if total_sum is 0, target is 0. We need to see if 0 appears 
        # more than once in the subtree sums.
        
        # Let's use a frequency map or a simple count instead of a set for robustness.
        return _check_with_frequency(root)

    return target in subtree_sums

def _check_with_frequency(root: TreeNode) -> bool:
    """Helper to handle the edge case where total_sum is 0."""
    sums_list = []
    
    def get_sums(node: TreeNode) -> int:
        if not node:
            return 0
        s = node.val + get_sums(node.left) + get_sums(node.right)
        sums_list.append(s)
        return s
    
    total = get_sums(root)
    if total % 2 != 0:
        return False
    
    target = total // 2
    # We need to find if 'target' exists in sums_list excluding the last element (the root)
    for i in range(len(sums_list) - 1):
        if sums_list[i] == target:
            return True
    return False

# The solve function above is slightly redundant due to the 0-sum edge case.
# Let's provide the clean, single-pass optimal version.

def solve_final(root: TreeNode) -> bool:
    """
    Optimal implementation of Equal Tree Partition.
    """
    if not root:
        return False
    
    subtree_sums = []

    def dfs(node: TreeNode) -> int:
        if not node:
            return 0
        current_sum = node.val + dfs(node.left) + dfs(node.right)
        subtree_sums.append(current_sum)
        return current_sum

    total_sum = dfs(root)
    
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    
    # The last element in subtree_sums is the total_sum (the root).
    # We check all other elements to see if any match the target.
    for i in range(len(subtree_sums) - 1):
        if subtree_sums[i] == target:
            return True
            
    return False

# Re-assigning solve to the clean version for the final output
solve = solve_final