METADATA = {
    "id": 212,
    "name": "Word Search II",
    "slug": "word-search-ii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["trie", "backtracking", "dfs"],
    "difficulty": "hard",
    "time_complexity": "O(M * (4 * 3^(L-1)))",
    "space_complexity": "O(N)",
    "description": "Find all words from a given list that can be constructed from letters of sequentially adjacent cells in a 2D grid.",
}

def solve(board: list[list[str]], words: list[str]) -> list[str]:
    """
    Args:
        board: A 2D grid of characters.
        words: A list of strings to search for in the grid.

    Returns:
        A list of strings containing all words found in the grid.
    """
    trie = {}
    for word in words:
        current_node = trie
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node["#"] = word

    rows = len(board)
    cols = len(board[0])
    found_words = set()

    def backtrack(row: int, col: int, parent_node: dict):
        char = board[row][col]
        current_node = parent_node[char]

        if "#" in current_node:
            found_words.add(current_node["#"])

        board[row][col] = None

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                next_char = board[new_row][new_col]
                if next_char in current_node:
                    backtrack(new_row, new_col, current_node)

        board[row][col] = char

        if not current_node:
            parent_node.pop(char)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] in trie:
                backtrack(r, c, trie)

    return list(found_words)