METADATA = {
    "id": 2100,
    "name": "Find Good Days to Rob the Bank",
    "slug": "find-good-days-to-rob-the-bank",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all indices in an array where the value is greater than or equal to all preceding values and all succeeding values.",
}

def solve(money: list[int]) -> list[int]:
    """
    Finds all indices where the amount of money is a 'good day' to rob the bank.
    A day is good if it is not strictly less than any day before it and not 
    strictly less than any day after it.

    Args:
        money: A list of integers representing the amount of money available each day.

    Returns:
        A list of indices representing the good days.

    Examples:
        >>> solve([5, 3, 4, 3, 1])
        [0]
        >>> solve([1, 2, 3, 4, 5])
        [4]
        >>> solve([5, 4, 3, 2, 1])
        [0]
        >>> solve([1, 1, 1, 1, 1])
        [0, 1, 2, 3, 4]
    """
    n = len(money)
    if n == 0:
        return []
    if n == 1:
        return [0]

    # left_max[i] stores the maximum value encountered from index 0 to i-1
    left_max = [0] * n
    current_max = float('-inf')
    for i in range(n):
        left_max[i] = current_max
        if money[i] > current_max:
            current_max = money[i]

    # right_max[i] stores the maximum value encountered from index i+1 to n-1
    right_max = [0] * n
    current_max = float('-inf')
    for i in range(n - 1, -1, -1):
        right_max[i] = current_max
        if money[i] > current_max:
            current_max = money[i]

    good_days = []
    # A day is good if money[i] >= max(all elements to the left) 
    # AND money[i] >= max(all elements to the right)
    for i in range(n):
        if money[i] >= left_max[i] and money[i] >= right_max[i]:
            good_days.append(i)

    return good_days
