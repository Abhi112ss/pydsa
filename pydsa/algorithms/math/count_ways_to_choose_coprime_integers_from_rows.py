METADATA = {
    "id": 3725,
    "name": "Count Ways to Choose Coprime Integers from Rows",
    "slug": "count_ways_to_choose_coprime_integers_from_rows",
    "category": "math",
    "aliases": [],
    "tags": ["math", "combinatorics", "inclusion_exclusion"],
    "difficulty": "hard",
    "time_complexity": "O(rows * max_val * log(max_val))",
    "space_complexity": "O(max_val)",
    "description": "Counts the number of ways to pick one integer from each row such that the selected numbers are pairwise coprime.",
}

import sys
from collections import Counter

MOD = 10 ** 9 + 7

def solve() -> None:
    """
    Reads a matrix from standard input and prints the number of ways to choose
    exactly one integer from each row so that the chosen integers are coprime
    (their greatest common divisor equals 1). The result is given modulo 1e9+7.

    Input format:
        n m
        a_11 a_12 ... a_1m
        ...
        a_n1 a_n2 ... a_nm

    Args:
        None (input is read from stdin).

    Returns:
        None (the answer is printed to stdout).

    Example:
        Input:
            2 3
            2 3 4
            6 5 7
        Output:
            5
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    rows: list[Counter[int]] = []
    max_val = 0
    for _ in range(n):
        row_vals = [int(next(it)) for _ in range(m)]
        rows.append(Counter(row_vals))
        max_val = max(max_val, max(row_vals))

    # ---------- compute Möbius function up to max_val ----------
    mu = [1] * (max_val + 1)
    is_prime = [True] * (max_val + 1)
    primes: list[int] = []
    mu[0] = 0  # unused
    for i in range(2, max_val + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > max_val:
                break
            is_prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            else:
                mu[i * p] = -mu[i]
    # ---------- compute f(d) = product over rows of count of multiples of d ----------
    f = [0] * (max_val + 1)
    for d in range(1, max_val + 1):
        product = 1
        for row_counter in rows:
            cnt = 0
            # sum frequencies of numbers that are multiples of d
            for multiple in range(d, max_val + 1, d):
                cnt += row_counter.get(multiple, 0)
            if cnt == 0:
                product = 0
                break
            product = (product * cnt) % MOD
        f[d] = product

    # ---------- apply Möbius inversion to obtain answer ----------
    answer = 0
    for d in range(1, max_val + 1):
        if mu[d] == 0:
            continue
        answer = (answer + mu[d] * f[d]) % MOD

    print(answer % MOD)
