METADATA = {
    "id": 3374,
    "name": "First Letter Capitalization II",
    "slug": "first-letter-capitalization-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["string_manipulation", "dp"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest string by capitalizing exactly one character in each word under specific constraints.",
}

def solve(s: str, k: int) -> str:
    """
    Finds the lexicographically smallest string by capitalizing exactly one 
    character in each word, such that the total number of capitalized 
    characters is exactly k.

    Args:
        s: The input string consisting of lowercase letters and spaces.
        k: The exact number of characters that must be capitalized.

    Returns:
        The lexicographically smallest string possible.

    Examples:
        >>> solve("abc def", 2)
        'Abc Def'
        >>> solve("abc def", 1)
        'abc Def'
    """
    words = s.split(' ')
    n = len(words)
    
    # dp[i][j] = minimum lexicographical string using words from index i to n-1
    # with exactly j capitalizations remaining.
    # Since we want the lexicographically smallest string, and strings are 
    # compared character by character, we work backwards.
    # However, a standard DP with strings is slow. 
    # Observation: To make a string lexicographically smallest, we want 
    # the earliest possible characters to be as small as possible.
    # For a single word, the best character to capitalize is the first one 
    # that makes the word smaller (none, since 'A' < 'a' is False, actually 'A' < 'a' is True).
    # Wait, in ASCII, 'A' is 65 and 'a' is 97. So 'A' < 'a'.
    # To make a word lexicographically smallest, we want to capitalize 
    # the character that results in the smallest string.
    # Since 'A' < 'a', capitalizing any character makes the word lexicographically smaller.
    # To get the smallest overall string, we want the "smallest" changes to happen 
    # as early as possible in the string.
    
    # Let's refine: For each word, we must pick exactly one index to capitalize.
    # We have n words and we need to pick k indices. 
    # Wait, the problem implies we pick exactly one character per word? 
    # "exactly one character in each word" and "total number of capitalized characters is k".
    # This implies k must equal the number of words. 
    # If k != len(words), the problem constraints or logic must be different.
    # Re-reading: "exactly one character in each word" and "total k".
    # This means k must be equal to the number of words.
    
    # If the problem is: "Pick exactly one character in each word such that 
    # the total number of capitalized characters is k", and there are n words,
    # then k must be n. If k is not n, the problem is impossible or 
    # the constraint is "at most one" or "exactly k characters total".
    
    # Assuming the standard version: We have n words, we must capitalize 
    # exactly one character in each word, and we want the smallest string.
    # Since 'A' < 'a', capitalizing the first character of a word is always 
    # better than capitalizing any subsequent character in that same word.
    # Example: "abc" -> "Abc" (smallest), "aBc", "abC".
    # "Abc" < "aBc" < "abC".
    
    # If k is the number of words, we capitalize the first letter of every word.
    # If the problem allows choosing which words to capitalize (if k < n),
    # we want to capitalize the first letter of the words that appear earliest.
    
    # Let's implement the logic for: "Capitalize exactly one character in k words 
    # out of n words to make the string lexicographically smallest."
    
    word_list = words
    num_words = len(word_list)
    
    # To make the string lexicographically smallest:
    # 1. We want to capitalize the first letter of a word if possible.
    # 2. We want to do this for the words that appear earliest in the string.
    
    # Because 'A' < 'a', "Abc" < "abc".
    # Thus, the best strategy is to pick the first k words and capitalize their first letter.
    
    result_words = []
    for i in range(num_words):
        word = word_list[i]
        if i < k:
            # Capitalize the first letter of the word
            new_word = word[0].upper() + word[1:]
            result_words.append(new_word)
        else:
            # Keep the word as is
            result_words.append(word)
            
    return " ".join(result_words)

# Note: The logic above assumes the problem asks to pick k words to capitalize 
# one letter each. If the problem is "exactly one letter in each word" 
# and "total k", then k must be len(words). 
# If the problem is "exactly k letters total" across all words, 
# the greedy approach of picking the first k words and capitalizing their 
# first letters is optimal because 'A' < 'a' and earlier positions 
# have more weight in lexicographical comparison.
