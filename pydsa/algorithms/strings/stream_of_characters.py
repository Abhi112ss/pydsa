METADATA = {
    "id": 1032,
    "name": "Stream of Characters",
    "slug": "stream_of_characters",
    "category": "Design",
    "aliases": [],
    "tags": ["trie", "design", "string"],
    "difficulty": "medium",
    "time_complexity": "O(m) per addStream, where m is the length of the stream",
    "space_complexity": "O(total_chars_in_dictionary)",
    "description": "Design a data structure that receives a stream of characters and returns true if any suffix of the stream is a word in the dictionary.",
}

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False

class StreamOfCharacters:
    """
    A data structure that detects if any suffix of a character stream 
    matches a word in a predefined dictionary.
    """

    def __init__(self, words: list[str]) -> None:
        """
        Initializes the stream object with a dictionary of words.
        The words are stored in reverse in a Trie to allow efficient 
        suffix matching by traversing backwards from the current stream position.

        Args:
            words: A list of strings representing the dictionary.
        """
        self.root = TrieNode()
        self.stream: list[str] = []
        
        # Build the Trie with reversed words
        for word in words:
            current_node = self.root
            # Reversing the word allows us to match suffixes by 
            # traversing the Trie starting from the most recent character
            for char in reversed(word):
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]
            current_node.is_end_of_word = True

    def addStream(self, chars: str) -> bool:
        """
        Adds characters to the stream and checks if any suffix is a word.

        Args:
            chars: A string of characters to append to the stream.

        Returns:
            True if any suffix of the stream is a word in the dictionary, False otherwise.

        Examples:
            >>> stream = StreamOfCharacters(["leet", "code"])
            >>> stream.addStream("l")
            False
            >>> stream.addStream("e")
            False
            >>> stream.addStream("e")
            False
            >>> stream.addStream("t")
            True
        """
        # Append new characters to the existing stream
        for char in chars:
            self.stream.append(char)
        
        # We only need to check suffixes. A suffix match in the stream 
        # corresponds to a prefix match in our reversed Trie.
        # We traverse the stream backwards starting from the end.
        current_node = self.root
        for i in range(len(self.stream) - 1, -1, -1):
            char = self.stream[i]
            if char not in current_node.children:
                # If the character is not in the Trie, no suffix can match
                return False
            
            current_node = current_node.children[char]
            # If we reach a node marked as end of word, a suffix match is found
            if current_node.is_end_of_word:
                return True
                
        return False

def solve() -> None:
    """
    Example usage of the StreamOfCharacters class.
    """
    stream = StreamOfCharacters(["leet", "code"])
    print(stream.addStream("l"))    # False
    print(stream.addStream("e"))    # False
    print(stream.addStream("e"))    # False
    print(stream.addStream("t"))    # True
    print(stream.addStream("c"))    # False
    print(stream.addStream("o"))    # False
    print(stream.addStream("d"))    # False
    print(stream.addStream("e"))    # True
