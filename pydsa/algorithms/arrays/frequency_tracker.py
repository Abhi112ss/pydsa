METADATA = {
    "id": 2671,
    "name": "Frequency Tracker",
    "slug": "frequency_tracker",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "design", "data_structures"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(N)",
    "description": "Design a data structure that tracks the frequency of elements and allows retrieving the most frequent element in constant time.",
}

from collections import defaultdict

class FrequencyTracker:
    def __init__(self) -> None:
        """
        Initializes the FrequencyTracker.
        
        Uses two hash maps:
        1. val_to_freq: maps a value to its current frequency.
        2. freq_to_vals: maps a frequency to a set of values having that frequency.
        3. max_freq: tracks the current maximum frequency present in the tracker.
        """
        self.val_to_freq: dict[int, int] = defaultdict(int)
        self.freq_to_vals: dict[int, set[int]] = defaultdict(set)
        self.max_freq: int = 0

    def add(self, val: int) -> None:
        """
        Adds an element to the tracker.

        Args:
            val: The integer value to add.
        """
        old_freq = self.val_to_freq[val]
        new_freq = old_freq + 1
        
        # Update the value's frequency mapping
        self.val_to_freq[val] = new_freq
        
        # Remove the value from its old frequency set if it existed
        if old_freq > 0:
            self.freq_to_vals[old_freq].remove(val)
            
        # Add the value to the new frequency set
        self.freq_to_vals[new_freq].add(val)
        
        # Update the global maximum frequency tracker
        if new_freq > self.max_freq:
            self.max_freq = new_freq

    def remove(self, val: int) -> None:
        """
        Removes one occurrence of the element from the tracker.

        Args:
            val: The integer value to remove.
        """
        old_freq = self.val_to_freq[val]
        if old_freq == 0:
            return

        new_freq = old_freq - 1
        
        # Remove from current frequency set
        self.freq_to_vals[old_freq].remove(val)
        
        # Update the value's frequency mapping
        if new_freq > 0:
            self.val_to_freq[val] = new_freq
            self.freq_to_vals[new_freq].add(val)
        else:
            # If frequency drops to 0, remove from val_to_freq entirely
            del self.val_to_freq[val]
            
        # If the removed element was the only one at max_freq, decrement max_freq
        if not self.freq_to_vals[self.max_freq]:
            self.max_freq -= 1

    def top_k_frequent(self, k: int) -> list[int]:
        """
        Returns the k most frequent elements. 
        Note: The problem description for 2671 usually asks for the most frequent 
        element or top k. Based on standard LeetCode 2671 requirements, 
        we return the k most frequent elements.

        Args:
            k: The number of most frequent elements to return.

        Returns:
            A list of the k most frequent elements.
        """
        # Since the problem asks for top k, we iterate downwards from max_freq
        # This is efficient because we only visit frequencies that actually contain elements
        result = []
        current_f = self.max_freq
        
        while len(result) < k and current_f > 0:
            if current_f in self.freq_to_vals and self.freq_to_vals[current_f]:
                # Add elements from the current highest frequency set
                # We take elements until we reach k or exhaust the set
                for val in self.freq_to_vals[current_f]:
                    if len(result) < k:
                        result.append(val)
                    else:
                        break
            current_f -= 1
            
        return result

def solve():
    """
    Example usage of the FrequencyTracker.
    """
    tracker = FrequencyTracker()
    tracker.add(5)
    tracker.add(7)
    tracker.add(5)
    tracker.add(7)
    tracker.add(4)
    tracker.add(5)
    # Frequencies: {5: 3, 7: 2, 4: 1}
    # Top 2: [5, 7]
    print(tracker.top_k_frequent(2)) 
    
    tracker.remove(5)
    # Frequencies: {5: 2, 7: 2, 4: 1}
    # Top 2: [5, 7] (order might vary due to set)
    print(tracker.top_k_frequent(2))
