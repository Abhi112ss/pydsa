METADATA = {
    "id": 2930,
    "name": "Number of Strings Which Can Be Rearranged to Contain Substring",
    "slug": "number-of-strings-which-can-be-rearranged-to-contain-substring",
    "category": "math",
    "aliases": [],
    "tags": ["combinatorics", "math", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of strings of length n that can be rearranged to contain a specific substring of length m.",
}

def solve(n: int, m: int, required_chars: list[str]) -> int:
    """
    Args:
        n: The length of the strings to be formed.
        m: The length of the required substring.
        required_chars: A list of characters that must appear in the string at least m times.

    Returns:
        The number of strings modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    num_required = len(required_chars)
    num_other = 26 - num_required

    def power(base: int, exponent: int) -> int:
        result = 1
        base %= MODULUS
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % MODULUS
            base = (base * base) % MODULUS
            exponent //= 2
        return result

    def inverse(a: int) -> int:
        return power(a, MODULUS - 2)

    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MODULUS
    
    inv_fact[n] = inverse(fact[n])
    for i in range(n - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MODULUS

    def nCr(n_val: int, r_val: int) -> int:
        if r_val < 0 or r_val > n_val:
            return 0
        num = fact[n_val]
        den = (inv_fact[r_val] * inv_fact[n_val - r_val]) % MODULUS
        return (num * den) % MODULUS

    total_strings = power(26, n)
    invalid_strings = 0

    for k in range(m):
        ways_to_choose_positions = nCr(n, k)
        ways_to_fill_required = power(num_required, k)
        ways_to_fill_others = power(num_other, n - k)
        
        term = (ways_to_choose_positions * ways_to_fill_required) % MODULUS
        term = (term * ways_to_fill_others) % MODULUS
        invalid_strings = (invalid_strings + term) % MODULUS

    return (total_strings - invalid_strings + MODULUS) % MODULUS