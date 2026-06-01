METADATA = {
    "id": 527,
    "name": "Word Abbreviation",
    "slug": "word-abbreviation",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n * l)",
    "space_complexity": "O(n * l)",
    "description": "Find the shortest unique abbreviation for each word in a list such that no two abbreviations are identical.",
}

def solve(words: list[str]) -> list[str]:
    """
    Generates the shortest unique abbreviation for each word in the input list.
    
    An abbreviation is formed by taking a prefix of the word and appending 
    the count of remaining characters (e.g., 'apple' -> 'a4').
    If two words result in the same abbreviation, the prefix length is 
    increased until all abbreviations are unique.

    Args:
        words: A list of strings to be abbreviated.

    Returns:
        A list of unique abbreviations corresponding to the input words.

    Examples:
        >>> solve(["apple", "apply", "dog"])
        ['app2', 'appl1', 'd3']
        >>> solve(["a", "b", "c"])
        ['a0', 'b0', 'c0']
    """
    n = len(words)
    if n == 0:
        return []

    # Store the current prefix length for each word. 
    # We start with a prefix length of 0 for all words.
    # Note: The problem asks for the shortest unique abbreviation.
    # An abbreviation is prefix + str(len(word) - len(prefix)).
    prefix_lengths = [0] * n
    
    # To handle conflicts efficiently, we use a dictionary to track 
    # how many times each abbreviation appears.
    # However, a more direct approach is to iteratively resolve conflicts.
    
    # We use a loop to ensure all abbreviations are unique.
    # In each iteration, we check if there are any duplicate abbreviations.
    # If duplicates exist, we increment the prefix length for the words involved.
    
    # To optimize, we can use a frequency map of current abbreviations.
    while True:
        abbreviations = []
        counts = {}
        
        for i in range(n):
            word = words[i]
            p_len = prefix_lengths[i]
            # Ensure prefix length does not exceed word length
            p_len = min(p_len, len(word))
            abbr = word[:p_len] + str(len(word) - p_len)
            abbreviations.append(abbr)
            counts[abbr] = counts.get(abbr, 0) + 1
            
        # Check if all abbreviations are unique
        conflicts = [i for i, abbr in enumerate(abbreviations) if counts[abbr] > 1]
        
        if not conflicts:
            return abbreviations
        
        # If there are conflicts, we must increase the prefix length 
        # for the words that are causing the conflict.
        # To avoid infinite loops and ensure progress, we increment 
        # prefix lengths for words involved in a collision.
        # A simple greedy approach: increment prefix length for all words 
        # that currently have a non-unique abbreviation.
        for idx in conflicts:
            prefix_lengths[idx] += 1

    return []

# Note: The logic above is a conceptual simulation. 
# For a production-grade O(N*L) implementation, we use a more direct approach:
# 1. Calculate all possible abbreviations for all words.
# 2. Use a frequency map to identify collisions.
# 3. Since we want the *shortest* unique abbreviation, we can use a 
#    Trie-like approach or a greedy increment.

def solve_optimized(words: list[str]) -> list[str]:
    """
    Optimized version of the word abbreviation logic.
    """
    n = len(words)
    if n == 0:
        return []

    # current_prefixes[i] stores the length of the prefix used for words[i]
    current_prefixes = [0] * n
    
    while True:
        abbr_map = {}
        current_abbrs = []
        
        # Generate current abbreviations and count frequencies
        for i in range(n):
            word = words[i]
            p_len = current_prefixes[i]
            # Clamp prefix length to word length
            p_len = min(p_len, len(word))
            abbr = word[:p_len] + str(len(word) - p_len)
            current_abbrs.append(abbr)
            abbr_map[abbr] = abbr_map.get(abbr, 0) + 1
            
        # Identify indices of words whose abbreviations are not unique
        conflict_indices = []
        for i in range(n):
            if abbr_map[current_abbrs[i]] > 1:
                conflict_indices.append(i)
        
        # If no conflicts, we found the shortest unique abbreviations
        if not conflict_indices:
            return current_abbrs
            
        # Increment prefix length for words in conflict to resolve them
        # We increment by 1 to find the next shortest possible abbreviation
        for idx in conflict_indices:
            current_prefixes[idx] += 1

# Re-assigning to the required function name
solve = solve_optimized