METADATA = {
    "id": 158,
    "name": "Read N Characters Given read4 II - Call Multiple Times",
    "slug": "read-n-characters-given-read4-ii-call-multiple-times",
    "category": "Design",
    "aliases": [],
    "tags": ["interactive", "string_manipulation", "design"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Implement a function to read n characters from a stream using a limited read4 function, handling leftover characters from previous calls.",
}

class Solution:
    def __init__(self, reader: "Reader"):
        """
        Initializes the solution object.

        Args:
            reader: An instance of the Reader class provided by the problem.
        """
        self.reader = reader
        self.buffer = []
        self.buffer_ptr = 0

    def readN(self, n: int) -> str:
        """
        Reads n characters from the reader.

        Args:
            n: The number of characters to read.

        Returns:
            A string containing the n characters read.

        Examples:
            >>> reader = Reader("abcdefgh")
            >>> sol = Solution(reader)
            >>> sol.readN(2)
            'ab'
            >>> sol.readN(3)
            'cde'
            >>> sol.readN(10)
            'fgh'
        """
        result = []
        chars_needed = n

        while chars_needed > 0:
            # If the internal buffer is exhausted, fetch more from the reader
            if self.buffer_ptr >= len(self.buffer):
                new_chars = []
                # The read4 function returns the number of characters actually read
                count = self.reader.read4(new_chars)
                
                if count == 0:
                    # End of stream reached
                    break
                
                self.buffer = new_chars[:count]
                self.buffer_ptr = 0

            # Calculate how many characters we can take from the current buffer
            # without exceeding the requested 'n' or the buffer's current size
            can_take = min(chars_needed, len(self.buffer) - self.buffer_ptr)
            
            # Append the slice of the buffer to our result list
            result.extend(self.buffer[self.buffer_ptr : self.buffer_ptr + can_take])
            
            # Advance the buffer pointer and decrement the remaining count
            self.buffer_ptr += can_take
            chars_needed -= can_take

        return "".join(result)

class Reader:
    """
    Mock Reader class for testing purposes.
    """
    def __init__(self, stream: str):
        self.stream = stream
        self.ptr = 0

    def read4(self, buf: list[str]) -> int:
        """
        Reads up to 4 characters from the stream into the buffer.
        """
        count = 0
        while count < 4 and self.ptr < len(self.stream):
            buf.append(self.stream[self.ptr])
            self.ptr += 1
            count += 1
        return count

def solve():
    """
    Entry point to demonstrate the solution.
    """
    stream = "abcdefgh"
    reader = Reader(stream)
    sol = Solution(reader)
    
    print(f"Read 2: {sol.readN(2)}")   # Expected: 'ab'
    print(f"Read 3: {sol.readN(3)}")   # Expected: 'cde'
    print(f"Read 10: {sol.readN(10)}") # Expected: 'fgh'
