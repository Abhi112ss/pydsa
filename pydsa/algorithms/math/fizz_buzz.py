METADATA = {
    "id": 412,
    "name": "Fizz Buzz",
    "slug": "fizz_buzz",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "string", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return a list of strings representing numbers 1 to n, replacing multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'.",
}


def solve(n: int) -> list[str]:
    """Generate the Fizz Buzz sequence from 1 to n.

    For each integer i from 1 to n:
    - If i is divisible by both 3 and 5, append "FizzBuzz".
    - If i is divisible by 3 only, append "Fizz".
    - If i is divisible by 5 only, append "Buzz".
    - Otherwise, append the string representation of i.

    Args:
        n: A positive integer representing the upper bound of the sequence.

    Returns:
        A list of strings representing the Fizz Buzz sequence from 1 to n.

    Examples:
        >>> solve(3)
        ['1', '2', 'Fizz']
        >>> solve(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
        >>> solve(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    """
    result: list[str] = []

    for current in range(1, n + 1):
        # Check divisibility by both 3 and 5 first (LCM = 15) to avoid missing "FizzBuzz"
        if current % 15 == 0:
            result.append("FizzBuzz")
        elif current % 3 == 0:
            result.append("Fizz")
        elif current % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(current))

    return result