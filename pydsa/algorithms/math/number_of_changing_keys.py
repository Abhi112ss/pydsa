METADATA = {
    "id": 3019,
    "name": "Number of Changing Keys",
    "slug": "number-of-changing-keys",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of possible sequences of length n using k keys where adjacent keys must be different, modulo 10^9 + 7.",
}

def solve(n: int, k: int) -> int:
    """
    Calculates the number of possible sequences of length n using k keys
    where no two adjacent keys are the same.

    The logic follows:
    - For the first position, there are k choices.
    - For every subsequent position (from 2 to n), there are (k - 1) choices 
      because the key must be different from the one immediately preceding it.
    - Total sequences = k * (k - 1)^(n - 1)

    Args:
        n: The length of the sequence.
        k: The number of available keys.

    Returns:
        The total number of valid sequences modulo 10^9 + 7.

    Examples:
        >>> solve(2, 3)
        6
        >>> solve(3, 2)
        2
    """
    MODULO = 1_000_000_007

    if n == 0:
        return 0
    if n == 1:
        return k % MODULO

    # The first key has k choices.
    # Each of the remaining (n-1) keys has (k-1) choices.
    # We use pow(base, exp, mod) for efficient modular exponentiation.
    first_key_choices = k % MODULO
    remaining_choices = pow(k - 1, n - 1, MODULO)

    # Multiply the choices and apply modulo
    return (first_key_choices * remaining_choices) % MODULO
