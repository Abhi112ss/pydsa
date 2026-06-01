METADATA = {
    "id": 2698,
    "name": "Find the Punishment Number of an Integer",
    "slug": "find-the-punishment-number-of-an-integer",
    "category": "Math",
    "aliases": [],
    "tags": ["backtracking", "math", "dynamic programming"],
    "difficulty": "medium",
    "time_complexity": "O(n * 10^log10(n))",
    "space_complexity": "O(log10(n))",
    "description": "Calculate the sum of squares of integers from 1 to n where the square's digits can be partitioned to sum up to the integer itself.",
}

def solve(n: int) -> int:
    """
    Calculates the punishment number of an integer n.

    The punishment number is the sum of the squares of all integers i (1 <= i <= n)
    such that the digits of i*i can be partitioned into contiguous substrings
    whose sum equals i.

    Args:
        n: The upper bound integer.

    Returns:
        The punishment number of n.

    Examples:
        >>> solve(10)
        183
        >>> solve(37)
        1478
    """

    def can_partition(target: int, s: str, index: int) -> bool:
        """
        Uses backtracking to check if the string s can be partitioned 
        into substrings that sum up to the target.

        Args:
            target: The remaining sum required.
            s: The string representation of the square.
            index: The current starting index in the string.

        Returns:
            True if a valid partition exists, False otherwise.
        """
        # Base case: if we reached the end of the string, check if target is met
        if index == len(s):
            return target == 0
        
        # If target becomes negative, this path is invalid
        if target < 0:
            return False

        current_val = 0
        # Try all possible substrings starting from 'index'
        for j in range(index, len(s)):
            # Build the number digit by digit
            current_val = current_val * 10 + int(s[j])
            
            # Optimization: if current_val exceeds target, no need to continue this loop
            if current_val > target:
                break
            
            # Recurse with the remaining target and the next index
            if can_partition(target - current_val, s, j + 1):
                return True
                
        return False

    total_punishment_sum = 0
    
    for i in range(1, n + 1):
        square = i * i
        square_str = str(square)
        
        # Check if the square of i satisfies the punishment condition
        if can_partition(i, square_str, 0):
            total_punishment_sum += square
            
    return total_punishment_sum
