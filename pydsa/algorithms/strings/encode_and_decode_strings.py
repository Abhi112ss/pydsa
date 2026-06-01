METADATA = {
    "id": 271,
    "name": "Encode and Decode Strings",
    "slug": "encode-and-decode-strings",
    "category": "Design",
    "aliases": [],
    "tags": ["string", "design"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Design an algorithm to encode a list of strings to a single string and decode it back to the original list.",
}

class Codec:
    """
    A class to encode and decode a list of strings into a single string and back.
    """

    def encode(self, strs: list[str]) -> str:
        """
        Encodes a list of strings to a single string.

        The encoding scheme uses the format: <length> + <delimiter> + <string>.
        This ensures that even if the string contains the delimiter, we know 
        exactly how many characters to read based on the preceding length.

        Args:
            strs: A list of strings to encode.

        Returns:
            A single string representing the encoded list.

        Examples:
            >>> codec = Codec()
            >>> codec.encode(["hello", "world"])
            '5#hello5#world'
            >>> codec.encode(["", ""])
            '0#0#'
        """
        encoded_list = []
        for s in strs:
            # Prepend length and a delimiter to handle any character in the string
            encoded_list.append(f"{len(s)}#{s}")
        
        return "".join(encoded_list)

    def decode(self, s: str) -> list[str]:
        """
        Decodes a single string back into a list of strings.

        Args:
            s: The encoded string.

        Returns:
            The original list of strings.

        Examples:
            >>> codec = Codec()
            >>> codec.decode("5#hello5#world")
            ["hello", "world"]
            >>> codec.decode("0#0#")
            ["", ""]
        """
        decoded_list = []
        i = 0
        
        while i < len(s):
            # Find the delimiter to determine where the length prefix ends
            delimiter_index = s.find("#", i)
            
            # Extract the length of the next string
            length = int(s[i:delimiter_index])
            
            # Move the pointer to the start of the actual string content
            start_of_string = delimiter_index + 1
            end_of_string = start_of_string + length
            
            # Extract the string using the calculated length
            decoded_list.append(s[start_of_string:end_of_string])
            
            # Move the pointer to the start of the next encoded segment
            i = end_of_string
            
        return decoded_list

def solve():
    """
    Test function to verify the Codec implementation.
    """
    codec = Codec()
    test_cases = [
        ["hello", "world"],
        ["", ""],
        ["", "abc", ""],
        ["#", "##", "###"],
        ["123#abc", "456"],
        ["a", "b", "c", "d"]
    ]

    for case in test_cases:
        encoded = codec.encode(case)
        decoded = codec.decode(encoded)
        assert case == decoded, f"Failed! Input: {case}, Encoded: {encoded}, Decoded: {decoded}"
    
    print("All test cases passed!")
