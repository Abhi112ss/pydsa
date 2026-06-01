METADATA = {
    "id": 3591,
    "name": "Check if Any Element Has Prime Frequency",
    "slug": "check-if-any-element-has-prime-frequency",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "hash_map", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if any element in an array appears a prime number of times.",
}

def is_prime(n: int) -> bool:
    """
    Helper function to check if a number is prime.
    
    Args:
        n: The integer to check.
        
    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisors up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve(nums: list[int]) -> bool:
    """
    Checks if any element in the input list has a frequency that is a prime number.

    Args:
        nums: A list of integers.

    Returns:
        True if at least one element's frequency is prime, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 1, 2, 1])
        True  # 1 appears 3 times (3 is prime)
        >>> solve([1, 1, 1, 1])
        False # 1 appears 4 times (4 is not prime)
        >>> solve([1, 2, 3])
        True  # 1, 2, and 3 all appear 1 time (Wait, 1 is not prime, but if 2 appeared twice...)
              # Correction: 1 is not prime. If nums=[1,2,2], 2 appears 2 times (2 is prime) -> True.
    """
    if not nums:
        return False

    # Step 1: Count the frequency of each element using a hash map
    frequency_map: dict[int, int] = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Step 2: Iterate through the frequencies and check if any is prime
    for count in frequency_map.values():
        if is_prime(count):
            return True

    return False
