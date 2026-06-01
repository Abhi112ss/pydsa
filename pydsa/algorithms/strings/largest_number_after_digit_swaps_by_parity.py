METADATA = {
    "id": 2231,
    "name": "Largest Number After Digit Swaps by Parity",
    "slug": "largest-number-after-digit-swaps-by-parity",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Rearrange digits of a number such that even digits stay in even positions and odd digits stay in odd positions to form the largest possible number.",
}

def solve(num: int) -> int:
    """
    Rearranges the digits of a number to form the largest possible number,
    maintaining the parity of the digit's position.

    Args:
        num: The input integer.

    Returns:
        The largest possible integer formed by swapping digits of the same parity.

    Examples:
        >>> solve(5274)
        7452
        >>> solve(4321)
        4321
        >>> solve(1234)
        3412
    """
    # Convert number to a list of digits for easy manipulation
    digits = [int(d) for d in str(num)]
    n = len(digits)
    
    # Separate digits based on the parity of their index
    # Note: The problem defines parity based on the index (0-indexed or 1-indexed)
    # In LeetCode 2231, it refers to the parity of the index in the string representation.
    evens = []
    odds = []
    
    for i in range(n):
        if i % 2 == 0:
            evens.append(digits[i])
        else:
            odds.append(digits[i])
            
    # Sort both groups in descending order to ensure the largest digits 
    # appear as early as possible in their respective parity slots
    evens.sort(reverse=True)
    odds.sort(reverse=True)
    
    # Reconstruct the number by placing sorted digits back into their original parity positions
    result_digits = [0] * n
    even_ptr = 0
    odd_ptr = 0
    
    for i in range(n):
        if i % 2 == 0:
            result_digits[i] = evens[even_ptr]
            even_ptr += 1
        else:
            result_digits[i] = odds[odd_ptr]
            odd_ptr += 1
            
    # Convert the list of digits back into an integer
    result_str = "".join(map(str, result_digits))
    return int(result_str)
