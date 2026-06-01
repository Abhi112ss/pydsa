METADATA = {
    "id": 440,
    "name": "K-th Smallest in Lexicographical Order",
    "slug": "k-th-smallest-in-lexicographical-order",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "trie", "math"],
    "difficulty": "hard",
    "time_complexity": "O((log n)^2)",
    "space_complexity": "O(1)",
    "description": "Find the k-th smallest integer in lexicographical order from 1 to n.",
}

def solve(n: int, k: int) -> int:
    """
    Finds the k-th smallest integer in lexicographical order from 1 to n.

    The algorithm treats the numbers as a prefix tree (trie) where each node 
    represents a prefix. We traverse the tree greedily. For each prefix, 
    we calculate how many numbers exist in its subtree. If k is greater 
    than the subtree size, we skip the entire subtree. Otherwise, we 
    descend into the subtree.

    Args:
        n: The upper bound of the range [1, n].
        k: The target rank in lexicographical order.

    Returns:
        The k-th smallest integer in lexicographical order.

    Examples:
        >>> solve(13, 2)
        2
        >>> solve(13, 3)
        3
    """
    def count_steps(current: int, n: int) -> int:
        """
        Calculates the number of nodes in the subtree rooted at 'current'.
        
        Args:
            current: The current prefix.
            n: The upper bound.
            
        Returns:
            The count of integers in the range [1, n] that have 'current' as a prefix.
        """
        steps = 0
        first = current
        last = current
        while first <= n:
            # Add the number of nodes at the current level of the subtree
            # We take the minimum of n and the end of the current range
            steps += min(n, last) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps

    current_num = 1
    # We decrement k because we start at the first element (1)
    k -= 1

    while k > 0:
        steps = count_steps(current_num, n)
        if steps <= k:
            # If the k-th element is not in this subtree, skip the subtree
            # and move to the next sibling (current_num + 1)
            k -= steps
            current_num += 1
        else:
            # If the k-th element is in this subtree, move to the first child
            # (current_num * 10) and decrement k by 1 for the current node itself
            k -= 1
            current_num *= 10

    return current_num
