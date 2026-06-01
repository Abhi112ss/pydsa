METADATA = {
    "id": 1505,
    "name": "Minimum Possible Integer After at Most K Adjacent Swaps On Digits",
    "slug": "minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string", "implementation"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum possible integer by performing at most k adjacent swaps on the digits of a given string.",
}

def solve(number: str, k: int) -> str:
    """
    Finds the minimum possible integer by performing at most k adjacent swaps.

    The algorithm uses a greedy approach: for each position in the string, 
    it looks ahead up to k steps to find the smallest possible digit that 
    can be moved to the current position.

    Args:
        number: A string representing the initial integer.
        k: The maximum number of adjacent swaps allowed.

    Returns:
        A string representing the minimum possible integer after at most k swaps.

    Examples:
        >>> solve("4321", 4)
        '2431'
        >>> solve("1000", 1)
        '0100'
        >>> solve("1234", 10)
        '1234'
    """
    digits = list(number)
    n = len(digits)

    for i in range(n):
        if k <= 0:
            break

        # Find the index of the smallest digit within the reachable range [i, i + k]
        # We want the smallest digit to minimize the number at the current position.
        # If there are multiple identical smallest digits, we pick the leftmost one
        # to minimize the number of swaps used.
        best_digit_index = i
        limit = min(i + k, n - 1)
        
        for j in range(i + 1, limit + 1):
            if digits[j] < digits[best_digit_index]:
                best_digit_index = j
        
        # Calculate the cost to move the best digit found to the current position i
        swaps_needed = best_digit_index - i
        
        if swaps_needed > 0:
            # Perform the swaps by shifting elements to the right
            # This simulates the adjacent swaps required to bring digits[best_digit_index] to i
            target_digit = digits.pop(best_digit_index)
            digits.insert(i, target_digit)
            
            # Deduct the cost from our remaining budget k
            k -= swaps_needed

    return "".join(digits)
