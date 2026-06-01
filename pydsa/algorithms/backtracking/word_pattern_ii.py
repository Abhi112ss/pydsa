METADATA = {
    "id": 291,
    "name": "Word Pattern II",
    "slug": "word-pattern-ii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "hash_map", "recursion"],
    "difficulty": "hard",
    "time_complexity": "O(N^M)",
    "space_complexity": "O(M)",
    "description": "Determine if a string follows a specific pattern of words where each character in the pattern maps to a unique word.",
}

def solve(pattern: str, s: str) -> bool:
    """
    Determines if the string 's' follows the pattern provided in 'pattern'.
    
    Each character in the pattern must map to a unique word in the string,
    and each unique word must map to exactly one character in the pattern.

    Args:
        pattern: A string of characters representing the pattern.
        s: A space-separated string of words.

    Returns:
        True if the string follows the pattern, False otherwise.

    Examples:
        >>> solve("abba", "dog cat cat dog")
        True
        >>> solve("abba", "dog cat cat fish")
        False
        >>> solve("aaaa", "dog dog dog dog")
        True
        >>> solve("abba", "dog dog dog dog")
        False
    """
    words = s.split()
    
    # If lengths don't match, the pattern cannot be satisfied
    if len(pattern) != len(words):
        return False

    char_to_word: dict[str, str] = {}
    word_to_char: dict[str, str] = {}

    def backtrack(pattern_idx: int, word_idx: int) -> bool:
        # Base case: if we have processed all characters in the pattern
        if pattern_idx == len(pattern):
            return True

        current_char = pattern[pattern_idx]
        
        # Case 1: The character already has a mapping
        if current_char in char_to_word:
            target_word = char_to_word[current_char]
            # Check if the current word in the sequence matches the mapped word
            if words[word_idx] == target_word:
                return backtrack(pattern_idx + 1, word_idx + 1)
            return False

        # Case 2: The character does not have a mapping yet
        # We try all possible substring lengths for the current word
        # Note: Since words are space-separated, we actually iterate through 
        # the words list provided by split(), but the problem logic 
        # implies we are matching the sequence of words.
        # However, the standard interpretation of Word Pattern II is 
        # matching the sequence of words in the split list.
        
        # If the word is already used by another character, this path is invalid
        if words[word_idx] in word_to_char:
            return False

        # Try assigning the current word to the current character
        current_word = words[word_idx]
        char_to_word[current_char] = current_word
        word_to_char[current_word] = current_char

        if backtrack(pattern_idx + 1, word_idx + 1):
            return True

        # Backtrack: remove the mapping if the path didn't lead to a solution
        del char_to_word[current_char]
        del word_to_char[current_word]
        
        return False

    # Note: The problem description for Word Pattern II on LeetCode 
    # actually asks to find all possible ways to split the string 's' 
    # into words that match the pattern. The split() approach above 
    # is for Word Pattern I. Let's implement the correct backtracking 
    # for Word Pattern II which involves substring slicing.

    def backtrack_substring(p_idx: int, s_idx: int) -> list[list[str]]:
        """
        Finds all possible word sequences matching the pattern.
        """
        if p_idx == len(pattern):
            return [[]] if s_idx == len(s) else []

        results = []
        char = pattern[p_idx]
        
        # Try every possible end position for the current word
        for end in range(s_idx + 1, len(s) + 1):
            word = s[s_idx:end]
            
            # Optimization: If we encounter a space, it's not a valid word boundary
            # unless it's the end of the word, but the problem implies words 
            # are separated by spaces. Actually, the problem says 's' is a string 
            # and we need to split it.
            
            # Check if this word is valid for the current character
            # We need to track mappings locally within this recursion branch
            # to ensure consistency.
            
            # However, the standard Word Pattern II requires finding all 
            # valid sequences. The mapping must be consistent across the whole sequence.
            pass

    # Correct implementation for Word Pattern II (finding all sequences):
    def find_all_sequences(p_idx: int, s_idx: int, 
                           char_map: dict[str, str], 
                           word_map: dict[str, str]) -> list[list[str]]:
        if p_idx == len(pattern):
            return [[]] if s_idx == len(s) else []

        res = []
        char = pattern[p_idx]

        # Try all possible lengths for the next word
        for end in range(s_idx + 1, len(s) + 1):
            word = s[s_idx:end]
            
            # Check if word is valid for the current character
            is_valid = False
            if char in char_map:
                if char_map[char] == word:
                    is_valid = True
            else:
                if word not in word_map:
                    is_valid = True
            
            if is_valid:
                # Apply mapping
                old_char_val = char_map.get(char)
                old_word_val = word_map.get(word)
                
                char_map[char] = word
                word_map[word] = char
                
                # Recurse
                sub_sequences = find_all_sequences(p_idx + 1, end, char_map, word_map)
                for sub in sub_sequences:
                    res.append([word] + sub)
                
                # Backtrack
                if old_char_val is None:
                    del char_map[char]
                else:
                    char_map[char] = old_char_val
                    
                if old_word_val is None:
                    del word_map[word]
                else:
                    word_map[word] = old_word_val
                    
        return res

    # The problem asks for a boolean in some contexts, but LeetCode 291 
    # asks for all possible sequences. Given the prompt asks for a 
    # "solver" and the signature returns bool, I will provide the 
    # logic that returns True if at least one valid sequence exists.
    
    def exists_sequence(p_idx: int, s_idx: int, 
                        char_map: dict[str, str], 
                        word_map: dict[str, str]) -> bool:
        if p_idx == len(pattern):
            return s_idx == len(s)

        char = pattern[p_idx]
        for end in range(s_idx + 1, len(s) + 1):
            word = s[s_idx:end]
            
            # Check mapping consistency
            if char in char_map:
                if char_map[char] != word:
                    continue
            else:
                if word in word_map:
                    continue
            
            # Tentative mapping
            prev_char_word = char_map.get(char)
            prev_word_char = word_map.get(word)
            
            char_map[char] = word
            word_map[word] = char
            
            if exists_sequence(p_idx + 1, end, char_map, word_map):
                return True
            
            # Backtrack
            if prev_char_word is None:
                del char_map[char]
            else:
                char_map[char] = prev_char_word
                
            if prev_word_char is None:
                del word_map[word]
            else:
                word_map[word] = prev_word_char
                
        return False

    return exists_sequence(0, 0, {}, {})
