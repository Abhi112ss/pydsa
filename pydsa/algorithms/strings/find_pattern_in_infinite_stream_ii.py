METADATA = {
    "id": 3037,
    "name": "Find Pattern in Infinite Stream II",
    "slug": "find-pattern-in-infinite-stream-ii",
    "category": "String Matching",
    "aliases": [],
    "tags": ["string_matching", "kmp", "stream"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Determine if a pattern exists in a stream of integers using a KMP-based state machine approach.",
}

class PatternStreamMatcher:
    """
    A state machine based on the Knuth-Morris-Pratt (KMP) algorithm 
    to detect a pattern within an incoming stream of integers.
    """

    def __init__(self, pattern: list[int]):
        """
        Initializes the matcher with a pattern and precomputes the KMP failure function.

        Args:
            pattern: The integer sequence to search for.
        """
        self.pattern = pattern
        self.m = len(pattern)
        self.failure_function = self._compute_failure_function(pattern)
        self.current_state = 0

    def _compute_failure_function(self, pattern: list[int]) -> list[int]:
        """
        Computes the Longest Prefix which is also a Suffix (LPS) array.

        Args:
            pattern: The pattern to process.

        Returns:
            A list of integers representing the failure function.
        """
        m = len(pattern)
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        return lps

    def next_element(self, val: int) -> bool:
        """
        Processes the next integer from the stream and checks if the pattern is completed.

        Args:
            val: The next integer from the stream.

        Returns:
            True if the pattern is found ending at this element, False otherwise.
        """
        # Standard KMP state transition logic
        while self.current_state > 0 and val != self.pattern[self.current_state]:
            self.current_state = self.failure_function[self.current_state - 1]
        
        if val == self.pattern[self.current_state]:
            self.current_state += 1
        
        # If state reaches the length of the pattern, we found a match
        if self.current_state == self.m:
            # Reset state to allow finding overlapping patterns if necessary
            # (Though for this specific problem, we just return True)
            self.current_state = self.failure_function[self.m - 1]
            return True
            
        return False

def solve(pattern: list[int], stream: list[int]) -> list[bool]:
    """
    Processes a stream of integers to find occurrences of a pattern.

    Args:
        pattern: The integer pattern to search for.
        stream: The stream of integers to process.

    Returns:
        A list of booleans where result[i] is True if the pattern ends at stream[i].

    Examples:
        >>> solve([1, 2, 1], [1, 2, 1, 2, 1])
        [False, False, True, False, True]
    """
    matcher = PatternStreamMatcher(pattern)
    results = []
    
    for val in stream:
        results.append(matcher.next_element(val))
        
    return results
