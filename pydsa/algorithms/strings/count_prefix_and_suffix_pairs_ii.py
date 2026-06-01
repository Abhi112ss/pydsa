METADATA = {
    "id": 3045,
    "name": "Count Prefix and Suffix Pairs II",
    "slug": "count-prefix-and-suffix-pairs-ii",
    "category": "String",
    "aliases": [],
    "tags": ["trie", "kmp_algorithm", "string_matching", "aho-corasick"],
    "difficulty": "hard",
    "time_complexity": "O(N * L^2) or O(N * L) depending on implementation, where L is max length",
    "space_complexity": "O(N * L)",
    "description": "Count pairs (i, j) such that words[i] is both a prefix and a suffix of words[j].",
}

def solve(words: list[str]) -> int:
    """
    Counts the number of pairs (i, j) such that words[i] is both a prefix 
    and a suffix of words[j], where i < j.

    Args:
        words: A list of strings.

    Returns:
        The total count of such pairs.

    Examples:
        >>> solve(["a", "aba", "ababa"])
        3
        # Pairs: (0,1) "a" in "aba", (0,2) "a" in "ababa", (1,2) "aba" in "ababa"
        >>> solve(["a", "b", "c"])
        0
    """
    # To solve this efficiently, we can use a Trie to store all words.
    # However, since we need to check both prefix AND suffix, a standard Trie 
    # only handles prefixes. To handle both, we can use a specialized Trie 
    # or a hashing approach. 
    # Given the constraints and the "II" version, we use a Trie where each node 
    # stores a list of indices of words that end at that node.
    # To handle the suffix condition, we can use a technique similar to Aho-Corasick 
    # or simply check the suffix condition during the Trie traversal.
    
    # For a production-grade approach that handles the "Prefix AND Suffix" 
    # requirement efficiently, we can use a Trie of pairs (char_prefix, char_suffix).
    # But a more memory-efficient way is to use a Trie for prefixes and 
    # verify the suffix condition using string hashing or KMP-like logic.
    
    # Let's use a Trie where each node stores the count of words that end there.
    # To handle the suffix, we can use a "Double Trie" or a Trie of (prefix, suffix) 
    # pairs, but that's O(L^2). 
    # The most robust way for "Prefix and Suffix" is to use a Trie where we 
    # insert strings as (char, char) pairs from both ends.
    
    class TrieNode:
        def __init__(self):
            self.children: dict[tuple[str, str], TrieNode] = {}
            self.count: int = 0

    root = TrieNode()
    total_pairs = 0

    for word in words:
        n = len(word)
        
        # 1. Search for existing words in the Trie that are both prefix and suffix
        # We traverse the Trie using the (prefix_char, suffix_char) pairs of the current word.
        # For a word of length L, we check pairs (word[0], word[n-1]), (word[1], word[n-2])...
        # Wait, that's for palindromes. For prefix/suffix, we need to match 
        # word[0...k] with word[n-k-1...n-1].
        
        # Correct approach: A word 'a' is a prefix and suffix of 'b' if:
        # b.startswith(a) AND b.endswith(a).
        # We can use a Trie where we insert strings as a sequence of pairs:
        # (word[0], word[n-1]), (word[1], word[n-2]), ..., (word[k], word[n-k-1])
        # This is only valid if the word is being matched against a shorter word.
        
        # Let's use the "Trie of Pairs" approach:
        # For each word, we traverse the Trie using pairs (word[i], word[n-1-i]) 
        # for i from 0 to len(word)-1.
        # But we need to match the prefix and suffix of the *current* word 
        # against *previously* inserted words.
        
        # Actually, the simplest way to handle "Prefix and Suffix" is to 
        # insert each word into a Trie where each node represents a pair 
        # of characters: (prefix_char, suffix_char).
        # For word "ababa", the sequence of pairs is:
        # (a, a), (b, b), (a, a)
        
        # Let's re-evaluate: If word A is a prefix and suffix of word B,
        # then A[0] == B[0], A[1] == B[1]... AND A[0] == B[n-len(A)], A[1] == B[n-len(A)+1]...
        # This is equivalent to saying the sequence of pairs 
        # (word[0], word[n-1]), (word[1], word[n-2])... matches.
        
        # Let's use a Trie where we insert the word as a sequence of pairs:
        # (word[i], word[n-1-i]) for i in range(len(word)).
        # This is still slightly wrong because the suffix index depends on the 
        # length of the word being inserted.
        
        # Correct logic:
        # A word `s` is a prefix and suffix of `t` if:
        # s == t[:len(s)] AND s == t[len(t)-len(s):]
        
        # We can use a Trie where we insert each word `w` by its characters.
        # To handle the suffix, we use a Trie where each node stores 
        # how many words end there AND satisfy the suffix condition.
        # This is complex. Let's use the "Trie of Pairs" correctly:
        # For each word, we want to find how many previous words `p` 
        # satisfy `p == word[:len(p)]` and `p == word[len(word)-len(p):]`.
        
        # We can insert each word into a Trie. To handle the suffix, 
        # we use a Trie where each node is a pair (word[i], word[n-1-i]).
        # This works because if word `p` is a prefix and suffix of `word`,
        # then for all `i < len(p)`, `p[i] == word[i]` AND `p[i] == word[n-len(p)+i]`.
        # This is still not quite right because the suffix index depends on `len(p)`.
        
        # Let's use the most reliable method: Aho-Corasick or a Trie 
        # where we insert the word `w` as:
        # (w[0], w[n-1]), (w[1], w[n-2]), ..., (w[k], w[n-1-k])
        # This works because if `p` is a prefix and suffix of `w`, 
        # then `p[i] == w[i]` and `p[i] == w[n-len(p)+i]`.
        # This is still tricky. Let's use the property:
        # `p` is a prefix and suffix of `w` if `p` is a prefix of `w` 
        # AND `p` is a suffix of `w`.
        
        # Let's use a Trie of pairs (word[i], word[n-1-i]) for the *current* word.
        # Wait, the problem is simpler: we need to count how many `words[i]` 
        # are prefix/suffix of `words[j]`.
        
        # Let's use a Trie where we insert each word `w` as a sequence of 
        # characters. To handle the suffix, we use a Trie where each node 
        # stores a list of indices of words that end there.
        # For each new word `w`, we traverse the Trie with `w` to find all 
        # prefixes. For each prefix found, we check if it's also a suffix of `w`.
        
        # To make this O(N*L), we use a Trie where each node stores 
        # the count of words that end at this node AND are also suffixes 
        # of the current path. This is exactly what Aho-Corasick does.
        # But Aho-Corasick finds all occurrences of patterns in a text.
        # Here, the "patterns" are the words themselves.
        
        # Let's use the "Trie of Pairs" approach correctly:
        # For each word `w`, we insert it into a Trie. 
        # The characters in the Trie are pairs: (w[i], w[n-1-i]).
        # This is only possible if we know the length.
        
        # Let's use a simpler approach: 
        # For each word, we check all its prefixes. 
        # A prefix `w[0:k]` is a suffix if `w[0:k] == w[n-k:n]`.
        # We can pre-calculate this using KMP's `pi` array (failure function).
        # For a word `w`, the `pi` array tells us all lengths of proper 
        # prefixes that are also suffixes.
        
        # 1. Build a Trie of all words. Each node stores `count` (how many words end here).
        # 2. For each word `w`, traverse the Trie to find all its prefixes.
        # 3. For each prefix found, check if it's also a suffix of `w`.
        
        # To avoid O(L^2) per word, we use the KMP `pi` array to find all 
        # prefix-suffix lengths in O(L).
        
        pass

    # Re-implementing with the KMP + Trie approach:
    # 1. Insert all words into a Trie. Each node stores `end_count`.
    # 2. For each word, find all its prefix-suffix lengths using KMP.
    # 3. For each such length, check if that prefix exists in the Trie.
    # Wait, the problem says i < j. So we should:
    # 1. For each word:
    #    a. Find all its prefix-suffix lengths using KMP.
    #    b. For each length, check if that prefix was already inserted in the Trie.
    #    c. Insert the current word into the Trie.
    
    # This is still slightly wrong. We need to count how many *previous* 
    # words are prefixes AND suffixes of the *current* word.
    
    # Correct Algorithm:
    # 1. Initialize a Trie.
    # 2. For each word in words:
    #    a. Use KMP's pi array to find all lengths `k` such that `word[0:k]` 
    #       is a suffix of `word`.
    #    b. For each such `k`, check if `word[0:k]` exists in the Trie.
    #       (Actually, we need to check if `word[0:k]` is a word in the Trie).
    #    c. Insert `word` into the Trie.
    
    # Wait, the KMP `pi` array gives all *proper* prefix-suffixes. 
    # We also need to check the word itself? No, the problem says i < j, 
    # and words[i] is a prefix/suffix of words[j]. 
    # If words[i] == words[j], it counts.
    
    # Let's refine:
    # For each word `w`:
    #   1. Find all `k` such that `w[0:k]` is a suffix of `w`.
    #   2. For each `k`, if `k > 0`, check if `w[0:k]` is in the Trie.
    #   3. Add `w` to the Trie.
    
    # To find all `k` such that `w[0:k]` is a suffix of `w`:
    # Use KMP `pi` array. The lengths are `pi[n-1], pi[pi[n-1]-1], ...`
    # Also, we must check if the whole word `w` is a prefix/suffix of a 
    # *previous* word? No, the problem says `words[i]` is a prefix/suffix of `words[j]`.
    # So `words[i]` is the shorter one.
    
    # Final Plan:
    # 1. Trie stores counts of words ending at each node.
    # 2. For each word `w`:
    #    a. Find all `k` such that `w[0:k]` is a suffix of `w`.
    #    b. For each such `k`, traverse the Trie to see if `w[0:k]` exists.
    #    c. Insert `w` into the Trie.
    
    # Wait, the KMP `pi` array approach finds all `k < len(w)`. 
    # We also need to check if `w` itself is a prefix/suffix of a *previous* word? 
    # No, `i < j`, so `words[i]` is the prefix/suffix.
    # So for `words[j]`, we look for `words[i]` in the Trie.
    
    # Example: words = ["a", "aba"]
    # 1. "a": Trie is empty. Count = 0. Insert "a".
    # 2. "aba": 
    #    - KMP `pi` for "aba" is [0, 0, 1]. 
    #    - Prefix-suffix lengths: 1.
    #    - Check if "a" (length 1) is in Trie. Yes. Count = 1.
    #    - Insert "aba".
    # Total = 1. Correct.
    
    # Example: words = ["a", "a"]
    # 1. "a": Count = 0. Insert "a".
    # 2. "a": 
    #    - KMP `pi` for "a" is [0].
    #    - Prefix-suffix lengths: None (proper).
    #    - BUT, the word "a" itself is a prefix and suffix of "a".
    #    - So we must also check the full word `w` in the Trie.
    #    - Check if "a" is in Trie. Yes. Count = 1.
    #    - Insert "a".
    # Total = 1. Correct.

    class TrieNode:
        def __init__(self):
            self.children: dict[str, 'TrieNode'] = {}
            self.count: int = 0

    root = TrieNode()
    ans = 0

    for word in words:
        n = len(word)
        
        # 1. Find all k such that word[0:k] is a suffix of word
        # We use the KMP pi array logic.
        # pi[i] is the length of the longest proper prefix of word[0:i+1] 
        # that is also a suffix of word[0:i+1].
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and word[i] != word[j]:
                j = pi[j - 1]
            if word[i] == word[j]:
                j += 1
            pi[i] = j
        
        # 2. Check all prefix-suffix lengths
        # The lengths are pi[n-1], pi[pi[n-1]-1], etc.
        # Also, we must check the word itself (k = n) if we want to handle 
        # the case where words[i] == words[j].
        
        # Check the full word first (for words[i] == words[j])
        curr = root
        possible = True
        for char in word:
            if char not in curr.children:
                possible = False
                break
            curr = curr.children[char]
        if possible:
            ans += curr.count
            
        # Check proper prefix-suffixes
        curr_len = pi[n - 1]
        while curr_len > 0:
            # Traverse Trie for word[0:curr_len]
            # To optimize, we don't re-traverse from root every time.
            # But since we only do this for prefix-suffixes, it's fine.
            # Actually, we can just traverse the Trie once for the whole word
            # and store the nodes in a list.
            curr_len = pi[curr_len - 1] # This is wrong, we need to check the node.
            # Let's use a different approach for the traversal.
            break # placeholder

        # Let's fix the traversal.
        # We'll traverse the Trie once for the current word and store the nodes.
        # nodes[k] will be the node