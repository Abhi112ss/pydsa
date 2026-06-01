METADATA = {
    "id": 943,
    "name": "Find the Shortest Superstring",
    "slug": "find-the-shortest-superstring",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "bitmask", "tsp", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n^2 * 2^n)",
    "space_complexity": "O(n * 2^n)",
    "description": "Find the shortest string that contains all given strings as substrings.",
}

def solve(words: list[str]) -> str:
    """
    Finds the shortest superstring that contains all input words as substrings.
    
    This problem is modeled as a Traveling Salesperson Problem (TSP). 
    The 'distance' between two words is the number of characters added to 
    the first word to include the second word (total length - overlap).

    Args:
        words: A list of strings to be included in the superstring.

    Returns:
        The shortest superstring containing all input words.

    Examples:
        >>> solve(["catg", "ctaagt", "gcta", "agcat"])
        'gctaagcatg'
    """
    n = len(words)
    
    # overlap[i][j] stores the length of the suffix of words[i] 
    # that is also a prefix of words[j].
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

    # dp[mask][i] stores the minimum length of a superstring 
    # using words in 'mask' and ending with words[i].
    # parent[mask][i] stores the previous word index to reconstruct the path.
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    # Base case: single words
    for i in range(n):
        dp[1 << i][i] = len(words[i])

    # Fill DP table using bitmasking
    for mask in range(1, 1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            if dp[mask][i] == float('inf'):
                continue
            
            # Try adding a new word 'j' that is not in the current mask
            for j in range(n):
                if mask & (1 << j):
                    continue
                
                new_mask = mask | (1 << j)
                # Cost of adding words[j] after words[i] is its length minus overlap
                new_len = dp[mask][i] + len(words[j]) - overlap[i][j]
                
                if new_len < dp[new_mask][j]:
                    dp[new_mask][j] = new_len
                    parent[new_mask][j] = i

    # Find the end word of the shortest superstring
    full_mask = (1 << n) - 1
    min_len = float('inf')
    last_idx = -1
    for i in range(n):
        if dp[full_mask][i] < min_len:
            min_len = dp[full_mask][i]
            last_idx = i

    # Reconstruct the path of indices using the parent pointers
    path = []
    curr_mask = full_mask
    while last_idx != -1:
        path.append(last_idx)
        prev_idx = parent[curr_mask][last_idx]
        curr_mask ^= (1 << last_idx)
        last_idx = prev_idx
    
    path.reverse()

    # Build the actual string from the path
    result = words[path[0]]
    for i in range(1, len(path)):
        prev, curr = path[i-1], path[i]
        # Append only the non-overlapping part of the next word
        overlap_len = overlap[prev][curr]
        result += words[curr][overlap_len:]
        
    return result
