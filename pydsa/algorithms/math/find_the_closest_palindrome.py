METADATA = {
    "id": 564,
    "name": "Find the Closest Palindrome",
    "slug": "find-the-closest-palindrome",
    "category": "String",
    "aliases": [],
    "tags": ["string", "math"],
    "difficulty": "hard",
    "time_complexity": "O(L)",
    "space_complexity": "O(L)",
    "description": "Find the closest integer (excluding itself) to a given number that is a palindrome.",
}

def solve(n: str) -> str:
    """
    Finds the closest palindrome to a given string representation of a number.

    The algorithm generates potential candidates by taking the first half of the 
    number and creating palindromes by:
    1. Keeping the prefix as is.
    2. Incrementing the prefix by 1.
    3. Decrementing the prefix by 1.
    Additionally, it considers edge cases like 10^k - 1 (e.g., 999) and 10^k + 1 (e.g., 1001).

    Args:
        n: A string representing the input integer.

    Returns:
        A string representing the closest palindrome.

    Examples:
        >>> solve("123")
        "121"
        >>> solve("1")
        "0"
        >>> solve("10")
        "9"
    """
    length = len(n)
    # Edge case: single digit numbers
    if length == 1:
        return str(int(n) - 1)

    candidates = set()
    
    # Case 1: The "99...9" case (e.g., n=100 -> 99)
    candidates.add(str(10**(length - 1) - 1))
    # Case 2: The "10...01" case (e.g., n=99 -> 101)
    candidates.add(str(10**length + 1))

    # Extract the prefix (first half, including middle digit if length is odd)
    prefix_len = (length + 1) // 2
    prefix_val = int(n[:prefix_len])

    # Case 3: Generate palindromes by modifying the prefix (prefix, prefix+1, prefix-1)
    for i in [-1, 0, 1]:
        new_prefix = str(prefix_val + i)
        
        # Construct the palindrome based on whether original length was even or odd
        if length % 2 == 0:
            # Even length: prefix + reversed prefix
            palindrome = new_prefix + new_prefix[::-1]
        else:
            # Odd length: prefix + reversed prefix (excluding the middle digit)
            palindrome = new_prefix + new_prefix[:-1][::-1]
        
        candidates.add(palindrome)

    # Remove the original number from candidates as per problem constraints
    if n in candidates:
        candidates.remove(n)

    target = int(n)
    closest_val = -1
    min_diff = float('inf')

    # Sort candidates to handle the "smallest number" tie-break rule easily
    # We iterate through sorted candidates to find the one with the minimum absolute difference
    for cand_str in sorted(candidates, key=int):
        cand_int = int(cand_str)
        diff = abs(cand_int - target)
        
        if diff < min_diff:
            min_diff = diff
            closest_val = cand_int

    return str(closest_val)
