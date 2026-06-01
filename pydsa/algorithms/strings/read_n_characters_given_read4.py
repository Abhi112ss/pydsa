METADATA = {
    "id": 157,
    "name": "Read N Characters Given Read4",
    "slug": "read_n_characters_given_read4",
    "category": "Interactive",
    "aliases": [],
    "tags": ["string_manipulation", "interactive"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Implement a function to read exactly n characters from a stream using a provided read4 function.",
}

class Solution:
    def readNCharacters(self, n: int, read4: callable) -> str:
        """
        Reads exactly n characters from a stream using the read4 function.

        Args:
            n: The number of characters to read.
            read4: A function that reads up to 4 characters from the stream 
                   and returns the number of characters actually read.
                   The signature is read4() -> int. 
                   Note: In the LeetCode environment, read4 is provided as a 
                   method of an object, but for this implementation, we treat 
                   it as a callable.

        Returns:
            A string containing exactly n characters, or fewer if the 
            stream ends before n characters are reached.

        Examples:
            >>> # Mocking read4 behavior
            >>> def mock_read4():
            ...     return 4 # returns 4 chars
            >>> sol = Solution()
            >>> sol.readNCharacters(6, mock_read4)
            '123456'
        """
        result_chars = []
        chars_needed = n

        while chars_needed > 0:
            # Read up to 4 characters at a time
            # In the actual LeetCode interface, this is usually self.read4()
            # We assume read4 is a callable provided to the function
            buffer = self._get_buffer(read4)
            
            if not buffer:
                break
            
            # Determine how many characters to take from the current buffer
            # We take the minimum of what was read and what we still need
            num_to_take = min(len(buffer), chars_needed)
            result_chars.append(buffer[:num_to_take])
            
            # Update the remaining count
            chars_needed -= num_to_take
            
            # If the buffer returned fewer than 4 characters, we reached EOF
            if len(buffer) < 4:
                break

        return "".join(result_chars)

    def _get_buffer(self, read4: callable) -> str:
        """
        Helper to simulate the read4 behavior which returns an integer 
        representing the count, but we need the actual characters.
        
        Note: In the real LeetCode problem, read4 is a method of an 
        interface that populates a buffer. Since we are writing the 
        logic for the user-facing function, we assume the standard 
        interface where read4() returns the count and updates an internal state.
        
        However, to make this code runnable and logically sound for the 
        algorithm, we implement the logic assuming read4() returns 
        the characters read as a string or we handle the buffer.
        """
        # In LeetCode, the interface is: 
        # int read4(char buf[])
        # This implementation assumes a simplified version where read4 
        # returns the string of characters read.
        return read4()

# Note: The actual LeetCode implementation of read4 is slightly different 
# (it populates a char array). The logic above follows the algorithmic 
# requirement of consuming the stream in chunks of 4.

def solve():
    """
    Example usage for testing purposes.
    """
    class MockStream:
        def __init__(self, data: str):
            self.data = data
            self.ptr = 0
        
        def read4(self) -> str:
            # Simulating the behavior: returns up to 4 chars
            chunk = self.data[self.ptr : self.ptr + 4]
            self.ptr += len(chunk)
            return chunk

    stream = MockStream("abcdefghijklmn")
    sol = Solution()
    
    # Test 1: Read exactly n
    print(f"Test 1 (n=6): {sol.readNCharacters(6, stream.read4)}") 
    
    # Reset stream
    stream = MockStream("abcdefghijklmn")
    # Test 2: Read more than available
    print(f"Test 2 (n=20): {sol.readNCharacters(20, stream.read4)}")
    
    # Reset stream
    stream = MockStream("abcdefghijklmn")
    # Test 3: Read exactly the total length
    print(f"Test 3 (n=14): {sol.readNCharacters(14, stream.read4)}")
