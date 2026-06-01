METADATA = {
    "id": 1397,
    "name": "Find All Good Strings",
    "slug": "find-all-good-strings",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "kmp", "string", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n * m * 26)",
    "space_complexity": "O(n * m)",
    "description": "Count the number of strings of length n that do not contain the pattern as a substring, modulo 10^9 + 7.",
}

def solve(n: int, pattern: str, avoidance: str) -> int:
    """
    Finds the number of strings of length n that do not contain 'pattern' 
    as a substring and do not contain 'avoidance' as a substring.

    Args:
        n: The length of the strings to generate.
        pattern: The string that must not appear as a substring.
        avoidance: The string that must not appear as a substring.

    Returns:
        The count of good strings modulo 10^9 + 7.

    Examples:
        >>> solve(2, "a", "b")
        1
        >>> solve(3, "ab", "ba")
        4
    """
    MOD = 1_000_000_007
    m_len = len(pattern)
    a_len = len(avoidance)

    def build_kmp_transition_table(s: str) -> list[list[int]]:
        """
        Builds a transition table for KMP state transitions.
        table[state][char_idx] returns the next state (length of longest prefix matched).
        """
        length = len(s)
        # pi[i] is the length of the longest proper prefix of s[0...i] 
        # that is also a suffix of s[0...i].
        pi = [0] * length
        for i in range(1, length):
            j = pi[i - 1]
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j

        # transition[state][char] = next_state
        transition = [[0] * 26 for _ in range(length + 1)]
        for state in range(length):
            for char_code in range(26):
                char = chr(ord('a') + char_code)
                # Simulate adding 'char' to the current prefix of length 'state'
                curr_state = state
                while curr_state > 0 and char != s[curr_state]:
                    curr_state = pi[curr_state - 1]
                if char == s[curr_state]:
                    transition[state][char_code] = curr_state + 1
                else:
                    transition[state][char_code] = 0
        
        # For the terminal state (full match), we don't care about transitions 
        # because we stop there, but for DP we fill it to avoid index errors.
        return transition

    # Precompute KMP transition tables for both strings
    # pattern_trans[i][c] is the new state in 'pattern' after adding char c to state i
    pattern_trans = build_kmp_transition_table(pattern)
    avoid_trans = build_kmp_transition_table(avoidance)

    # dp[i][p_state][a_state] = number of strings of length i 
    # with pattern prefix match length p_state and avoidance prefix match length a_state
    # We use two layers to optimize space from O(n*m*a) to O(m*a)
    dp = [[0] * a_len for _ in range(m_len)]
    dp[0][0] = 1

    for _ in range(n):
        new_dp = [[0] * a_len for _ in range(m_len)]
        for p_state in range(m_len):
            for a_state in range(a_len):
                if dp[p_state][a_state] == 0:
                    continue
                
                current_count = dp[p_state][a_state]
                for char_idx in range(26):
                    next_p = pattern_trans[p_state][char_idx]
                    next_a = avoid_trans[a_state][char_idx]
                    
                    # Only transition if neither pattern nor avoidance is fully matched
                    if next_p < m_len and next_a < a_len:
                        new_dp[next_p][next_a] = (new_dp[next_p][next_a] + current_count) % MOD
        dp = new_dp

    # Sum all valid states in the final DP table
    total_good_strings = 0
    for p_state in range(m_len):
        for a_state in range(a_len):
            total_good_strings = (total_good_strings + dp[p_state][a_state]) % MOD
            
    return total_good_strings
