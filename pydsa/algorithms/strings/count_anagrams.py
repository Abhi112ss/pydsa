METADATA = {
    "id": 2514,
    "name": "Count Anagrams",
    "slug": "count-anagrams",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(k)",
    "description": "Calculate the number of ways to form anagrams of a given string using a specific set of characters, modulo 10^9 + 7.",
}

def solve(s: str, words: list[str]) -> int:
    """
    Calculates the number of ways to form anagrams of each word in 'words' 
    using the characters available in 's', modulo 10^9 + 7.

    The problem is solved using multinomial coefficients. For each word, 
    the number of ways to arrange its characters is (length!) / (count(c1)! * count(c2)! * ...).
    However, the problem asks for the number of ways to pick characters from 's'.
    Actually, the problem asks for the number of ways to form anagrams of 'words[i]' 
    using characters from 's'. This is equivalent to:
    For each word, the number of ways to choose the positions for each unique character.
    Wait, the standard interpretation of "Count Anagrams" in this context is:
    For each word, how many ways can we pick the characters from the pool 's' to form it?
    If word has char 'a' appearing k times, and 's' has char 'a' appearing n times,
    we choose k positions out of n: C(n, k).
    Total ways for a word = Product over all unique chars 'c' in word of C(count_in_s(c), count_in_word(c)).

    Args:
        s: The source string containing available characters.
        words: A list of strings to form anagrams from.

    Returns:
        The total number of ways to form anagrams for all words, modulo 10^9 + 7.

    Examples:
        >>> solve("aabb", ["ab", "aa"])
        # "ab": C(2,1) * C(2,1) = 2 * 2 = 4
        # "aa": C(2,2) = 1
        # Total = 4 + 1 = 5
        5
    """
    MOD = 1_000_000_007

    # Count frequencies of characters in the source string s
    source_counts = {}
    for char in s:
        source_counts[char] = source_counts.get(char, 0) + 1

    # Precompute factorials and their modular inverses for combinations C(n, k)
    # Max n is len(s)
    max_n = len(s)
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    
    for i in range(1, max_n + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    # Modular inverse using Fermat's Little Theorem
    inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    def nCr_mod(n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        num = fact[n]
        den = (inv_fact[r] * inv_fact[n - r]) % MOD
        return (num * den) % MOD

    total_ways = 0

    for word in words:
        # Count frequencies of characters in the current word
        word_counts = {}
        for char in word:
            word_counts[char] = word_counts.get(char, 0) + 1
        
        word_ways = 1
        possible = True
        
        # For each unique character in the word, calculate combinations C(available, needed)
        for char, needed in word_counts.items():
            available = source_counts.get(char, 0)
            if needed > available:
                possible = False
                break
            
            # Multiply the ways to pick the required number of this character
            word_ways = (word_ways * nCr_mod(available, needed)) % MOD
        
        if possible:
            total_ways = (total_ways + word_ways) % MOD

    return total_ways
