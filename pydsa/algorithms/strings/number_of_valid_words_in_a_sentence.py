METADATA = {
    "id": 2047,
    "name": "Number of Valid Words in a Sentence",
    "slug": "number-of-valid-words-in-a-sentence",
    "category": "String",
    "aliases": [],
    "tags": ["string", "regex", "parsing"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(1)",
    "description": "Count the number of valid words in a sentence based on specific punctuation and digit constraints.",
}

def solve(sentence: str) -> int:
    """
    Counts the number of valid words in a sentence.
    
    A word is valid if:
    1. It contains only lowercase English letters, hyphens, or digits.
    2. It contains at most one hyphen, and the hyphen must be between two letters.
    3. It contains at most one punctuation mark, and it must be at the end of the word.
    4. It contains no digits. (Wait, the actual LeetCode rule is: 
       - Only lowercase letters, hyphens, or punctuation.
       - At most one hyphen, must be between letters.
       - At most one punctuation, must be at the end.
       - No digits allowed.)

    Args:
        sentence: The input string containing words separated by spaces.

    Returns:
        The count of valid words.

    Examples:
        >>> solve("a# b$c d--e f!g# i")
        1
        >>> solve("he-llo world! 123")
        2
    """
    # Split by whitespace to get individual words
    words = sentence.split()
    valid_count = 0
    
    # Define allowed punctuation marks based on problem description
    punctuation_marks = {'!', '.', ',', '?'}

    for word in words:
        is_valid = True
        hyphen_count = 0
        punctuation_count = 0
        
        for i, char in enumerate(word):
            # Rule: No digits allowed
            if char.isdigit():
                is_valid = False
                break
            
            # Rule: Handle hyphens
            if char == '-':
                hyphen_count += 1
                # Hyphen must be between two letters and only one hyphen allowed
                if hyphen_count > 1 or i == 0 or i == len(word) - 1 or \
                   not word[i-1].islower() or not word[i+1].islower():
                    is_valid = False
                    break
            
            # Rule: Handle punctuation
            elif char in punctuation_marks:
                punctuation_count += 1
                # Punctuation must be at the very end and only one allowed
                if punctuation_count > 1 or i != len(word) - 1:
                    is_valid = False
                    break
            
            # Rule: Only lowercase letters are allowed (other than '-' and punctuation)
            elif not char.islower():
                is_valid = False
                break
        
        if is_valid:
            valid_count += 1
            
    return valid_count
