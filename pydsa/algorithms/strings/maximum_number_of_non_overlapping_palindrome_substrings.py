METADATA = {
    "id": 2472,
    "name": "Maximum Number of Non-overlapping Palindrome Substrings",
    "slug": "maximum-number-of-non-overlapping-palindrome-substrings",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "manacher", "string", "palindrome"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of non-overlapping palindromic substrings of length at least k.",
}

def solve(s: str, k: int) -> int:
    """
    Finds the maximum number of non-overlapping palindromic substrings of length at least k.

    The algorithm uses Manacher's algorithm to find the radius of the largest palindrome 
    centered at each position in O(n) time. Then, it uses a greedy approach to pick 
    the palindrome that ends earliest to maximize the total count.

    Args:
        s: The input string.
        k: The minimum length required for each palindrome.

    Returns:
        The maximum number of non-overlapping palindromic substrings of length at least k.

    Examples:
        >>> solve("abacaba", 3)
        2
        >>> solve("abacaba", 4)
        1
    """
    n = len(s)
    if k > n:
        return 0

    # Transform string to handle even and odd palindromes uniformly
    # e.g., "aba" -> "#a#b#a#"
    t = "#" + "#".join(s) + "#"
    m = len(t)
    p = [0] * m
    center = 0
    right = 0

    # Manacher's Algorithm to find palindrome radii in O(n)
    for i in range(m):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])
        
        while (i + p[i] + 1 < m and i - p[i] - 1 >= 0 and 
               t[i + p[i] + 1] == t[i - p[i] - 1]):
            p[i] += 1
            
        if i + p[i] > right:
            center = i
            right = i + p[i]

    # Greedy approach: Find the palindrome that ends earliest
    # We iterate through the string and keep track of the last end position
    count = 0
    last_end = -1
    
    # We iterate through the transformed string indices
    # A palindrome in 't' with radius p[i] corresponds to a palindrome 
    # in 's' of length p[i].
    # The actual start/end in 's' can be derived from 't' indices.
    
    # To optimize, we can pre-calculate the earliest end for each possible start.
    # However, a simpler greedy approach is to iterate through possible end positions.
    # Since we want the earliest end, we can check every center i.
    
    # We use a min-heap or a simple array to store the earliest end position 
    # for each possible start position to make the greedy choice.
    # But since we only care about length >= k, we can check centers.
    
    # earliest_end[i] = the smallest end index of a palindrome of length >= k starting at or after i
    # Actually, a simpler way: iterate through all possible end positions 'r' from 0 to n-1.
    # For each 'r', find the largest 'l' such that s[l:r+1] is a palindrome and r-l+1 >= k.
    # If such 'l' exists and l > last_end, increment count and update last_end.
    
    # To do this efficiently, we pre-calculate for each end position 'r', 
    # the largest 'l' such that s[l:r+1] is a palindrome of length >= k.
    
    best_start_for_end = [-1] * n
    for i in range(m):
        radius = p[i]
        if radius < k:
            continue
            
        # The palindrome in 't' centered at i has length 'radius'.
        # In 's', this corresponds to a palindrome of length 'radius'.
        # We want to find the smallest possible length >= k that is still a palindrome.
        # Actually, any palindrome of length L > k contains a palindrome of length L-2 
        # with the same center. We only care about the smallest palindrome >= k 
        # to satisfy the greedy "earliest end" property.
        
        # The length of the palindrome in 's' is 'radius'.
        # The range in 's' is:
        # start = (i - radius) // 2
        # end = (i + radius - 2) // 2
        
        # However, a center might support multiple palindromes of length >= k.
        # To satisfy greedy, we want the one that ends earliest.
        # For a fixed center, the one that ends earliest is the one with the smallest 
        # length L such that L >= k and L has the same parity as 'radius'.
        
        # Smallest length L >= k with same parity as radius:
        # If radius is 5 and k is 3, L could be 3 or 5. 3 is better.
        # But wait, the parity in 't' is fixed by the center.
        # If center is at a character (odd index in t), radius is odd.
        # If center is at '#', radius is even.
        
        # Let's find the smallest L >= k such that L has same parity as radius.
        # L = k if k % 2 == radius % 2 else k + 1
        # But we must ensure L <= radius.
        
        # Correct logic: For each center i, the smallest palindrome length L >= k 
        # that can be formed is:
        # if radius >= k:
        #    actual_L = k if (radius % 2 == k % 2) else k + 1
        #    Wait, this is only true if we can shrink the palindrome.
        #    In Manacher, if radius is R, we can form palindromes of length R, R-2, R-4...
        #    So we need the smallest L in {R, R-2, ...} such that L >= k.
        
        # Let's find the smallest L >= k with same parity as radius:
        # If radius >= k:
        #    L = k if (radius - k) % 2 == 0 else k + 1
        #    If L <= radius:
        #        start = (i - L) // 2
        #        end = (i + L - 2) // 2
        #        We want to map this to the end position.
        
        # Let's re-calculate start and end for the smallest valid L:
        # The center in 't' is i. The radius is p[i].
        # The palindrome in 's' has length 'radius'.
        # The characters in 's' are at indices:
        # (i - radius)//2  to  (i + radius - 2)//2
        
        # Let's use the property: a palindrome of length L centered at i in 't'
        # ends at index (i + L - 2) // 2 in 's'.
        
        # We want to find the smallest L >= k such that L <= p[i] and L % 2 == p[i] % 2.
        # Wait, the parity of L must match the parity of the center type.
        # If i is even (t[i] == '#'), L must be even.
        # If i is odd (t[i] != '#'), L must be odd.
        # This is exactly what p[i] % 2 tells us.
        
        # Smallest L >= k with same parity as p[i]:
        # if p[i] < k: continue
        # L = k if (p[i] % 2 == k % 2) else k + 1
        # This L is the smallest length >= k with the same parity as p[i].
        # Since p[i] is the maximum radius, any L <= p[i] with same parity is also a palindrome.
        
        # Let's find the end index in 's' for this L:
        # end_in_s = (i + L - 2) // 2
        # start_in_s = (i - L) // 2
        
        # We want to find for each end_in_s, the largest start_in_s.
        # Actually, we just need to know if any palindrome ends at 'r' and starts after 'last_end'.
        
        # Let's simplify:
        # For each center i, if p[i] >= k:
        #   Find smallest L >= k with same parity as p[i].
        #   L = k if (p[i] % 2 == k % 2) else k + 1
        #   start = (i - L) // 2
        #   end = (i + L - 2) // 2
        #   We want to pick the palindrome that ends earliest.
        #   We can store these (end, start) pairs and sort them by end.
        
        # But we can just use an array `min_start_for_end[end] = max_start`
        # and then iterate through end from 0 to n-1.
        
        # Let's refine the L calculation:
        # The parity of the length L is determined by whether the center i is at a char or '#'.
        # If i is odd, t[i] is a char, so L must be odd.
        # If i is even, t[i] is '#', so L must be even.
        # This is exactly p[i] % 2.
        
        # Wait, if k=3 and p[i]=4 (even), the smallest L >= 3 with same parity as 4 is 4.
        # If k=3 and p[i]=5 (odd), the smallest L >= 3 with same parity as 5 is 3.
        
        # Let's use a simpler approach:
        # For each center i, if p[i] >= k:
        #   L = k if (p[i] % 2 == k % 2) else k + 1
        #   # This L is the smallest length >= k with the same parity as p[i].
        #   # But we need to be careful: if p[i] is 4 and k is 3, L=4.
        #   # If p[i] is 5 and k is 3, L=3.
        #   # This L is always <= p[i] because if p[i] >= k, then 
        #   # either p[i] == k or p[i] == k+1 (if parities differ).
        #   # If p[i] >= k+1, then L <= k+1 <= p[i].
        #   # If p[i] == k, then L = k <= p[i].
        
        # Let's re-verify:
        # If p[i] = 4, k = 3. Parity of p[i] is 0, parity of k is 1.
        # L = k + 1 = 4. L <= p[i] is 4 <= 4 (True).
        # If p[i] = 5, k = 3. Parity of p[i] is 1, parity of k is 1.
        # L = k = 3. L <= p[i] is 3 <= 5 (True).
        
        # So:
        # L = k if (p[i] % 2 == k % 2) else k + 1
        # start = (i - L) // 2
        # end = (i + L - 2) // 2
        # This (start, end) is the "earliest ending" palindrome for this center.
        
        # We can collect all such (end, start) and sort by end.
        pass

    # Re-implementing the greedy part clearly:
    palindromes = []
    for i in range(m):
        if p[i] >= k:
            # Smallest L >= k with same parity as p[i]
            L = k if (p[i] % 2 == k % 2) else k + 1
            # The center i in 't' corresponds to a palindrome in 's'
            # The range in 't' is [i - L, i + L] (not quite, radius is L)
            # In 't', the palindrome is t[i-L : i+L+1]
            # The length in 't' is 2*L + 1.
            # The number of non-'#' characters is L.
            # The start index in 's' is (i - L) // 2
            # The end index in 's' is (i + L - 2) // 2
            # Example: s="aba", k=3. t="#a#b#a#", m=7.
            # i=3 (char 'b'), p[3]=3. k=3. L=3.
            # start = (3-3)//2 = 0. end = (3+3-2)//2 = 2. s[0:3] is "aba". Correct.
            # Example: s="aa", k=2. t="#a#a#", m=5.
            # i=2 (char '#'), p[2]=2. k=2. L=2.
            # start = (2-2)//2 = 0. end = (2+2-2)//2 = 1. s[0:2] is "aa". Correct.
            
            start = (i - L) // 2
            end = (i + L - 2) // 2
            palindromes.append((end, start))

    # Sort by end position to pick the one that ends earliest
    palindromes.sort()

    count = 0
    last_end = -1
    for end, start in palindromes:
        if start > last_end:
            count += 1
            last_end = end
            
    return count
