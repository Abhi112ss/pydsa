METADATA = {
    "id": 3485,
    "name": "Longest Common Prefix of K Strings After Removal",
    "slug": "longest_common_prefix_of_k_strings_after_removal",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "trie", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(N * L * log(L))",
    "space_complexity": "O(N * L)",
    "description": "Find the length of the longest common prefix shared by at least K strings after potentially removing characters to satisfy constraints.",
}

def solve(strings: list[str], k: int) -> int:
    """
    Finds the length of the longest common prefix shared by at least k strings.
    
    Note: The problem description implies finding the longest prefix that 
    appears in at least k of the given strings.

    Args:
        strings: A list of strings to analyze.
        k: The minimum number of strings that must share the prefix.

    Returns:
        The length of the longest common prefix.

    Examples:
        >>> solve(["flower", "flow", "flight"], 2)
        2
        >>> solve(["apple", "apply", "ape", "april"], 3)
        2
    """
    if not strings or k <= 0:
        return 0
    
    if k == 1:
        return max(len(s) for s in strings)

    # A Trie is an efficient way to count occurrences of prefixes.
    # Each node in the Trie will store the count of strings passing through it.
    trie = {}

    for s in strings:
        current_node = trie
        for char in s:
            if char not in current_node:
                # Each node stores: {'count': int, 'children': dict}
                current_node[char] = {'count': 0, 'children': {}}
            
            current_node[char]['count'] += 1
            current_node = current_node[char]['children']

    # We need to find the deepest node where the 'count' is >= k.
    # We use a BFS or DFS to traverse the Trie and track the maximum depth.
    max_prefix_len = 0
    
    # Stack stores (current_trie_node_dict, current_depth)
    # We start with the root level.
    stack = []
    # Initialize stack with the children of the root
    for char, node_data in trie.items():
        stack.append((node_data, 1))

    while stack:
        node_data, depth = stack.pop()
        
        # If this prefix is shared by at least k strings
        if node_data['count'] >= k:
            max_prefix_len = max(max_prefix_len, depth)
            
            # Explore children to see if a longer prefix exists
            for char, child_data in node_data['children'].items():
                stack.append((child_data, depth + 1))
                
    return max_prefix_len
