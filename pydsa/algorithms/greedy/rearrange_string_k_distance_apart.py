METADATA = {
    "id": 358,
    "name": "Rearrange String k Distance Apart",
    "slug": "rearrange-string-k-distance-apart",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "hash_map"],
    "difficulty": "hard",
    "time_complexity": "O(N log A)",
    "space_complexity": "O(A)",
    "description": "Rearrange characters in a string such that the same characters are at least k distance apart.",
}

import heapq
from collections import Counter, deque

def solve(s: str, k: int) -> str:
    """
    Rearranges the string s such that the same characters are at least k distance apart.

    Args:
        s: The input string to rearrange.
        k: The minimum distance required between identical characters.

    Returns:
        The rearranged string if possible, otherwise an empty string.

    Examples:
        >>> solve("aabbcc", 3)
        'abcabc'
        >>> solve("aaabc", 3)
        ''
    """
    if k <= 1:
        return s

    # Count frequencies of each character
    frequencies = Counter(s)
    
    # Max-heap to store (-frequency, character)
    # We use negative frequency because Python's heapq is a min-heap
    max_heap = [(-count, char) for char, count in frequencies.items()]
    heapq.heapify(max_heap)

    # Queue to keep track of characters that are "on cooldown"
    # Stores tuples of (negative_frequency, character)
    wait_queue = deque()
    result_chars = []

    while max_heap:
        # Pick the character with the highest remaining frequency
        neg_freq, char = heapq.heappop(max_heap)
        
        result_chars.append(char)
        
        # Add the character to the wait queue with its updated frequency
        # We decrement the absolute frequency (which means adding 1 to neg_freq)
        wait_queue.append((neg_freq + 1, char))

        # If the wait queue reaches size k, the character at the front 
        # is now far enough away to be reused
        if len(wait_queue) == k:
            old_neg_freq, old_char = wait_queue.popleft()
            # Only push back into heap if there are remaining instances of the character
            if old_neg_freq < 0:
                heapq.heappush(max_heap, (old_neg_freq, old_char))

    # If the resulting string length matches the input, we succeeded
    final_string = "".join(result_chars)
    return final_string if len(final_string) == len(s) else ""
