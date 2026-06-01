METADATA = {
    "id": 2791,
    "name": "Count Paths That Can Form a Palindrome in a Tree",
    "slug": "count-paths-that-can-form-a-palindrome-in-a-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "bit_manipulation", "dfs", "centroid_decomposition"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of paths in a tree where the characters on the path can be rearranged to form a palindrome.",
}

def solve(n: int, edges: list[list[int]], s: str) -> int:
    """
    Counts the number of paths in a tree that can form a palindrome.
    A path can form a palindrome if at most one character appears an odd number of times.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges [u, v].
        s: A string representing the character at each node.

    Returns:
        The total number of paths that can form a palindrome.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], "aba")
        3
        >>> solve(5, [[0, 1], [1, 2], [1, 3], [3, 4]], "abcde")
        5
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Convert characters to bitmasks (a=1, b=2, c=4, ...)
    node_masks = [1 << (ord(c) - ord('a')) for c in s]
    
    # To track visited nodes during centroid decomposition
    removed = [False] * n
    subtree_size = [0] * n

    def get_size(u: int, p: int) -> int:
        size = 1
        for v in adj[u]:
            if v != p and not removed[v]:
                size += get_size(v, u)
        subtree_size[u] = size
        return size

    def get_centroid(u: int, p: int, total_size: int) -> int:
        for v in adj[u]:
            if v != p and not removed[v] and subtree_size[v] > total_size // 2:
                return get_centroid(v, u, total_size)
        return u

    total_palindrome_paths = 0

    def decompose(u: int) -> None:
        nonlocal total_palindrome_paths
        
        # Find centroid of the current component
        current_size = get_size(u, -1)
        centroid = get_centroid(u, -1, current_size)
        removed[centroid] = True

        # mask_counts stores the frequency of bitmasks encountered in paths starting from centroid
        # A path from u to v through centroid has mask: mask(u) ^ mask(centroid) ^ mask(v)
        # We want mask(u) ^ mask(v) ^ mask(centroid) to have 0 or 1 bits set.
        # This is equivalent to: mask(u) ^ mask(v) == mask(centroid) ^ (0 or 1-bit-mask)
        mask_counts = {0: 1} # Base case: the centroid itself (mask 0 relative to centroid)
        
        # We process each subtree of the centroid one by one to avoid paths within the same subtree
        for v in adj[centroid]:
            if not removed[v]:
                subtree_paths = []
                
                # DFS to collect all path masks in the current subtree relative to the centroid
                stack = [(v, centroid, node_masks[v])]
                while stack:
                    curr, p, curr_mask = stack.pop()
                    subtree_paths.append(curr_mask)
                    
                    # Check if this path from centroid to curr can form a palindrome
                    # Path mask = curr_mask ^ node_masks[centroid]
                    path_to_centroid = curr_mask ^ node_masks[centroid]
                    if path_to_centroid == 0 or (path_to_centroid & (path_to_centroid - 1)) == 0:
                        total_palindrome_paths += 1
                    
                    for neighbor in adj[curr]:
                        if neighbor != p and not removed[neighbor]:
                            stack.append((neighbor, curr, curr_mask ^ node_masks[neighbor]))
                
                # For each path in the current subtree, check against paths in previously processed subtrees
                for path_mask in subtree_paths:
                    # Target mask for path(u) ^ path(v) ^ mask(centroid) to be 0 or 1-bit
                    # Let M = path_mask ^ node_masks[centroid]. We need M ^ prev_mask to be 0 or 1-bit.
                    # So prev_mask must be M ^ 0 or M ^ (1 << i)
                    target_base = path_mask ^ node_masks[centroid]
                    
                    # Check for 0 bits set (even parity)
                    if target_base in mask_counts:
                        total_palindrome_paths += mask_counts[target_base]
                    
                    # Check for 1 bit set (odd parity)
                    for i in range(26):
                        target_odd = target_base ^ (1 << i)
                        if target_odd in mask_counts:
                            total_palindrome_paths += mask_counts[target_odd]
                
                # Add current subtree paths to the global mask_counts for the next subtrees
                for path_mask in subtree_paths:
                    mask_counts[path_mask] = mask_counts.get(path_mask, 0) + 1

        # Recurse to decompose subtrees
        for v in adj[centroid]:
            if not removed[v]:
                decompose(v)

    decompose(0)
    return total_palindrome_paths
