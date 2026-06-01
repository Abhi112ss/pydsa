METADATA = {
    "id": 1258,
    "name": "Synonymous Sentences",
    "slug": "synonymous-sentences",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union find", "backtracking", "hash table"],
    "difficulty": "hard",
    "time_complexity": "O(N * K + S * W)",
    "space_complexity": "O(N * K + S * W)",
    "description": "Replace words in a sentence with their synonyms based on provided groups using Union-Find and backtracking.",
}

def solve(sentence: str, synonymGroups: list[list[str]]) -> list[str]:
    """
    Args:
        sentence: A string representing the input sentence.
        synonymGroups: A list of lists where each sub-list contains words that are synonyms.

    Returns:
        A list of all possible sentences formed by replacing words with their synonyms.
    """
    parent = {}

    def find(word: str) -> str:
        if word not in parent:
            parent[word] = word
        if parent[word] != word:
            parent[word] = find(parent[word])
        return parent[word]

    def union(word1: str, word2: str) -> None:
        root1 = find(word1)
        root2 = find(word2)
        if root1 != root2:
            parent[root1] = root2

    for group in synonymGroups:
        for i in range(len(group) - 1):
            union(group[i], group[i + 1])

    synonym_map = {}
    for word in parent:
        root = find(word)
        if root not in synonym_map:
            synonym_map[root] = []
        synonym_map[root].append(word)

    words = sentence.split()
    results = []
    n = len(words)

    def backtrack(index: int, current_sentence: list[str]) -> None:
        if index == n:
            results.append(" ".join(current_sentence))
            return

        original_word = words[index]
        root = find(original_word)
        
        if root in synonym_map:
            options = synonym_map[root]
            for option in options:
                current_sentence.append(option)
                backtrack(index + 1, current_sentence)
                current_sentence.pop()
        else:
            current_sentence.append(original_word)
            backtrack(index + 1, current_sentence)
            current_sentence.pop()

    backtrack(0, [])
    return results