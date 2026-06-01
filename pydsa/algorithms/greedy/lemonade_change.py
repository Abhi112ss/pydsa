METADATA = {
    "id": 860,
    "name": "Lemonade Change",
    "slug": "lemonade_change",
    "category": "greedy",
    "aliases": [],
    "tags": ["array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if correct change can be provided to each customer in order.",
}


def solve(bills: list[int]) -> bool:
    """Determine whether lemonade stand can give correct change to each customer.

    Args:
        bills: List of integers representing the bill each customer pays with.
                Each value is one of 5, 10, or 20.

    Returns:
        True if change can be given to every customer, False otherwise.

    Examples:
        >>> solve([5, 5, 5, 10, 20])
        True
        >>> solve([5, 5, 10, 10, 20])
        False
    """
    count_five = 0  # number of $5 bills on hand
    count_ten = 0   # number of $10 bills on hand

    for bill in bills:
        if bill == 5:
            count_five += 1
        elif bill == 10:
            # need $5 as change
            if count_five == 0:
                return False
            count_five -= 1
            count_ten += 1
        else:  # bill == 20
            # Prefer giving one $10 and one $5 as change
            if count_ten > 0 and count_five > 0:
                count_ten -= 1
                count_five -= 1
            elif count_five >= 3:
                count_five -= 3
            else:
                return False
    return True