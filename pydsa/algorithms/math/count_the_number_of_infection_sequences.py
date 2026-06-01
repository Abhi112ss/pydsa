METADATA = {
    "id": 2954,
    "name": "Count the Number of Infection Sequences",
    "slug": "count-the-number-of-infection-sequences",
    "category": "Math",
    "aliases": [],
    "tags": ["combinatorics", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total number of ways to infect all healthy people given initial infection sources and constraints.",
}

def solve(infected: list[int], healthy: list[int], mod: int) -> int:
    """
    Calculates the number of valid infection sequences using combinatorics.

    The problem can be viewed as arranging the infection events of different 
    independent groups. Each group of healthy people trapped between two 
    infected people can be infected in any order, but people at the ends 
    of the array (one-sided boundaries) have more freedom.

    Args:
        infected: A list of indices of initially infected people.
        healthy: A list of indices of healthy people.
        mod: The modulo value.

    Returns:
        The total number of valid infection sequences modulo `mod`.

    Examples:
        >>> solve([1, 3], [2], 10**9 + 7)
        1
        >>> solve([1, 3], [2, 4], 10**9 + 7)
        2
    """
    n = len(healthy)
    if n == 0:
        return 1

    # Precompute factorials and their modular inverses for combinations
    fact = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % mod

    # Modular exponentiation for Fermat's Little Theorem (assuming mod is prime)
    # If mod is not prime, we'd need a different approach, but LeetCode 
    # problems usually provide a prime mod for these types of problems.
    inv[n] = pow(fact[n], mod - 2, mod)
    for i in range(n - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % mod

    def nCr(n_val: int, r_val: int) -> int:
        if r_val < 0 or r_val > n_val:
            return 0
        num = fact[n_val]
        den = (inv[r_val] * inv[n_val - r_val]) % mod
        return (num * den) % mod

    infected.sort()
    healthy.sort()

    # Identify groups of healthy people between infected people
    # and those at the boundaries.
    groups = []
    
    # 1. Left boundary group (one-sided)
    left_idx = 0
    while left_idx < n and healthy[left_idx] < infected[0]:
        left_idx += 1
    if left_idx > 0:
        groups.append({"size": left_idx, "type": "one_sided"})

    # 2. Middle groups (two-sided)
    current_healthy_ptr = left_idx
    for i in range(len(infected) - 1):
        start = infected[i]
        end = infected[i + 1]
        count = 0
        while current_healthy_ptr < n and healthy[current_healthy_ptr] < end:
            count += 1
            current_healthy_ptr += 1
        if count > 0:
            groups.append({"size": count, "type": "two_sided"})

    # 3. Right boundary group (one-sided)
    right_count = n - current_healthy_ptr
    if right_count > 0:
        groups.append({"size": right_count, "type": "one_sided"})

    # Total ways = (Total Permutations of all healthy) / (Internal constraints)
    # We use the multinomial coefficient logic:
    # Total ways = (N!) / (size1! * size2! * ...) * (Product of ways within each group)
    
    # Start with the multinomial coefficient: N! / (s1! * s2! * ...)
    ans = fact[n]
    for g in groups:
        ans = (ans * inv[g["size"]]) % mod

    # Multiply by the internal ways for each group
    for g in groups:
        if g["type"] == "two_sided":
            # For a group of size k between two infected, 
            # there are 2^(k-1) ways to pick which side gets infected next.
            # However, the standard formula for two-sided is 2^(size-1).
            # Wait, the logic is: in each step except the last, we have 2 choices.
            # So 2^(size-1) ways.
            ways = pow(2, g["size"] - 1, mod)
            ans = (ans * ways) % mod
        else:
            # One-sided groups have only 1 way to be ordered (must go outward)
            # Actually, they can be infected in any order, but they are 
            # effectively "one-sided" in terms of choice. 
            # But the multinomial already accounts for their positions.
            # For one-sided, there is only 1 way to pick the 'next' person 
            # if we consider the sequence of infection.
            # Actually, for one-sided, the number of ways is 1.
            pass

    return ans % mod
