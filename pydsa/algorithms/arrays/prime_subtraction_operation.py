METADATA = {
    "id": 2601,
    "name": "Prime Subtraction Operation",
    "slug": "prime-subtraction-operation",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math", "prime_numbers"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 * sqrt(max_diff))",
    "space_complexity": "O(1)",
    "description": "Maximize the sum of differences between pairs of elements by subtracting a prime number from one element in each pair.",
}

def is_prime(n: int) -> bool:
    """Checks if a number is prime."""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_largest_prime_le(n: int) -> int:
    """Finds the largest prime number less than or equal to n."""
    for candidate in range(n, 1, -1):
        if is_prime(candidate):
            return candidate
    return 0

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum possible sum of differences by choosing a prime 
    to subtract from one element in each pair (nums[i], nums[j]).

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of differences.

    Examples:
        >>> solve([4, 5, 10])
        11
        >>> solve([1, 2, 3, 4])
        6
    """
    n = len(nums)
    total_sum = 0

    # Iterate through every unique pair (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            # Case 1: nums[i] - nums[j]
            # We want to find the largest prime p <= nums[i] - nums[j]
            # If nums[i] - nums[j] is negative, no prime can be subtracted to increase it
            diff1 = nums[i] - nums[j]
            val1 = 0
            if diff1 > 0:
                p1 = get_largest_prime_le(diff1)
                val1 = diff1 - p1
            
            # Case 2: nums[j] - nums[i]
            # We want to find the largest prime p <= nums[j] - nums[i]
            diff2 = nums[j] - nums[i]
            val2 = 0
            if diff2 > 0:
                p2 = get_largest_prime_le(diff2)
                val2 = diff2 - p2
            
            # Greedy choice: For each pair, pick the operation that yields the maximum difference
            total_sum += max(val1, val2)

    return total_sum
