METADATA = {
    "id": 443,
    "name": "String Compression",
    "slug": "string-compression",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Compress an array of characters in-place using a two-pointer approach.",
}

def solve(chars: list[str]) -> int:
    """
    Compresses the input list of characters in-place and returns the new length.

    The compression follows the rule: if a character repeats, replace it with 
    the character followed by the count of its repetitions. If the count is 1, 
    only the character is written.

    Args:
        chars: A list of characters to be compressed in-place.

    Returns:
        The new length of the compressed character array.

    Examples:
        >>> chars1 = ["a", "a", "b", "b", "c", "c", "c"]
        >>> solve(chars1)
        6
        >>> chars1[:6]
        ['a', '2', 'b', '2', 'c', '3']

        >>> chars2 = ["a"]
        >>> solve(chars2)
        1
        >>> chars2[:1]
        ['a']
    """
    write_index = 0
    read_index = 0
    total_length = len(chars)

    while read_index < total_length:
        char_to_compress = chars[read_index]
        count = 0
        
        # Count occurrences of the current character
        while read_index < total_length and chars[read_index] == char_to_compress:
            read_index += 1
            count += 1
        
        # Write the character to the write_index position
        chars[write_index] = char_to_compress
        write_index += 1
        
        # If count > 1, convert count to string and write each digit
        if count > 1:
            for digit in str(count):
                chars[write_index] = digit
                write_index += 1
                
    return write_index
