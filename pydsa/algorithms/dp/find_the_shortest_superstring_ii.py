METADATA = {
    "id": 3571,
    "name": "Find the Shortest Superstring II",
    "slug": "find_the_shortest_superstring_ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bit_manipulation", "strings", "tsp"],
    "difficulty": "hard",
    "time_complexity": "O(n^2 * 2^n)",
    "space_complexity": "O(n * 2^n)",
    "description": "Find the shortest string that contains all given strings as substrings using a TSP-style dynamic programming approach.",
}

def solve(words: list[str]) -> str:
    """
    Finds the shortest superstring that contains all strings in the input list.

    This problem is a variation of the Traveling Salesperson Problem (TSP).
    We treat each word as a node and the 'cost' of an edge between word i and word j
    as the number of additional characters needed to append word j after word i.

    Args:
        words: A list of strings to be included in the superstring.

    Returns:
        The shortest superstring containing all input words.

    Examples:
        >>> solve(["abcd", "cdfg", "efgh"])
        'abcdfghegh' (Note: actual result depends on overlap calculation)
    """
    n = len(words)
    
    # overlap[i][j] = length of the suffix of words[i] that is a prefix of words[j]
    overlap = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            len_i, len_j = len(words[i]), len(words[j])
            # Check maximum possible overlap length
            for k in range(min(len_i, len_j), 0, -1):
                if words[i].endswith(words[j][:k]):
                    overlap[i][j] = k
                    break

    # dp[mask][i] = maximum total overlap using words in 'mask', ending with words[i]
    # mask is a bitmask where the k-th bit is 1 if words[k] is included
    dp = [[0] * n for _ in range(1 << n)]
    # parent[mask][i] = the index of the word that preceded words[i] in the optimal path
    parent = [[-1] * n for _ in range(1 << n)]

    # Fill DP table
    for mask in range(1, 1 << n):
        for j in range(n):
            if not (mask & (1 << j)):
                continue
            
            prev_mask = mask ^ (1 << j)
            if prev_mask == 0:
                continue
                
            for i in range(n):
                if prev_mask & (1 << i):
                    # Calculate potential overlap if we transition from i to j
                    val = dp[prev_mask][i] + overlap[i][j]
                    if val > dp[mask][j]:
                        dp[mask][j] = val
                        parent[mask][j] = i

    # Find the end word that gives the maximum total overlap for the full mask
    full_mask = (1 << n) - 1
    max_overlap = -1
    last_word_idx = -1
    for i in range(n):
        if dp[full_mask][i] > max_overlap:
            max_overlap = dp[full_mask][i]
            last_word_idx = i

    # Reconstruct the path using the parent pointers
    path = []
    curr_mask = full_mask
    curr_idx = last_word_idx
    while curr_idx != -1:
        path.append(curr_idx)
        next_idx = parent[curr_mask][curr_idx]
        curr_mask ^= (1 << curr_idx)
        curr_idx = next_idx
    
    path.reverse()

    # Build the superstring based on the reconstructed path
    result = words[path[0]]
    for i in range(1, len(path)):
        prev, curr = path[i-1], path[i]
        # Append only the non-overlapping part of the current word
        overlap_len = overlap[prev][curr]
        result += words[curr][overlap_len:]

    return result
