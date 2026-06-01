METADATA = {
    "id": 3734,
    "name": "Lexicographically Smallest Palindromic Permutation Greater Than Target",
    "slug": "lexicographically-smallest-palindromic-permutation-greater-than-target",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "greedy", "palindrome"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest palindromic permutation of a given string that is strictly greater than a target string.",
}

def solve(s: str, target: str) -> str:
    """
    Args:
        s: The input string used to form the palindrome.
        target: The target string to compare against.

    Returns:
        The lexicographically smallest palindromic permutation of s that is greater than target, or an empty string if none exists.
    """
    n = len(s)
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_chars = []
    for char, count in char_counts.items():
        if count % 2 != 0:
            odd_chars.append(char)

    if len(odd_chars) > (1 if n % 2 != 0 else 0):
        return ""

    half_len = n // 2
    sorted_chars = sorted(char_counts.keys())
    
    available_half = []
    for char in sorted_chars:
        available_half.extend([char] * (char_counts[char] // 2))

    def get_palindrome(prefix: list, middle: str, suffix_chars: list) -> str:
        suffix = suffix_chars[::-1]
        return "".join(prefix) + middle + "".join(suffix)

    target_half = target[:half_len]
    
    current_half = []
    for i in range(half_len):
        target_char = target[i]
        
        possible_chars = sorted([c for c in char_counts if char_counts[c] > 0 and (i == 0 or True)]) 
        
        found_greater = False
        for char in sorted_chars:
            if char_counts[char] >= 2:
                if char > target_char:
                    current_half.append(char)
                    char_counts[char] -= 2
                    
                    remaining_half = []
                    for c in sorted_chars:
                        remaining_half.extend([c] * (char_counts[c] // 2))
                    
                    middle = ""
                    if n % 2 != 0:
                        for c in sorted_chars:
                            if char_counts[c] % 2 != 0:
                                middle = c
                                break
                    
                    return get_palindrome(current_half, middle, remaining_half)
                elif char == target_char:
                    pass 

        if target_char in char_counts and char_counts[target_char] >= 2:
            current_half.append(target_char)
            char_counts[target_char] -= 2
        else:
            return ""

    if n % 2 != 0:
        middle_char = ""
        for c in sorted_chars:
            if char_counts[c] % 2 != 0:
                middle_char = c
                break
        
        if middle_char > target[half_len]:
            return get_palindrome(current_half, middle_char, [])
        else:
            return ""
    else:
        full_palindrome = "".join(current_half) + "".join(current_half[::-1])
        if full_palindrome > target:
            return full_palindrome
        return ""

    return ""

def solve(s: str, target: str) -> str:
    """
    Args:
        s: The input string used to form the palindrome.
        target: The target string to compare against.

    Returns:
        The lexicographically smallest palindromic permutation of s that is greater than target, or an empty string if none exists.
    """
    n = len(s)
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    odds = [c for c, count in counts.items() if count % 2 != 0]
    if len(odds) > (n % 2):
        return ""
    
    mid_char = odds[0] if odds else ""
    
    half_chars = []
    for char in sorted(counts.keys()):
        half_chars.extend([char] * (counts[char] // 2))
    
    m = len(half_chars)
    target_half = target[:m]
    
    res_half = []
    
    def backtrack(idx, is_greater):
        if idx == m:
            if n % 2 == 1:
                if is_greater or mid_char > target[m]:
                    return True
                return False
            else:
                full = "".join(res_half) + "".join(res_half[::-1])
                return full > target
            
        start_char_idx = 0
        if not is_greater:
            t_char = target[idx]
            chars_available = sorted([c for c in counts if counts[c] >= 2])
            
            for c in chars_available:
                if c < t_char:
                    continue
                
                if c > t_char:
                    res_half.append(c)
                    counts[c] -= 2
                    if backtrack(idx + 1, True):
                        return True
                    counts[c] += 2
                    res_half.pop()
                    return False
                else:
                    if counts[c] >= 2:
                        res_half.append(c)
                        counts[c] -= 2
                        if backtrack(idx + 1, False):
                            return True
                        counts[c] += 2
                        res_half.pop()
                    return False
            return False
        else:
            chars_available = sorted([c for c in counts if counts[c] >= 2])
            for c in chars_available:
                res_half.append(c)
                counts[c] -= 2
                if backtrack(idx + 1, True):
                    return True
                counts[c] += 2
                res_half.pop()
            return False

    # The backtracking approach above is too slow for O(n). 
    # Let's use a greedy approach with a single pass.
    
    half_len = n // 2
    prefix = []
    
    # Try to match the target prefix as long as possible
    for i in range(half_len):
        t_char = target[i]
        
        # Option 1: Try to pick a character strictly greater than target[i]
        # This would allow us to pick the smallest possible characters for the rest of the prefix.
        # We check this at every position to see if it's a valid "pivot".
        
        # However, the standard way is:
        # 1. Try to match target prefix exactly.
        # 2. If we can't, or if matching exactly leads to a palindrome <= target,
        #    we must backtrack to the last position where we could have picked a larger char.
        pass

    # Correct Greedy:
    # 1. Build the smallest possible palindrome.
    # 2. If it's > target, we are done.
    # 3. If not, find the rightmost position in the first half where we can increment the character.
    
    # Let's refine:
    # First, find the largest prefix of the target that can be formed by the available half-characters.
    
    available_half = []
    for c in sorted(counts.keys()):
        available_half.extend([c] * (counts[c] // 2))
    
    # Try to match target[:half_len]
    current_counts = counts.copy()
    match_idx = 0
    for i in range(half_len):
        t_char = target[i]
        if current_counts.get(t_char, 0) >= 2:
            current_counts[t_char] -= 2
            match_idx += 1
        else:
            break
            
    # If we matched the whole half_len
    if match_idx == half_len:
        # Check middle char if exists
        if n % 2 == 1:
            m_char = ""
            for c in sorted(current_counts.keys()):
                if current_counts[c] % 2 != 0:
                    m_char = c
                    break
            if m_char > target[half_len]:
                # Success!
                res_prefix = target[:half_len]
                return res_prefix + m_char + res_prefix[::-1]
            else:
                # Must backtrack from the last possible position in the prefix
                match_idx -= 1
        else:
            # Check the full palindrome
            res_prefix = target[:half_len]
            full = res_prefix + res_prefix[::-1]
            if full > target:
                return full
            else:
                match_idx -= 1
                
    # Backtrack: find the rightmost index i in [0, match_idx] where we can pick a char > target[i]
    # or if match_idx was already less than half_len, find the rightmost i in [0, match_idx]
    # where we can pick a char > target[i].
    
    # Actually, it's simpler:
    # Iterate i from min(match_idx, half_len - 1) down to 0.
    # At each i, try to pick the smallest char > target[i].
    # If successful, fill the rest of the prefix with the smallest available chars.
    
    # Re-calculate counts for the prefix matching attempt
    current_counts = counts.copy()
    for i in range(match_idx):
        current_counts[target[i]] -= 2
        
    for i in range(match_idx, -1, -1):
        # If i < half_len, we try to find a char > target[i]
        # If i == half_len and n is odd, we try to find a mid_char > target[half_len]
        
        if i < half_len:
            t_char = target[i]
            # Try to find smallest char > t_char
            found_char = None
            for c in sorted(current_counts.keys()):
                if c > t_char and current_counts[c] >= 2:
                    found_char = c
                    break
            
            if found_char:
                # Found it! Construct prefix
                res_prefix = list(target[:i])
                res_prefix.append(found_char)
                current_counts[found_char] -= 2
                
                # Fill remaining prefix with smallest available
                remaining_half = []
                for c in sorted(current_counts.keys()):
                    remaining_half.extend([c] * (current_counts[c] // 2))
                
                # We need to fill from index i+1 to half_len-1
                # The remaining_half is already sorted.
                needed = half_len - (i + 1)
                res_prefix.extend(remaining_half[:needed])
                
                # Middle char
                mid = ""
                if n % 2 == 1:
                    for c in sorted(current_counts.keys()):
                        if current_counts[c] % 2 != 0:
                            mid = c
                            break
                
                # The remaining_half might have been used partially. 
                # Let's be more precise.
                # The prefix is res_prefix. The suffix is res_prefix[::-1].
                # But we must ensure the suffix is the reverse of the prefix.
                # The characters used in res_prefix are fixed.
                # The remaining characters must form the rest of the palindrome.
                
                # Let's re-calculate everything from scratch for the found_char
                final_counts = counts.copy()
                final_prefix = list(target[:i])
                final_prefix.append(found_char)
                for char in final_prefix:
                    final_counts[char] -= 2
                
                # Fill the rest of the prefix with smallest available
                for j in range(i + 1, half_len):
                    for c in sorted(final_counts.keys()):
                        if final_counts[c] >= 2:
                            final_prefix.append(c)
                            final_counts[c] -= 2
                            break
                
                mid = ""
                if n % 2 == 1:
                    for c in sorted(final_counts.keys()):
                        if final_counts[c] % 2 != 0:
                            mid = c
                            break
                
                res_str = "".join(final_prefix) + mid + "".join(final_prefix[::-1])
                return res_str
        
        # If we are at the middle char (only if n is odd and i == half_len)
        # This part is actually handled by the match_idx logic above.
        # Let's adjust the loop to handle the middle char case.
        
        # If i == half_len and n is odd, we check if we can pick a mid_char > target[half_len]
        if i == half_len and n % 2 == 1:
            # This case is only reachable if match_idx was half_len
            # and we are looking for a mid_char > target[half_len]
            # But the loop goes from match_idx down to 0.
            # If match_idx == half_len, i starts at half_len.
            t_char = target[half_len]
            found_mid = None
            for c in sorted(current_counts.keys()):
                if c > t_char and current_counts[c] % 2 != 0:
                    found_mid = c
                    break
            if found_mid:
                res_prefix = list(target[:half_len])
                return "".join(res_prefix) + found_mid + "".join(res_prefix[::-1])

        # If we can't find a char at this i, we "remove" target[i] from the prefix
        # and try the next i.
        if i > 0:
            char_to_remove = target[i-1]
            current_counts[char_to_remove] += 2
        else:
            break
            
    return ""