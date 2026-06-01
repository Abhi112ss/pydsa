METADATA = {
    "id": 2738,
    "name": "Count Occurrences in Text",
    "slug": "count-occurrences-in-text",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "hash_map", "kmp", "aho-corasick"],
    "difficulty": "medium",
    "time_complexity": "O(N + Σ|patterns|)",
    "space_complexity": "O(Σ|patterns|)",
    "description": "Count the total number of occurrences of multiple patterns within a given text.",
}

from collections import deque, defaultdict

class AhoCorasick:
    """
    Implementation of the Aho-Corasick automaton for efficient multi-pattern matching.
    """
    def __init__(self, patterns: list[str]):
        # trie[node][char] = next_node
        self.trie: list[dict[str, int]] = [{}]
        # count[node] stores how many patterns end at this node or its failure link ancestors
        self.count: list[int] = [0]
        # fail[node] stores the failure link for the node
        self.fail: list[int] = [0]
        
        self._build_trie(patterns)
        self._build_automaton()

    def _build_trie(self, patterns: list[str]) -> None:
        for pattern in patterns:
            current_node = 0
            for char in pattern:
                if char not in self.trie[current_node]:
                    self.trie[current_node][char] = len(self.trie)
                    self.trie.append({})
                    self.count.append(0)
                current_node = self.trie[current_node][char]
            self.count[current_node] += 1

    def _build_automaton(self) -> None:
        self.fail = [0] * len(self.trie)
        queue = deque()

        # Initialize depth 1 nodes
        for char, next_node in self.trie[0].items():
            queue.append(next_node)

        while queue:
            u = queue.popleft()
            for char, v in self.trie[u].items():
                # Find the failure link for child v
                f = self.fail[u]
                while f > 0 and char not in self.trie[f]:
                    f = self.fail[f]
                
                self.fail[v] = self.trie[f][char] if char in self.trie[f] else 0
                
                # Key step: Accumulate counts from failure links to handle overlapping patterns
                # If a pattern is a suffix of another, it's counted via the failure link
                self.count[v] += self.count[self.fail[v]]
                queue.append(v)

    def count_matches(self, text: str) -> int:
        total_matches = 0
        current_node = 0
        for char in text:
            # Follow failure links until we find a transition or reach root
            while current_node > 0 and char not in self.trie[current_node]:
                current_node = self.fail[current_node]
            
            if char in self.trie[current_node]:
                current_node = self.trie[current_node][char]
            else:
                current_node = 0
            
            # Add the pre-calculated count of patterns ending at this state
            total_matches += self.count[current_node]
        return total_matches

def solve(text: str, patterns: list[str]) -> int:
    """
    Counts the total occurrences of all patterns in the given text using Aho-Corasick.

    Args:
        text: The source string to search within.
        patterns: A list of pattern strings to search for.

    Returns:
        The total number of times any pattern appears in the text.

    Examples:
        >>> solve("ababc", ["ab", "abc"])
        3
        >>> solve("aaaaa", ["aa"])
        4
    """
    if not patterns or not text:
        return 0
        
    automaton = AhoCorasick(patterns)
    return automaton.count_matches(text)
