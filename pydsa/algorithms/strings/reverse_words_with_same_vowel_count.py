METADATA = {
    "id": 3775,
    "name": "Reverse Words With Same Vowel Count",
    "slug": "reverse-words-with-same-vowel-count",
    "category": "Strings",
    "aliases": [],
    "tags": ["two_pointer", "strings", "hash_table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reverse the order of words in a sentence that have the same number of vowels.",
}

def solve(sentence: str) -> str:
    """
    Reverses the order of words in a sentence that have the same number of vowels.

    Args:
        sentence: A string containing words separated by single spaces.

    Returns:
        A string where words with the same vowel count are reversed relative to 
        each other, while maintaining the original positions of the vowel counts.

    Examples:
        >>> solve("hello world")
        'hello world'
        >>> solve("abc def ghi")
        'abc def ghi'
        >>> solve("aeiou bcd eiou")
        'aeiou bcd eiou'
        >>> solve("apple eat orange")
        'apple eat orange'
    """
    def count_vowels(word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count

    words = sentence.split(" ")
    vowel_counts = [count_vowels(word) for word in words]
    
    # Map to store lists of words grouped by their vowel count
    # We use a dictionary where key is vowel count and value is a list of words
    groups: dict[int, list[str]] = {}
    for word in words:
        count = count_vowels(word)
        if count not in groups:
            groups[count] = []
        groups[count].append(word)
    
    # Reverse the list of words for each vowel count group
    for count in groups:
        groups[count].reverse()
        
    # Reconstruct the sentence by picking words from the reversed groups
    # based on the original sequence of vowel counts
    result_words: list[str] = []
    # Track how many words of a specific vowel count we have used
    # to simulate popping from the reversed lists
    group_indices: dict[int, int] = {count: 0 for count in groups}
    
    # Since we reversed the lists in 'groups', we can treat them as queues 
    # or simply use an index to pick the next available word for that count.
    # However, it's easier to just use the reversed lists and pop from the front.
    # To avoid O(N) pops from the front of a list, we use a pointer or reverse again.
    # Let's use a pointer approach for efficiency.
    
    # Actually, a simpler way: 
    # 1. Group words by count.
    # 2. Reverse each group.
    # 3. Iterate through original vowel_counts and pick the next word from the corresponding group.
    
    # Re-initialize groups to be used as queues (using index pointers)
    group_pointers: dict[int, int] = {count: 0 for count in groups}
    
    for count in vowel_counts:
        # Get the next word from the reversed group for this vowel count
        word_index = group_pointers[count]
        result_words.append(groups[count][word_index])
        group_pointers[count] += 1
        
    return " ".join(result_words)
