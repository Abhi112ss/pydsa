METADATA = {
    "id": 2800,
    "name": "Shortest String That Contains Three Strings",
    "slug": "shortest-string-that-contains-three-strings",
    "category": "String",
    "aliases": [],
    "tags": ["string", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the shortest string that contains three given strings as substrings by checking all permutations.",
}

import itertools

def get_overlap_length(s1: str, s2: str) -> int:
    """
    Calculates the maximum length of a suffix of s1 that is also a prefix of s2.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        The length of the longest overlap.
    """
    max_possible_overlap = min(len(s1), len(s2))
    # Check from longest possible overlap down to 1
    for length in range(max_possible_overlap, 0, -1):
        if s1.endswith(s2[:length]):
            return length
    return 0

def solve(word1: str, word2: str, word3: str) -> str:
    """
    Finds the shortest string that contains word1, word2, and word3 as substrings.

    The algorithm considers all 6 permutations of the three words. For each 
    permutation, it merges the words by maximizing the overlap between 
    adjacent strings. It also handles cases where one word might be 
    entirely contained within another.

    Args:
        word1: The first input string.
        word2: The second input string.
        word3: The third input string.

    Returns:
        The shortest string containing all three words.

    Examples:
        >>> solve("a", "b", "c")
        'abc'
        >>> solve("ab", "bc", "cd")
        'abcd'
        >>> solve("a", "ab", "abc")
        'abc'
    """
    words = [word1, word2, word3]
    shortest_result = ""

    # Iterate through all possible permutations of the three words
    for permutation in itertools.permutations(words):
        # Start with the first word in the current permutation
        current_merged = permutation[0]
        
        # Flag to track if we need to skip a word because it's already a substring
        # However, a simpler way is to check containment during the merge process
        # We build the string by merging the next word into the current result
        
        # To handle containment correctly, we check if the next word is already in the current string
        # If not, we find the maximum overlap between the current string's suffix and the next word's prefix
        
        # We need to be careful: the "current_merged" grows. 
        # A word might be contained in the *original* words or the *merged* result.
        # The most robust way for 3 words is to build the sequence:
        # Result = WordA + (WordB - overlap) + (WordC - overlap)
        # But we must handle if WordB is inside WordA or WordC is inside (WordA+WordB)
        
        # Let's refine the merge logic for a specific permutation (A, B, C):
        # 1. Start with A.
        # 2. If B is in A, current = A. Else, current = A + B[overlap:]
        # 3. If C is in current, current = current. Else, current = current + C[overlap:]
        
        temp_string = permutation[0]
        for i in range(1, 3):
            next_word = permutation[i]
            if next_word in temp_string:
                continue
            
            # Find overlap between the end of the current built string and the start of the next word
            overlap = get_overlap_length(temp_string, next_word)
            temp_string += next_word[overlap:]
            
        # Update the global shortest string found so far
        if shortest_result == "" or len(temp_string) < len(shortest_result):
            shortest_result = temp_string
        elif len(temp_string) == len(shortest_result):
            # If lengths are equal, the problem doesn't specify lexicographical order, 
            # but usually, any valid shortest string is accepted.
            if temp_string < shortest_result:
                shortest_result = temp_string

    return shortest_result
