METADATA = {
    "id": 692,
    "name": "Top K Frequent Words",
    "slug": "top-k-frequent-words",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "hash_map", "sorting", "string"],
    "difficulty": "medium",
    "time_complexity": "O(N log K)",
    "space_complexity": "O(N)",
    "description": "Given an array of strings words and an integer k, return the k most frequent strings. The result should be sorted by frequency from highest to lowest, and words with the same frequency should be sorted by their lexicographical order.",
}

import heapq

class WordFreqWrapper:
    """
    A wrapper class to handle custom comparison logic for the heap.
    
    LeetCode requires:
    1. Higher frequency comes first.
    2. If frequencies are equal, lexicographically smaller word comes first.
    
    Since Python's heapq is a min-heap, to simulate a max-priority behavior 
    for frequency while maintaining min-priority for lexicographical order 
    within a fixed-size heap of size K, we need to invert the logic.
    """
    def __init__(self, word: str, freq: int):
        self.word = word
        self.freq = freq

    def __lt__(self, other: "WordFreqWrapper") -> bool:
        # In a min-heap of size K:
        # We want to pop the 'least' important elements.
        # The 'least' important element is one with:
        # 1. Lower frequency.
        # 2. If frequencies are equal, the lexicographically LARGER word.
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.word > other.word

def solve(words: list[str], k: int) -> list[str]:
    """
    Finds the k most frequent words in the list.

    Args:
        words: A list of strings.
        k: The number of top frequent words to return.

    Returns:
        A list of k strings sorted by frequency (descending) and 
        lexicographical order (ascending).

    Examples:
        >>> solve(["i", "love", "leetcode", "i", "love", "coding"], 2)
        ['i', 'love']
        >>> solve(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
        ['the', 'is', 'sunny', 'day']
    """
    # Step 1: Count frequencies using a hash map
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # Step 2: Use a min-heap of size k to keep track of top elements
    # The heap will store WordFreqWrapper objects.
    # The 'smallest' element in our custom logic will be the one we want to discard.
    min_heap: list[WordFreqWrapper] = []

    for word, freq in counts.items():
        heapq.heappush(min_heap, WordFreqWrapper(word, freq))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 3: Extract elements from heap and sort them
    # Since it's a min-heap, elements come out in 'least important' order.
    # We need to reverse the result to get 'most important' order.
    result: list[str] = []
    while min_heap:
        result.append(heapq.heappop(min_heap).word)
    
    return result[::-1]
