METADATA = {
    "id": 676,
    "name": "Implement Magic Dictionary",
    "slug": "implement-magic-dictionary",
    "category": "Design",
    "aliases": [],
    "tags": ["trie", "hash_map", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(N * L) for construction, O(L^2) for search",
    "space_complexity": "O(N * L)",
    "description": "Design a data structure that stores a dictionary of words and can determine if a given word can be transformed into a dictionary word by changing exactly one character.",
}

class MagicDictionary:
    def __init__(self, dictionary: list[str]):
        """
        Initializes the MagicDictionary with a list of words.
        
        Args:
            dictionary: A list of strings to be stored in the dictionary.
        """
        # We use a dictionary of sets where keys are word lengths.
        # This allows us to only compare the input word against words of the same length.
        self.words_by_length: dict[int, set[str]] = {}
        for word in dictionary:
            length = len(word)
            if length not in self.words_by_length:
                self.words_by_length[length] = set()
            self.words_by_length[length].add(word)

    def search(self, search_word: str) -> bool:
        """
        Returns True if search_word can be transformed into a dictionary word 
        by changing exactly one character.
        
        Args:
            search_word: The word to search for.
            
        Returns:
            True if a valid transformation exists, False otherwise.
            
        Examples:
            >>> md = MagicDictionary(["hello", "leetcode"])
            >>> md.search("hello")
            False
            >>> md.search("hallo")
            True
        """
        length = len(search_word)
        if length not in self.words_by_length:
            return False
        
        target_words = self.words_by_length[length]
        
        # Iterate through every character position in the search_word
        for i in range(length):
            original_char = search_word[i]
            # Try replacing the current character with every other lowercase letter
            for char_code in range(ord('a'), ord('z') + 1):
                new_char = chr(char_code)
                
                if new_char == original_char:
                    continue
                
                # Construct the modified word
                # Using slicing to create the new word string
                modified_word = search_word[:i] + new_char + search_word[i+1:]
                
                # If the modified word exists in our set, we found a valid transformation
                if modified_word in target_words:
                    return True
                    
        return False

def solve():
    """
    Entry point for testing the implementation.
    """
    # Example 1
    md1 = MagicDictionary(["hello", "leetcode"])
    assert md1.search("hello") == False
    assert md1.search("hallo") == True
    assert md1.search("hell") == False
    assert md1.search("leetcoded") == False
    
    # Example 2
    md2 = MagicDictionary(["leet", "code"])
    assert md2.search("leet") == False
    assert md2.search("lote") == True
    assert md2.search("code") == False
    assert md2.search("lode") == True
