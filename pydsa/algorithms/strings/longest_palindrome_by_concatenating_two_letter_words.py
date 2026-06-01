METADATA = {
    "id": 2131,
    "name": "Longest Palindrome by Concatenating Two Letter Words",
    "slug": "longest-palindrome-by-concatenating-two-letter-words",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest palindrome that can be formed by concatenating two-letter words from a given list.",
}

def solve(words: list[str]) -> int:
    """
    Calculates the length of the longest palindrome formed by concatenating two-letter words.

    The algorithm counts the occurrences of each word. Words that are palindromes 
    (e.g., 'aa') can be used in pairs or one can be placed in the center. 
    Words that are not palindromes (e.g., 'ab') must be paired with their 
    reverse ('ba') to contribute to the palindrome length.

    Args:
        words: A list of two-letter strings.

    Returns:
        The length of the longest possible palindrome.

    Examples:
        >>> solve(["lc", "cl", "gg"])
        6
        >>> solve(["ab", "ba", "aa", "ab", "ba"])
        6
        >>> solve(["aa", "bb", "cc", "dd"])
        2
    """
    word_counts: dict[str, int] = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    total_length = 0
    has_central_element = False

    # We iterate through the unique words found in the input
    for word, count in list(word_counts.items()):
        # Skip processed words to avoid double counting
        if count == 0:
            continue

        reverse_word = word[::-1]

        if word == reverse_word:
            # Case 1: The word is a palindrome (e.g., 'aa')
            # We can use pairs of these words (count // 2 * 2)
            # If there's an odd count, one can potentially be the center
            pairs = count // 2
            total_length += pairs * 4
            
            if count % 2 == 1:
                has_central_element = True
            
            # Mark as processed
            word_counts[word] = 0
        else:
            # Case 2: The word is not a palindrome (e.g., 'ab')
            # We need to find its reverse ('ba') to form a pair
            if reverse_word in word_counts:
                reverse_count = word_counts[reverse_word]
                # The number of pairs is the minimum of the two counts
                num_pairs = min(count, reverse_count)
                total_length += num_pairs * 4
                
                # Mark both words as processed
                word_counts[word] = 0
                word_counts[reverse_word] = 0

    # If we found any single palindrome word, we can put one in the middle
    if has_central_element:
        total_length += 2

    return total_length
