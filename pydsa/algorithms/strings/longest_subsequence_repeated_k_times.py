METADATA = {
    "id": 2014,
    "name": "Longest Subsequence Repeated k Times",
    "slug": "longest-subsequence-repeated-k-times",
    "category": "String",
    "aliases": [],
    "tags": ["backtracking", "strings", "greedy", "breadth-first-search"],
    "difficulty": "hard",
    "time_complexity": "O(N * (20/k)^L) where L is the max length",
    "space_complexity": "O((20/k)^L)",
    "description": "Find the longest subsequence of a string that is repeated k times.",
}

from collections import deque

def solve(s: str, k: int) -> str:
    """
    Finds the longest subsequence of string 's' that appears at least 'k' times.

    The approach uses Breadth-First Search (BFS) to build potential subsequences
    character by character. Since k >= 2, the maximum length of the subsequence
    is limited (at most 7 for a string of length 200), making BFS feasible.

    Args:
        s: The input string.
        k: The number of times the subsequence must repeat.

    Returns:
        The longest subsequence that repeats k times. If multiple exist, 
        the lexicographically largest one is returned.

    Examples:
        >>> solve("letsleetcode", 2)
        'lets'
        >>> solve("aaaaa", 2)
        'aa'
    """
    # Count frequencies of each character to filter candidates
    # Only characters appearing at least k times can be part of the subsequence
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Candidates are characters that appear at least k times, sorted descending
    # to help find lexicographically larger strings first
    candidates = sorted(
        [char for char in char_counts if char_counts[char] >= k],
        reverse=True
    )

    def is_subsequence_repeated_k_times(sub: str, target_s: str, k_val: int) -> bool:
        """Checks if 'sub' appears as a subsequence in 'target_s' at least 'k_val' times."""
        if not sub:
            return True
        
        count = 0
        current_pos = 0
        # We need to find the subsequence k times. 
        # However, the problem asks for the subsequence to be repeated k times 
        # within the original string as non-overlapping occurrences? 
        # Actually, the definition is: 'sub' is a subsequence of 's' such that 
        # 'sub' repeated k times is also a subsequence of 's'.
        
        # Correct interpretation: 'sub' repeated k times is a subsequence of 's'.
        # We can check this by trying to find 'sub' k times sequentially.
        full_sub = sub * k_val
        it = iter(target_s)
        return all(char in it for char in full_sub)

    # BFS to find the longest subsequence
    # We start with an empty string and append candidate characters
    queue = deque([""])
    best_subsequence = ""

    while queue:
        current = queue.popleft()

        for char in candidates:
            next_sub = current + char
            
            # If the new string (repeated k times) is a subsequence of s
            if is_subsequence_repeated_k_times(next_sub, s, k):
                # Since we use BFS, the first time we find a length, 
                # it's one of the longest. We keep updating to get 
                # the lexicographically largest among the longest.
                best_subsequence = next_sub
                queue.append(next_sub)
            
            # Note: We don't need to check length here because BFS 
            # naturally explores shorter strings before longer ones.
            # The queue will eventually exhaust all valid subsequences.

    return best_subsequence
