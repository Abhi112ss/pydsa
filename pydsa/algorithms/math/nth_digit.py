METADATA = {
    "id": 400,
    "name": "Nth Digit",
    "slug": "nth-digit",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the nth digit of the infinite integer sequence.",
}

def solve(n: int) -> int:
    """
    Finds the nth digit of the infinite integer sequence (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...).

    The algorithm works by:
    1. Determining how many digits the number containing the nth digit has (1-digit, 2-digits, etc.).
    2. Finding the actual number that contains the nth digit.
    3. Extracting the specific digit from that number.

    Args:
        n: The 1-indexed position of the digit to find.

    Returns:
        The digit at the nth position.

    Examples:
        >>> solve(3)
        3
        >>> solve(11)
        0
        >>> solve(15)
        2
    """
    # length: number of digits in the current group of numbers (1, 2, 3...)
    # count: how many numbers exist in the current group (9, 90, 900...)
    # start: the first number in the current group (1, 10, 100...)
    length = 1
    count = 9
    start = 1

    # Step 1: Identify the digit-length group where the nth digit resides
    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10

    # Step 2: Find the actual number that contains the nth digit
    # (n - 1) is used because we are looking for the offset from the 'start' number
    target_number = start + (n - 1) // length

    # Step 3: Find the specific digit within the target_number
    # Convert to string to easily index the digit, or use math
    # Using math to keep space complexity O(1)
    digit_index_in_number = (n - 1) % length
    
    # Convert number to string to extract the digit at the specific index
    # While string conversion is O(log(target_number)), it is effectively O(1) 
    # relative to the input n in terms of complexity classes for this problem.
    s = str(target_number)
    return int(s[digit_index_in_number])
