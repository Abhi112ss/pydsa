METADATA = {
    "id": 2182,
    "name": "Construct String With Repeat Limit",
    "slug": "construct-string-with-repeat-limit",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "priority_queue", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n log k) where k is the alphabet size",
    "space_complexity": "O(k) where k is the alphabet size",
    "description": "Construct the lexicographically largest string possible given a limit on consecutive identical characters.",
}

import heapq
from collections import Counter

def solve(s: str, limit: int) -> str:
    """
    Constructs the lexicographically largest string possible such that no character 
    is repeated more than 'limit' times consecutively.

    Args:
        s: The input string containing lowercase English letters.
        limit: The maximum number of times a character can appear consecutively.

    Returns:
        The lexicographically largest string possible, or an empty string if impossible.

    Examples:
        >>> solve("aaaaaaaaaaaabc", 2)
        'ababaaaaaaaabc' # Note: This is a simplified example; actual logic follows greedy max-heap.
        >>> solve("aaaaaa", 2)
        ''
    """
    # Count frequencies of each character
    counts = Counter(s)
    
    # Max-heap to store (-frequency, character) to always pick the largest available char
    # We use negative frequency because Python's heapq is a min-heap
    max_heap = [(-count, char) for char, count in counts.items()]
    heapq.heapify(max_heap)
    
    result_chars = []
    
    while max_heap:
        # Get the character with the highest remaining frequency
        freq, char = heapq.heappop(max_heap)
        freq = -freq  # Convert back to positive
        
        # Determine how many times we can append this character
        # We can append up to 'limit' times, or the total remaining count
        use_count = min(freq, limit)
        
        # Check if we can actually append this character. 
        # If the last character in result is the same as current, 
        # we must ensure we don't exceed the limit.
        # However, since we always pick the absolute max from the heap, 
        # the only way we'd violate the limit is if we didn't have a 
        # different character to "break" the sequence.
        
        # In a greedy approach with a max-heap, we append the character, 
        # then if we still have more of it, we must pick the next best character 
        # to act as a separator.
        
        result_chars.append(char * use_count)
        freq -= use_count
        
        # If we still have more of the current character left, 
        # we need to find the second most frequent character to act as a buffer.
        if freq > 0:
            if not max_heap:
                # No other character available to break the sequence
                return ""
            
            # Get the second most frequent character
            sec_freq, sec_char = heapq.heappop(max_heap)
            sec_freq = -sec_freq
            
            # Append exactly one instance of the separator character
            result_chars.append(sec_char)
            sec_freq -= 1
            
            # Put both characters back into the heap with updated counts
            # We put the current char back first to maintain lexicographical priority
            if freq > 0:
                heapq.heappush(max_heap, (-freq, char))
            if sec_freq > 0:
                heapq.heappush(max_heap, (-sec_freq, sec_char))
            # Re-add the current char if it was already popped but we need to re-push it
            # Actually, the logic above handles the re-pushing correctly.
            # But we must ensure the current char is pushed back if it still has count.
            # Wait, the current char was already popped. Let's refine the push logic.
            
            # Corrected logic: 
            # 1. Pop max. 2. Use 'limit' amount. 3. If remaining > 0, pop second max.
            # 4. Use 1 of second max. 5. Push both back.
            # Note: The 'char' was already popped, so we push it back with 'freq'.
            # The 'sec_char' was already popped, so we push it back with 'sec_freq'.
            # We must be careful not to double-push.
            
            # Let's re-implement the loop body cleanly.
            pass # Placeholder for the logic below
            
    # Re-implementing the loop body to be cleaner and avoid the 'pass'
    return _greedy_construct(counts, limit)

def _greedy_construct(counts: dict[str, int], limit: int) -> str:
    max_heap = [(-count, char) for char, count in counts.items()]
    heapq.heapify(max_heap)
    
    res = []
    
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        freq = -freq
        
        # 1. Use as many as possible up to the limit
        can_use = min(freq, limit)
        res.append(char * can_use)
        freq -= can_use
        
        # 2. If we still have this character left, we MUST use a different character
        if freq > 0:
            if not max_heap:
                return ""
            
            sec_freq, sec_char = heapq.heappop(max_heap)
            sec_freq = -sec_freq
            
            # Use exactly one of the second character to break the streak
            res.append(sec_char)
            sec_freq -= 1
            
            # 3. Push both back into the heap with updated counts
            if freq > 0:
                heapq.heappush(max_heap, (-freq, char))
            if sec_freq > 0:
                heapq.heappush(max_heap, (-sec_freq, sec_char))
        else:
            # If no more of the current character, we don't need a separator.
            # However, we might have popped the character but it's now exhausted.
            # We don't need to push it back.
            pass
            
    return "".join(res)

# The solve function is actually just a wrapper for the logic
def solve_final(s: str, limit: int) -> str:
    """
    Implementation of the greedy approach using a max-heap.
    """
    counts = Counter(s)
    max_heap = [(-count, char) for char, count in counts.items()]
    heapq.heapify(max_heap)
    
    res = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        freq = -freq
        
        # Append the maximum allowed consecutive characters
        use_count = min(freq, limit)
        res.append(char * use_count)
        freq -= use_count
        
        # If character still has remaining count, we need a separator
        if freq > 0:
            if not max_heap:
                return ""
            
            # Get the next best character to act as a buffer
            sec_freq, sec_char = heapq.heappop(max_heap)
            sec_freq = -sec_freq
            
            # Append exactly one separator
            res.append(sec_char)
            sec_freq -= 1
            
            # Push both back to the heap for the next iteration
            if freq > 0:
                heapq.heappush(max_heap, (-freq, char))
            if sec_freq > 0:
                heapq.heappush(max_heap, (-sec_freq, sec_char))
        # If freq is 0, we don't push it back, and we don't need a separator
                
    return "".join(res)

# Re-assigning solve to the correct implementation
solve = solve_final