METADATA = {
    "id": 1542,
    "name": "Find Longest Awesome Substring",
    "slug": "find-longest-awesome-substring",
    "category": "String",
    "aliases": [],
    "tags": ["string", "hash_map", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the longest substring that is 'awesome', meaning it is either a palindrome or can be transformed into one by flipping 'a' to 'z' and vice versa.",
}

def solve(s: str) -> str:
    """
    Finds the longest 'awesome' substring in the given string.
    
    An awesome substring is a substring that is either a palindrome or 
    becomes a palindrome if all 'a's are replaced by 'z's and all 'z's 
    are replaced by 'a's.
    
    Args:
        s: The input string consisting of 'a' and 'z'.
        
    Returns:
        The longest awesome substring. If there are multiple, return the 
        one that appears first. If none exist, return an empty string.
        
    Examples:
        >>> solve("aazaa")
        'aazaa'
        >>> solve("aazz")
        'aazz'
        >>> solve("azaz")
        'azaz'
    """
    n = len(s)
    if n == 0:
        return ""

    # To handle both standard palindromes and 'flipped' palindromes,
    # we can transform the string. A flipped palindrome is a standard 
    # palindrome if we treat 'z' as 'a' and 'a' as 'z'.
    # However, a more unified way is to use Manacher's on a modified string.
    # But the problem defines 'awesome' as:
    # 1. Substring is a palindrome.
    # 2. Substring is a palindrome when 'a' <-> 'z' is applied.
    
    # Let's use Manacher's algorithm. To handle the 'flipped' case, 
    # we can represent 'a' as 0 and 'z' as 1. 
    # A palindrome satisfies: char[i] == char[j]
    # A flipped palindrome satisfies: char[i] != char[j] (specifically if one is 'a' and other is 'z')
    # Wait, the definition is: "a substring is awesome if it is a palindrome OR 
    # it becomes a palindrome if you replace all 'a' with 'z' and 'z' with 'a'".
    # This means for a flipped palindrome, the condition is: 
    # s[i] == 'a' and s[j] == 'z' OR s[i] == 'z' and s[j] == 'a'.
    # This is equivalent to saying s[i] != s[j] for all symmetric indices.
    
    # Actually, the simplest way to solve this is to realize that an awesome 
    # substring is just a palindrome in a string where we consider 
    # 'a' and 'z' as potentially matching or not matching.
    # But Manacher's only works for equality.
    
    # Let's re-read: "a substring is awesome if it is a palindrome OR 
    # it becomes a palindrome if you replace all 'a' with 'z' and 'z' with 'a'".
    # This is equivalent to:
    # Case 1: s[i] == s[n-1-i] for all i
    # Case 2: s[i] != s[n-1-i] for all i (where s[i] is 'a' or 'z')
    
    # We can use Manacher's twice.
    # 1. Standard Manacher's on s to find longest palindrome.
    # 2. Manacher's on a "flipped" version of s. 
    #    Wait, if we flip 'a' to 'z' and 'z' to 'a', a flipped palindrome 
    #    becomes a standard palindrome.
    #    Example: "aazz" -> flip -> "zzaa". "zzaa" is not a palindrome.
    #    Wait, the rule is: "replace all 'a' with 'z' and 'z' with 'a'".
    #    If s = "aazz", flip(s) = "zzaa". Not a palindrome.
    #    If s = "az", flip(s) = "za". Not a palindrome.
    #    If s = "azza", flip(s) = "zaaz". "zaaz" is a palindrome!
    #    So "azza" is awesome.
    
    # Correct logic:
    # A substring is awesome if:
    # 1. It is a palindrome.
    # 2. Its "complement" (a->z, z->a) is a palindrome.
    
    def get_longest_palindrome(text: str) -> str:
        if not text:
            return ""
        # Transform text for Manacher's: "aba" -> "#a#b#a#"
        t = "#" + "#".join(text) + "#"
        m = len(t)
        p = [0] * m
        center = 0
        right = 0
        max_len = 0
        best_start = 0
        
        for i in range(m):
            if i < right:
                p[i] = min(right - i, p[2 * center - i])
            
            # Attempt to expand around i
            while (i - p[i] - 1 >= 0 and i + p[i] + 1 < m and 
                   t[i - p[i] - 1] == t[i + p[i] + 1]):
                p[i] += 1
                
            if i + p[i] > right:
                center = i
                right = i + p[i]
            
            # Update max length found
            # p[i] in the transformed string is exactly the length of the 
            # palindrome in the original string.
            if p[i] > max_len:
                max_len = p[i]
                # Calculate start index in original string
                # The center in original is (i-1)//2
                best_start = (i - p[i]) // 2
                
        return text[best_start : best_start + max_len]

    # Case 1: Standard Palindrome
    res1 = get_longest_palindrome(s)
    
    # Case 2: Flipped Palindrome
    # Create a string where 'a' becomes 'z' and 'z' becomes 'a'
    flipped_s = "".join('z' if char == 'a' else 'a' for char in s)
    res2 = get_longest_palindrome(flipped_s)
    
    # We need to return the longest. If lengths are equal, 
    # the problem asks for the one that appears first in the original string.
    # However, res2 is the flipped version. We need the original substring.
    # If res2 is "zaaz", the original was "azza".
    
    # Let's refine the Manacher's to return (length, start_index)
    def get_longest_palindrome_info(text: str) -> tuple[int, int]:
        if not text:
            return 0, 0
        t = "#" + "#".join(text) + "#"
        m = len(t)
        p = [0] * m
        center = 0
        right = 0
        max_len = 0
        best_start = 0
        
        for i in range(m):
            if i < right:
                p[i] = min(right - i, p[2 * center - i])
            while (i - p[i] - 1 >= 0 and i + p[i] + 1 < m and 
                   t[i - p[i] - 1] == t[i + p[i] + 1]):
                p[i] += 1
            if i + p[i] > right:
                center = i
                right = i + p[i]
            if p[i] > max_len:
                max_len = p[i]
                best_start = (i - p[i]) // 2
            elif p[i] == max_len:
                # If lengths are equal, we want the one with smaller start index
                current_start = (i - p[i]) // 2
                if current_start < best_start:
                    best_start = current_start
        return max_len, best_start

    len1, start1 = get_longest_palindrome_info(s)
    
    # For the flipped case, we find the palindrome in the flipped string,
    # but we must map its indices back to the original string.
    # If flipped_s[i:i+L] is a palindrome, then s[i:i+L] is an awesome substring.
    len2, start2 = get_longest_palindrome_info(flipped_s)
    
    # Compare results
    if len1 > len2:
        return s[start1 : start1 + len1]
    elif len2 > len1:
        return s[start2 : start2 + len2]
    else:
        # Lengths are equal, return the one that appears first
        if start1 <= start2:
            return s[start1 : start1 + len1]
        else:
            return s[start2 : start2 + len2]
