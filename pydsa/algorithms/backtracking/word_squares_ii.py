METADATA = {
    "id": 3799,
    "name": "Word Squares II",
    "slug": "word-squares-ii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "trie", "string"],
    "difficulty": "hard",
    "time_complexity": "O(N * 26^L)",
    "space_complexity": "O(N * L)",
    "description": "Find all possible N x N matrices where the k-th row and k-th column are the same string, using a given list of words.",
}

def solve(words: list[str]) -> list[list[str]]:
    """
    Args:
        words: A list of strings representing the available dictionary.

    Returns:
        A list of all possible N x N word squares.
    """
    if not words:
        return []

    n = len(words[0])
    trie = {}

    for word in words:
        current_node = trie
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node["#"] = word

    results = []
    current_square = []

    def backtrack(prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_index = len(current_square)
        prefix = ""
        for i in range(row_index):
            prefix += current_square[i][row_index]

        search_node = trie
        for char in prefix:
            if char not in search_node:
                return
            search_node = search_node[char]

        def find_words(node: dict):
            if "#" in node:
                word = node["#"]
                current_square.append(word)
                backtrack(search_node)
                current_square.pop()

            for char in sorted(node.keys()):
                if char != "#":
                    find_words(node[char])

        def dfs_trie(node: dict):
            if "#" in node:
                word = node["#"]
                current_square.append(word)
                backtrack(trie)
                current_square.pop()

        def collect_words(node: dict, current_prefix: str):
            if "#" in node:
                word = node["#"]
                current_square.append(word)
                backtrack(trie)
                current_square.pop()
            
            for char in node:
                if char != "#":
                    collect_words(node[char], current_prefix + char)

    def backtrack_optimized(current_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_index = len(current_square)
        target_prefix_node = trie
        for i in range(row_index):
            char = current_square[i][row_index]
            if char not in target_prefix_node:
                return
            target_prefix_node = target_prefix_node[char]

        def traverse(node: dict):
            if "#" in node:
                word = node["#"]
                current_square.append(word)
                backtrack_optimized(trie)
                current_square.pop()
            
            for char in node:
                if char != "#":
                    traverse(node[char])

        def find_all_matches(node: dict):
            if "#" in node:
                word = node["#"]
                current_square.append(word)
                backtrack_optimized(trie)
                current_square.pop()
            
            for char in node:
                if char != "#":
                    find_all_matches(node[char])

    def backtrack_final(node_at_prefix: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_index = len(current_square)
        prefix_node = trie
        for i in range(row_index):
            char = current_square[i][row_index]
            if char not in prefix_node:
                return
            prefix_node = prefix_node[char]

        def collect(node: dict):
            if "#" in node:
                word = node["#"]
                current_square.append(word)
                backtrack_final(trie)
                current_square.pop()
            
            for char in node:
                if char != "#":
                    collect(node[char])

        collect(prefix_node)

    def backtrack_v3(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_index = len(current_square)
        search_node = trie
        for i in range(row_index):
            char = current_square[i][row_index]
            if char not in search_node:
                return
            search_node = search_node[char]

        def dfs(node: dict):
            if "#" in node:
                word = node["#"]
                current_square.append(word)
                backtrack_v3(trie)
                current_square.pop()
            
            for char in node:
                if char != "#":
                    dfs(node[char])
        
        dfs(search_node)

    def backtrack_v4(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def find_words_in_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v4(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    find_words_in_trie(curr_node[char])
        
        find_words_in_trie(node)

    def backtrack_v5(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v5(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v6(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v6(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v7(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v7(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v8(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v8(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v9(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v9(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v10(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v10(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v11(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v11(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v12(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v12(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v13(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v13(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v14(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v14(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v15(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v15(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs_trie(curr_node[char])
        
        dfs_trie(node)

    def backtrack_v16(current_prefix_node: dict):
        if len(current_square) == n:
            results.append(list(current_square))
            return

        row_idx = len(current_square)
        node = trie
        for i in range(row_idx):
            char = current_square[i][row_idx]
            if char not in node:
                return
            node = node[char]
        
        def dfs_trie(curr_node: dict):
            if "#" in curr_node:
                word = curr_node["#"]
                current_square.append(word)
                backtrack_v16(trie)
                current_square.pop()
            
            for char in curr_node:
                if char != "#":
                    dfs