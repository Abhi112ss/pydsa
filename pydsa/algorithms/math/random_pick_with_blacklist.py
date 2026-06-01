METADATA = {
    "id": 710,
    "name": "Random Pick with Blacklist",
    "slug": "random-pick-with-blacklist",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "random", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(1) for pick, O(B) for initialization",
    "space_complexity": "O(B)",
    "description": "Design a class that picks a random integer from [0, n-1] excluding a given blacklist.",
}

import random

class Solution:
    def __init__(self, n: int, blacklist: list[int]):
        """
        Initializes the RandomPicker with n and a blacklist.
        
        The strategy is to partition the range [0, n-1] into two parts:
        1. The 'safe' prefix: [0, n - len(blacklist) - 1]
        2. The 'replacement' suffix: [n - len(blacklist), n - 1]
        
        We map blacklisted numbers that fall into the 'safe' prefix to 
        available numbers in the 'replacement' suffix.
        
        Args:
            n: The upper bound (exclusive) of the range.
            blacklist: A list of integers to be excluded from selection.
        """
        self.n = n
        self.blacklist_set = set(blacklist)
        
        # The threshold defines the boundary of the 'safe' prefix.
        # Numbers below this threshold are guaranteed not to be in the blacklist
        # if we handle the mapping correctly.
        self.threshold = n - len(blacklist)
        
        # mapping: blacklisted_number_in_prefix -> available_number_in_suffix
        self.mapping: dict[int, int] = {}
        
        # We use two pointers/iterators to fill the mapping.
        # One pointer looks for blacklisted numbers in the prefix [0, threshold-1].
        # One pointer looks for available (non-blacklisted) numbers in the suffix [threshold, n-1].
        prefix_ptr = 0
        suffix_ptr = self.threshold
        
        # We only need to map as many numbers as there are blacklisted numbers in the prefix.
        # However, it's easier to just iterate through the blacklist and map those in the prefix.
        # To keep O(B) space and time, we find available numbers in the suffix.
        
        # First, identify which numbers in the suffix are actually available.
        available_in_suffix = []
        for i in range(self.threshold, n):
            if i not in self.blacklist_set:
                available_in_suffix.append(i)
        
        # Second, map blacklisted numbers in the prefix to the available suffix numbers.
        suffix_idx = 0
        for val in blacklist:
            if val < self.threshold:
                # This blacklisted number is in our 'safe' range, so we must replace it.
                self.mapping[val] = available_in_suffix[suffix_idx]
                suffix_idx += 1
        
        # The effective range for random selection is [0, threshold - 1] 
        # plus the number of successful mappings we created.
        # Actually, the number of valid choices is always (n - len(blacklist)).
        self.valid_count = n - len(blacklist)

    def pick(self) -> int:
        """
        Returns a random integer from the non-blacklisted set.
        
        Returns:
            A random integer from [0, n-1] not in the blacklist.
            
        Examples:
            >>> sol = Solution(10, [2, 3])
            >>> sol.pick() # Returns one of [0, 1, 4, 5, 6, 7, 8, 9]
        """
        # Pick a random index from the range of available counts.
        # This index represents a number in the 'safe' prefix [0, valid_count - 1].
        idx = random.randint(0, self.valid_count - 1)
        
        # If the picked index is in our mapping, it means it was a blacklisted 
        # number in the prefix, so we return its mapped replacement from the suffix.
        return self.mapping.get(idx, idx)

def solve():
    """
    Example usage of the Solution class.
    """
    n = 10
    blacklist = [2, 3]
    sol = Solution(n, blacklist)
    
    results = [sol.pick() for _ in range(10)]
    print(f"Random picks: {results}")
