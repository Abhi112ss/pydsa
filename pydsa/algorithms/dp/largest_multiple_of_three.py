METADATA = {
    "id": 1363,
    "name": "Largest Multiple of Three",
    "slug": "largest-multiple-of-three",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math", "dp"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the largest number that can be formed by a subset of digits such that the number is divisible by three.",
}

def solve(digits: list[int]) -> int:
    """
    Finds the largest number formed by a subset of digits that is divisible by three.

    Args:
        digits: A list of single-digit integers.

    Returns:
        The largest integer divisible by three, or 0 if no such number exists.

    Examples:
        >>> solve([8, 1, 9])
        981
        >>> solve([8, 6, 7, 1, 4, 5, 9])
        987654
        >>> solve([1])
        0
    """
    # Group digits by their remainder when divided by 3
    # remainders[0] stores digits with remainder 0
    # remainders[1] stores digits with remainder 1
    # remainders[2] stores digits with remainder 2
    remainders = [[], [], []]
    for digit in digits:
        remainders[digit % 3].append(digit)

    # Sort each group in descending order to pick largest digits first
    for i in range(3):
        remainders[i].sort(reverse=True)

    total_sum = sum(digits)
    
    # Case 1: Sum is already divisible by 3
    if total_sum % 3 == 0:
        result_digits = remainders[0] + remainders[1] + remainders[2]
    
    # Case 2: Sum % 3 == 1
    # We must either remove one digit from remainders[1] 
    # OR two digits from remainders[2] (since 2+2=4, 4%3=1)
    elif total_sum % 3 == 1:
        if len(remainders[1]) >= 1:
            # Remove the smallest digit with remainder 1
            result_digits = remainders[0] + remainders[1][1:] + remainders[2]
        elif len(remainders[2]) >= 2:
            # Remove the two smallest digits with remainder 2
            result_digits = remainders[0] + remainders[1] + remainders[2][:-2]
        else:
            result_digits = []

    # Case 3: Sum % 3 == 2
    # We must either remove one digit from remainders[2]
    # OR two digits from remainders[1] (since 1+1=2, 2%3=2)
    else:
        if len(remainders[2]) >= 1:
            # Remove the smallest digit with remainder 2
            result_digits = remainders[0] + remainders[1] + remainders[2][1:]
        elif len(remainders[1]) >= 2:
            # Remove the two smallest digits with remainder 1
            result_digits = remainders[0] + remainders[1][:-2] + remainders[2]
        else:
            result_digits = []

    if not result_digits:
        return 0

    # Sort all selected digits descending to form the largest number
    result_digits.sort(reverse=True)
    
    # Convert list of digits to a single integer
    # Handle leading zero case (e.g., [0, 0] -> 0)
    if result_digits[0] == 0:
        return 0
        
    res_str = "".join(map(str, result_digits))
    return int(res_str)
