METADATA = {
    "id": 3306,
    "name": "Count of Substrings Containing Every Vowel and K Consonants II",
    "slug": "count-of-substrings-containing-every-vowel-and-k-consonants-ii",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings that contain all five vowels and at least k consonants.",
}

def solve(word: str, k: int) -> int:
    """
    Args:
        word: A string consisting of lowercase English letters.
        k: An integer representing the minimum number of consonants required.

    Returns:
        The total count of substrings containing all five vowels and at least k consonants.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}

    def count_at_least(min_k: int) -> int:
        total_count = 0
        left = 0
        vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        distinct_vowels = 0
        consonant_count = 0

        for right in range(len(word)):
            char = word[right]
            if char in vowels:
                if vowel_counts[char] == 0:
                    distinct_vowels += 1
                vowel_counts[char] += 1
            else:
                consonant_count += 1

            while distinct_vowels == 5 and consonant_count >= min_k:
                total_count += len(word) - right
                left_char = word[left]
                if left_char in vowels:
                    vowel_counts[left_char] -= 1
                    if vowel_counts[left_char] == 0:
                        distinct_vowels -= 1
                else:
                    consonant_count -= 1
                left += 1
            
        return total_count

    return count_at_least(k)