METADATA = {
    "id": 2205,
    "name": "The Number of Users That Are Eligible for Discount",
    "slug": "the_number_of_users_that_are_eligible_for_discount",
    "category": "array",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count users whose discounted price is lower than the standard discounted price.",
}

import sys

def solve() -> None:
    """Read input, count eligible users, and print the result.

    Args:
        None (reads from standard input).

    Returns:
        None (writes the count to standard output).

    Example:
        Input:
            100 20 3
            90 10
            110 30
            80 25
        Output:
            2
    """
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return

    price = int(tokens[0])
    discount = int(tokens[1])
    user_count = int(tokens[2])

    eligible_users = 0
    index = 3
    for _ in range(user_count):
        user_price = int(tokens[index])
        user_discount = int(tokens[index + 1])
        index += 2
        # A user is eligible if user_price * discount < price * user_discount
        if user_price * discount < price * user_discount:
            eligible_users += 1

    print(eligible_users)