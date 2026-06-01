METADATA = {
    "id": 187,
    "name": "Repeated DNA Sequences",
    "slug": "repeated-dna-sequences",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "bit_manipulation", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all 10-letter-long sequences (substrings) that occur more than once in a DNA strand.",
}

def solve(s: str) -> list[str]:
    """
    Args:
        s: A string representing the DNA sequence.

    Returns:
        A list of all 10-letter-long sequences that occur more than once.
    """
    seen_sequences: set[str] = set()
    repeated_sequences: set[str] = set()
    sequence_length = 10
    
    for index in range(len(s) - sequence_length + 1):
        current_substring = s[index : index + sequence_length]
        if current_substring in seen_sequences:
            repeated_sequences.add(current_substring)
        else:
            seen_sequences.add(current_substring)
            
    return list(repeated_sequences)