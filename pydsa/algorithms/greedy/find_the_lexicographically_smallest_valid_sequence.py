METADATA = {
    "id": 3302,
    "name": "Find the Lexicographically Smallest Valid Sequence",
    "slug": "find-the-lexicographically-smallest-valid-sequence",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "stack", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct the lexicographically smallest sequence by greedily picking the smallest available character that allows for a valid completion using a monotonic stack approach.",
}

def solve(words: list[str], k: int) -> str:
    """
    Args:
        words: A list of strings representing the available characters.
        k: The required length of the sequence.

    Returns:
        The lexicographically smallest valid sequence of length k.
    """
    n = len(words)
    suffix_counts = [[0] * 26 for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for char_idx in range(26):
            suffix_counts[i][char_idx] = suffix_counts[i + 1][char_idx]
        for char in words[i]:
            suffix_counts[i][ord(char) - ord('a')] += 1

    result = []
    current_word_idx = 0
    current_char_idx = 0
    
    for _ in range(k):
        found = False
        for char_code in range(26):
            char = chr(ord('a') + char_code)
            
            needed_chars = k - len(result) - 1
            
            potential_word_idx = current_word_idx
            potential_char_idx = current_char_idx
            
            if potential_char_idx < len(words[potential_word_idx]) and words[potential_word_idx][potential_char_idx] == char:
                potential_char_idx += 1
                if potential_char_idx == len(words[potential_word_idx]):
                    potential_word_idx += 1
                    potential_char_idx = 0
            else:
                potential_word_idx += 1
                potential_char_idx = 0
            
            if potential_word_idx >= n:
                continue
                
            can_complete = True
            remaining_needed = needed_chars
            
            for c_idx in range(26):
                if suffix_counts[potential_word_idx][c_idx] < 0:
                    can_complete = False
                    break
            
            if not can_complete:
                continue

            available_total = 0
            for c_idx in range(26):
                available_total += suffix_counts[potential_word_idx][c_idx]
            
            if available_total < needed_chars:
                continue

            result.append(char)
            current_word_idx = potential_word_idx
            current_char_idx = potential_char_idx
            found = True
            break
            
        if not found:
            return ""

    return "".join(result)

def solve_optimized(words: list[str], k: int) -> str:
    """
    Args:
        words: A list of strings representing the available characters.
        k: The required length of the sequence.

    Returns:
        The lexicographically smallest valid sequence of length k.
    """
    n = len(words)
    suffix_counts = [[0] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(26):
            suffix_counts[i][j] = suffix_counts[i + 1][j]
        for char in words[i]:
            suffix_counts[i][ord(char) - ord('a')] += 1

    res = []
    curr_w = 0
    curr_c = 0

    for _ in range(k):
        found = False
        for char_val in range(26):
            char = chr(ord('a') + char_val)
            
            next_w, next_c = curr_w, curr_c
            if next_c < len(words[next_w]) and words[next_w][next_c] == char:
                next_c += 1
                if next_c == len(words[next_w]):
                    next_w += 1
                    next_c = 0
            else:
                next_w += 1
                next_c = 0
            
            if next_w < n:
                rem = k - len(res) - 1
                total_avail = sum(suffix_counts[next_w])
                if total_avail >= rem:
                    res.append(char)
                    curr_w, curr_c = next_w, next_c
                    found = True
                    break
            elif rem == 0:
                res.append(char)
                curr_w, curr_c = next_w, next_c
                found = True
                break
        
        if not found:
            return ""
            
    return "".join(res)

def solve(words: list[str], k: int) -> str:
    """
    Args:
        words: A list of strings representing the available characters.
        k: The required length of the sequence.

    Returns:
        The lexicographically smallest valid sequence of length k.
    """
    n = len(words)
    suffix_counts = [[0] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(26):
            suffix_counts[i][j] = suffix_counts[i + 1][j]
        for char in words[i]:
            suffix_counts[i][ord(char) - ord('a')] += 1

    res = []
    curr_w = 0
    curr_c = 0

    for _ in range(k):
        found = False
        for char_val in range(26):
            char = chr(ord('a') + char_val)
            
            next_w, next_c = curr_w, curr_c
            if next_c < len(words[next_w]) and words[next_w][next_c] == char:
                next_c += 1
                if next_c == len(words[next_w]):
                    next_w += 1
                    next_c = 0
            else:
                next_w += 1
                next_c = 0
            
            rem = k - len(res) - 1
            if rem == 0:
                if next_w <= n:
                    res.append(char)
                    curr_w, curr_c = next_w, next_c
                    found = True
                    break
            else:
                if next_w < n:
                    total_avail = 0
                    for count in suffix_counts[next_w]:
                        total_avail += count
                    if total_avail >= rem:
                        res.append(char)
                        curr_w, curr_c = next_w, next_c
                        found = True
                        break
        if not found:
            return ""
    return "".join(res)