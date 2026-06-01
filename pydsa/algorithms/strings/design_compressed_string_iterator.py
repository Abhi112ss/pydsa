METADATA = {
    "id": 604,
    "name": "Design Compressed String Iterator",
    "slug": "design-compressed-string-iterator",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(1) per next() call amortized",
    "space_complexity": "O(1) excluding the input string storage",
    "description": "Implement an iterator that traverses a compressed string representation where characters are followed by their counts.",
}

class StringIterator:
    def __init__(self, compressedString: str):
        """
        Args:
            compressedString (str): The compressed string to iterate over.
        """
        self.compressed_string = compressedString
        self.index = 0
        self.current_char = ""
        self.remaining_count = 0
        self._advance()

    def _advance(self) -> None:
        """
        Internal method to move to the next valid character in the compressed sequence.
        """
        if self.remaining_count > 0:
            return

        while self.index < len(self.compressed_string):
            char = self.compressed_string[self.index]
            self.index += 1
            
            num_str = ""
            while self.index < len(self.compressed_string) and self.compressed_string[self.index].isdigit():
                num_str += self.compressed_string[self.index]
                self.index += 1
            
            self.current_char = char
            self.remaining_count = int(num_str)

        if self.index >= len(self.compressed_string) and self.remaining_count <= 0:
            self.current_char = ""
            self.remaining_count = 0

    def next(self) -> str:
        """
        Args:
            None
        Returns:
            str: The next character in the compressed string.
        """
        result = self.current_char
        self.remaining_count -= 1
        if self.remaining_count == 0:
            self._advance()
        return result

    def hasNext(self) -> bool:
        """
        Args:
            None
        Returns:
            bool: True if there are more characters to iterate, False otherwise.
        """
        return self.remaining_count > 0 or self.index < len(self.compressed_string) or (self.current_char != "" and self.remaining_count > 0)

def solve():
    pass