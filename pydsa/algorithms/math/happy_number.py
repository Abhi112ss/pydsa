METADATA = {
    "id": 202,
    "name": "Happy Number",
    "slug": "happy_number",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_set", "two_pointer", "math"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Determine if a number is happy by detecting cycles in the sum-of-squared-digits sequence.",
}


def solve(n: int) -> bool:
    """Determine if a number is a happy number.

    A happy number is defined by the following process:
    Starting with any positive integer, replace the number by the sum of the
    squares of its digits, and repeat the process until the number equals 1
    (where it will stay), or it loops endlessly in a cycle which does not
    include 1.

    Args:
        n: A positive integer to check for happiness.

    Returns:
        True if n is a happy number, False otherwise.

    Examples:
        >>> solve(19)
        True
        >>> solve(2)
        False
        >>> solve(1)
        True
    """
    def get_next_number(num: int) -> int:
        """Compute the sum of the squares of the digits of num."""
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    # Floyd's cycle-finding algorithm (tortoise and hare)
    slow = n
    fast = get_next_number(n)

    # If there's a cycle, slow and fast will eventually meet
    while fast != 1 and slow != fast:
        slow = get_next_number(slow)          # Move one step
        fast = get_next_number(get_next_number(fast))  # Move two steps

    return fast == 1