METADATA = {
    "id": 3043,
    "name": "Find the Length of the Longest Common Prefix",
    "slug": "find-the-length-of-the-longest-common-prefix",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "trie", "prefix"],
    "difficulty": "medium",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N * M)",
    "description": "Find the length of the longest common prefix among all pairs of strings in a given array.",
}

def solve(words: list[str]) -> int:
    """
    Finds the length of the longest common prefix among all pairs of strings in the array.
    
    The problem asks for the maximum length of a common prefix shared by any two 
    distinct strings in the input list. This is equivalent to finding the longest 
    prefix that appears at least twice in the set of all prefixes of all words.

    Args:
        words: A list of strings.

    Returns:
        The length of the longest common prefix found between any two strings.

    Examples:
        >>> solve(["abcde", "fghij", "abcfg"])
        3
        >>> solve(["a", "b", "c"])
        0
        >>> solve(["apple", "apply", "ape"])
        4
    """
    if not words:
        return 0

    # A Trie node structure to store character transitions and a count
    # of how many words pass through this specific prefix.
    class TrieNode:
        def __init__(self):
            self.children: dict[str, TrieNode] = {}
            self.count: int = 0

    root = TrieNode()
    max_prefix_len = 0

    for word in words:
        current_node = root
        current_depth = 0
        
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            
            current_node = current_node.children[char]
            current_depth += 1
            
            # Increment the count of words sharing this prefix.
            # If count becomes 2, it means we found a common prefix between 
            # the current word and a previously inserted word.
            current_node.count += 1
            
            if current_node.count >= 2:
                # Update the global maximum length found so far.
                if current_depth > max_prefix_len:
                    max_prefix_len = current_depth

    return max_prefix_len
