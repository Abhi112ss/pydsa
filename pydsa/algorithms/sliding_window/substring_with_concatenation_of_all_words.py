METADATA = {
    "id": 30,
    "name": "Substring with Concatenation of All Words",
    "slug": "substring-with-concatenation-of-all-words",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "sliding_window", "strings"],
    "difficulty": "hard",
    "time_complexity": "O(n * word_len)",
    "space_complexity": "O(m)",
    "description": "Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once.",
}

def solve(s: str, words: list[str]) -> list[int]:
    """
    Finds all starting indices of substrings in s that are a concatenation of all words.

    Args:
        s: The input string to search within.
        words: A list of strings where each string has the same length.

    Returns:
        A list of starting indices where the concatenation begins.

    Examples:
        >>> solve("barfoothefoobarman", ["foo", "bar"])
        [0, 9]
        >>> solve("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])
        []
    """
    if not s or not words:
        return []

    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = {}

    # Build the frequency map for the target words
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    result_indices = []

    # We run the sliding window 'word_len' times to cover all possible offsets
    # This ensures we check every possible alignment of words
    for offset in range(word_len):
        left = offset
        current_window_freq = {}
        words_found = 0

        # Slide the window by word_len increments
        for right in range(offset, len(s) - word_len + 1, word_len):
            word = s[right : right + word_len]

            if word in word_freq:
                current_window_freq[word] = current_window_freq.get(word, 0) + 1
                words_found += 1

                # If we have more instances of 'word' than required, shrink from the left
                while current_window_freq[word] > word_freq[word]:
                    left_word = s[left : left + word_len]
                    current_window_freq[left_word] -= 1
                    words_found -= 1
                    left += word_len

                # If the number of words matches the target, we found a valid substring
                if words_found == word_count:
                    result_indices.append(left)
            else:
                # Word not in target list: reset the window
                current_window_freq.clear()
                words_found = 0
                left = right + word_len

    return sorted(result_indices)
