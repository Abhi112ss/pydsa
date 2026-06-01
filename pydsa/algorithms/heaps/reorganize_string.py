METADATA = {
    "id": 767,
    "name": "Reorganize String",
    "slug": "reorganize-string",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "heap", "hash_map", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(N log K)",
    "space_complexity": "O(K)",
    "description": "Rearrange characters in a string so that no two adjacent characters are the same.",
}

import heapq
from collections import Counter

def solve(s: str) -> str:
    """
    Rearranges the characters in the string s such that no two adjacent characters are identical.

    Args:
        s: The input string to reorganize.

    Returns:
        A reorganized string if possible, otherwise an empty string "".

    Examples:
        >>> solve("aab")
        "aba"
        >>> solve("aaab")
        ""
    """
    # Count frequencies of each character
    char_counts = Counter(s)
    
    # Create a max-heap based on character frequencies.
    # Python's heapq is a min-heap, so we store negative counts to simulate a max-heap.
    max_heap = [(-count, char) for char, count in char_counts.items()]
    heapq.heapify(max_heap)
    
    # Check if the most frequent character exceeds the possibility of valid placement.
    # If max_freq > (n + 1) // 2, it's impossible to separate them.
    if max_heap and -max_heap[0][0] > (len(s) + 1) // 2:
        return ""
    
    result_chars = []
    # prev_char_data stores the character we just used so we don't pick it immediately again.
    # It acts as a "waiting room" for one turn.
    prev_char_data = None
    
    while max_heap or prev_char_data:
        # If we need to pick a character but the heap is empty, it means we are stuck
        # (though the initial frequency check prevents this for valid inputs).
        if not max_heap and prev_char_data:
            return ""
            
        # Pop the most frequent available character
        count, char = heapq.heappop(max_heap)
        result_chars.append(char)
        
        # Update the count (since count is negative, adding 1 moves it toward 0)
        count += 1
        
        # If there was a character waiting from the previous step, 
        # put it back into the heap now that it's no longer adjacent.
        if prev_char_data:
            heapq.heappush(max_heap, prev_char_data)
            prev_char_data = None
            
        # If the current character still has remaining occurrences, 
        # put it in the waiting room to ensure it's not used in the next step.
        if count < 0:
            prev_char_data = (count, char)
            
    return "".join(result_chars)
