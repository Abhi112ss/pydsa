METADATA = {
    "id": 248,
    "name": "Strobogrammatic Number III",
    "slug": "strobogrammatic-number-iii",
    "category": "Math",
    "aliases": [],
    "tags": ["recursion", "backtracking", "math"],
    "difficulty": "hard",
    "time_complexity": "O(5^(max_len/2))",
    "space_complexity": "O(5^(max_len/2))",
    "description": "Find the count of strobogrammatic numbers in the range [low, high].",
}

def solve(low: str, high: str) -> int:
    """
    Counts the number of strobogrammatic numbers in the range [low, high].

    A strobogrammatic number is a number that looks the same when rotated 180 degrees.
    The valid digits are 0, 1, 6, 8, 9.

    Args:
        low: The lower bound of the range as a string.
        high: The upper bound of the range as a string.

    Returns:
        The count of strobogrammatic numbers within the inclusive range.

    Examples:
        >>> solve("1", "10")
        3
        >>> solve("100", "1000")
        4
    """
    low_int = int(low)
    high_int = int(high)
    low_len = len(low)
    high_len = len(high)
    
    count = 0

    def generate_strobogrammatic(current_len: int, target_len: int) -> list[str]:
        """
        Recursively generates all strobogrammatic numbers of a specific length.
        """
        if current_len == 0:
            return [""]
        if current_len == 1:
            return ["0", "1", "8"]

        # Recursive step: get numbers of length n-2
        prev_numbers = generate_strobogrammatic(current_len - 2, target_len)
        results = []

        # Pairs that are strobogrammatic
        # (0,0), (1,1), (8,8), (6,9), (9,6)
        for s in prev_numbers:
            # We cannot put '0' at the outermost position if it's the full length
            if current_len != target_len:
                results.append("0" + s + "0")
            
            results.append("1" + s + "1")
            results.append("8" + s + "8")
            results.append("6" + s + "9")
            results.append("9" + s + "6")
            
        return results

    # Iterate through all possible lengths from len(low) to len(high)
    for length in range(low_len, high_len + 1):
        # Generate all strobogrammatic numbers of the current length
        candidates = generate_strobogrammatic(length, length)
        
        for cand in candidates:
            # Filter out numbers with leading zeros (unless the number is just "0")
            if len(cand) > 1 and cand[0] == '0':
                continue
                
            # Convert to int to check range constraints
            val = int(cand)
            if low_int <= val <= high_int:
                count += 1
                
    return count
