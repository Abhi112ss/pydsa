METADATA = {
    "id": 1015,
    "name": "Smallest Integer Divisible by K",
    "slug": "smallest-integer-divisible-by-k",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "pigeonhole_principle"],
    "difficulty": "medium",
    "time_complexity": "O(k)",
    "space_complexity": "O(1)",
    "description": "Find the smallest positive integer consisting only of ones that is divisible by k.",
}

def solve(k: int) -> str:
    """
    Finds the smallest positive integer consisting only of ones that is divisible by k.

    The problem asks for a number like 1, 11, 111, ... that is divisible by k.
    We can build this number digit by digit and track the remainder modulo k.
    Using the property (a * 10 + b) % k = ((a % k) * 10 + b) % k, we can avoid
    handling extremely large integers directly during the calculation.

    Args:
        k: The divisor integer.

    Returns:
        A string representing the smallest integer consisting only of ones 
        that is divisible by k.

    Examples:
        >>> solve(3)
        '111'
        >>> solve(1)
        '1'
        >>> solve(6)
        ''
    """
    # current_remainder tracks (11...1) % k
    current_remainder = 0
    # result_digits stores the count of '1's used so far
    result_digits = 0
    
    # We use a set to detect cycles, but since we only care about 
    # reaching remainder 0, and the number of possible remainders is k,
    # we can simply limit the loop to k iterations (Pigeonhole Principle).
    # If we don't hit 0 within k steps, we will enter a cycle that doesn't include 0.
    for i in range(1, k + 1):
        # Append a '1' to the current number: (prev_num * 10 + 1) % k
        current_remainder = (current_remainder * 10 + 1) % k
        result_digits += 1
        
        # If remainder is 0, we found the smallest number
        if current_remainder == 0:
            return "1" * result_digits
            
    # If we loop k times without hitting 0, no such number exists
    return ""
