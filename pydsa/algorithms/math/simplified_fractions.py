METADATA = {
    "id": 1447,
    "name": "Simplified Fractions",
    "slug": "simplified-fractions",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "gcd", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 log n)",
    "space_complexity": "O(n^2)",
    "description": "Return all simplified fractions between 0 and 1 with denominator n.",
}

import math

def solve(n: int) -> list[str]:
    """
    Finds all simplified fractions between 0 and 1 with denominator n.
    
    A fraction i/j is simplified if the greatest common divisor (GCD) 
    of i and j is 1.

    Args:
        n: The denominator of the fractions.

    Returns:
        A list of strings representing the simplified fractions in lexicographical order.

    Examples:
        >>> solve(5)
        ['1/5', '2/5', '3/5', '4/5']
        >>> solve(2)
        ['1/2']
    """
    fractions: list[str] = []

    # Iterate through all possible numerators from 1 to n-1
    for numerator in range(1, n):
        # A fraction numerator/n is simplified if gcd(numerator, n) == 1
        if math.gcd(numerator, n) == 1:
            fractions.append(f"{numerator}/{n}")

    # The problem asks for lexicographical order. 
    # Since we iterate numerator from 1 to n-1, and the denominator is fixed,
    # the strings "1/n", "2/n", etc., are already in lexicographical order
    # if we consider the string representation. However, standard string 
    # sorting for "10/n" vs "2/n" might differ from numerical order.
    # But for a fixed denominator, the string "i/n" sorted lexicographically 
    # is actually what the problem expects.
    
    # Wait, the problem asks for lexicographical order of the strings.
    # Example n=5: "1/5", "2/5", "3/5", "4/5"
    # Example n=10: "1/10", "3/10", "7/10", "9/10"
    # Let's sort the resulting strings to ensure lexicographical order.
    fractions.sort()
    
    return fractions
