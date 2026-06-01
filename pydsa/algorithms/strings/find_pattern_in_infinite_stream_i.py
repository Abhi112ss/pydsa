METADATA = {
    "id": 3023,
    "name": "Find Pattern in Infinite Stream I",
    "slug": "find-pattern-in-infinite-stream-i",
    "category": "String Matching",
    "aliases": [],
    "tags": ["string_matching", "kmp", "rolling_hash"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Determine if a pattern exists within a stream of integers using an efficient string matching approach.",
}

class PatternMatcher:
    """
    A class to handle pattern matching in a stream using the KMP algorithm.
    """

    def __init__(self, pattern: list[int]):
        """
        Initializes the matcher with a pattern and precomputes the KMP failure function.

        Args:
            pattern: The list of integers to search for in the stream.
        """
        self.pattern = pattern
        self.m = len(pattern)
        self.failure_function = self._compute_failure_function(pattern)
        self.current_match_index = 0
        self.stream_buffer = []

    def _compute_failure_function(self, pattern: list[int]) -> list[int]:
        """
        Computes the Longest Prefix which is also a Suffix (LPS) array.

        Args:
            pattern: The pattern to process.

        Returns:
            The failure function array.
        """
        m = len(pattern)
        pi = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = pi[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            pi[q] = k
        return pi

    def process_element(self, element: int) -> bool:
        """
        Processes a single element from the stream and checks if the pattern is completed.

        Args:
            element: The next integer from the stream.

        Returns:
            True if the pattern is found ending at this element, False otherwise.
        """
        # We only need to keep track of the current state in the KMP automaton
        # to avoid storing the entire stream.
        k = self.current_match_index
        
        while k > 0 and self.pattern[k] != element:
            k = self.failure_function[k - 1]
            
        if self.pattern[k] == element:
            k += 1
            
        self.current_match_index = k
        
        # If k reaches the length of the pattern, we found a match
        if k == self.m:
            # Reset k to the next possible match position using the failure function
            # to allow for overlapping matches if the problem required it.
            # However, for this specific problem, we just return True.
            self.current_match_index = self.failure_function[k - 1]
            return True
            
        return False

def solve(pattern: list[int], stream: list[int]) -> list[bool]:
    """
    Finds occurrences of a pattern in a stream of integers.

    Args:
        pattern: The pattern to search for.
        stream: The stream of integers.

    Returns:
        A list of booleans where result[i] is True if the pattern ends at stream[i].

    Examples:
        >>> solve([1, 2, 3], [1, 2, 1, 2, 3])
        [False, False, False, False, True]
        >>> solve([1, 1], [1, 1, 1])
        [False, True, True]
    """
    matcher = PatternMatcher(pattern)
    results = []
    
    for val in stream:
        # The KMP state machine processes each element in O(1) amortized time
        results.append(matcher.process_element(val))
        
    return results
