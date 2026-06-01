METADATA = {
    "id": 411,
    "name": "Minimum Unique Word Abbreviation",
    "slug": "minimum-unique-word-abbreviation",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "backtracking", "trie"],
    "difficulty": "hard",
    "time_complexity": "O(2^n * m)",
    "space_complexity": "O(n * m)",
    "description": "Find the minimum length of an abbreviation that uniquely identifies each word in a given list.",
}

def solve(words: list[str]) -> int:
    """
    Args:
        words: A list of strings to be abbreviated.

    Returns:
        The minimum length of an abbreviation that uniquely identifies each word.
    """
    n = len(words)
    if n <= 1:
        return 0

    word_lengths = [len(word) for word in words]
    
    def get_abbreviation_mask(word_index: int, mask: int) -> str:
        result = []
        current_word = words[word_index]
        length = len(current_word)
        
        for i in range(length):
            if (mask >> i) & 1:
                result.append(current_word[i])
            else:
                count = 0
                while i < length and not ((mask >> i) & 1):
                    count += 1
                    i += 1
                result.append(str(count))
                # This logic is simplified for the sake of the bitmask approach
                # In a real bitmask approach, we iterate through bits
        return "".join(result)

    def is_valid(mask_list: list[int]) -> bool:
        seen_abbreviations = set()
        for i in range(n):
            current_mask = mask_list[i]
            current_word = words[i]
            length = len(current_word)
            
            abbr_parts = []
            idx = 0
            while idx < length:
                if (current_mask >> idx) & 1:
                    abbr_parts.append(current_word[idx])
                    idx += 1
                else:
                    skip_count = 0
                    while idx < length and not ((current_mask >> idx) & 1):
                        skip_count += 1
                        idx += 1
                    abbr_parts.append(str(skip_count))
            
            abbr = "".join(abbr_parts)
            if abbr in seen_abbreviations:
                return False
            seen_abbreviations.add(abbr)
        return True

    def get_abbr_len(mask: int, word_len: int) -> int:
        length = 0
        idx = 0
        while idx < word_len:
            if (mask >> idx) & 1:
                length += 1
                idx += 1
            else:
                skip_count = 0
                while idx < word_len and not ((mask >> idx) & 1):
                    skip_count += 1
                    idx += 1
                length += 1
                if skip_count > 0:
                    length += len(str(skip_count))
        return length

    def check_length(target_len: int) -> bool:
        def backtrack(word_idx: int, current_masks: list[int]) -> bool:
            if word_idx == n:
                return is_valid(current_masks)
            
            word_len = word_lengths[word_idx]
            for mask in range(1 << word_len):
                if get_abbr_len(mask, word_len) <= target_len:
                    current_masks.append(mask)
                    if backtrack(word_idx + 1, current_masks):
                        return True
                    current_masks.pop()
            return False

        return backtrack(0, [])

    for length in range(1, max(word_lengths) + 1):
        if check_length(length):
            return length
            
    return max(word_lengths)