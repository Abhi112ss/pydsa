METADATA = {
    "id": 1178,
    "name": "Number of Valid Words for Each Puzzle",
    "slug": "number-of-valid-words-for-each-puzzle",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["bitmask", "hash_map"],
    "difficulty": "hard",
    "time_complexity": "O(N + M * 2^K) where N is total chars in words, M is number of puzzles, and K is puzzle size (7)",
    "space_complexity": "O(N) to store word bitmasks",
    "description": "Count how many words can be formed using a subset of characters from each puzzle, given each puzzle must use exactly the specified number of unique characters.",
}

def solve(words: list[str], puzzles: list[list[str]]) -> list[int]:
    """
    Counts the number of valid words for each puzzle based on character bitmasks.

    A word is valid for a puzzle if:
    1. All characters in the word are present in the puzzle.
    2. The number of unique characters in the word is exactly equal to the puzzle size.

    Args:
        words: A list of strings representing the available words.
        puzzles: A list of lists of strings, where each inner list is a puzzle.

    Returns:
        A list of integers representing the count of valid words for each puzzle.

    Examples:
        >>> solve(["apple", "pear", "peach"], [["a", "p", "l", "e"], ["p", "e", "a", "r"]])
        [1, 1]
    """
    # Map to store the frequency of bitmasks representing words.
    # A bitmask represents the set of unique characters in a word.
    word_mask_counts: dict[int, int] = {}

    for word in words:
        mask = 0
        is_valid_word = True
        # We only care about words that could potentially fit in a puzzle of size 7.
        # However, the problem constraints imply we just need to check if the word
        # contains characters outside the alphabet or if it's too complex.
        # Actually, we just need to build the mask.
        for char in word:
            bit = 1 << (ord(char) - ord('a'))
            mask |= bit
        
        # Count how many bits are set in the mask.
        # If a word has more than 7 unique characters, it can never satisfy a puzzle.
        if bin(mask).count('1') <= 7:
            word_mask_counts[mask] = word_mask_counts.get(mask, 0) + 1

    results: list[int] = []

    for puzzle in puzzles:
        puzzle_mask = 0
        for char in puzzle:
            puzzle_mask |= 1 << (ord(char) - ord('a'))
        
        # The puzzle size is the number of unique characters provided.
        puzzle_size = len(puzzle)
        count = 0
        
        # We need to find all submasks of the puzzle_mask that have exactly puzzle_size bits.
        # However, the problem states the word must use EXACTLY the characters in the puzzle?
        # No, the word must use a SUBSET of the puzzle characters, and the word's 
        # unique character count must equal the puzzle's unique character count.
        # This means the word's mask must be a submask of the puzzle_mask AND 
        # have the same number of set bits as the puzzle.
        
        # Optimization: Iterate through all submasks of the puzzle_mask.
        # A submask 's' of 'm' can be iterated using: s = (s - 1) & m
        submask = puzzle_mask
        while submask > 0:
            # Check if the submask has the required number of unique characters.
            # Since the submask is derived from the puzzle_mask, it is guaranteed
            # to be a subset of the puzzle characters.
            if bin(submask).count('1') == puzzle_size:
                if submask in word_mask_counts:
                    count += word_mask_counts[submask]
            
            # Standard bit manipulation trick to iterate through all submasks.
            submask = (submask - 1) & puzzle_mask
            
        results.append(count)

    return results
