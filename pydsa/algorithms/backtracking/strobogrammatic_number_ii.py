METADATA = {
    "id": 247,
    "name": "Strobogrammatic Number II",
    "slug": "strobogrammatic-number-ii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["recursion", "backtracking", "string"],
    "difficulty": "hard",
    "time_complexity": "O(5^(n/2))",
    "space_complexity": "O(5^(n/2))",
    "description": "Find all strobogrammatic numbers of a given length n.",
}

def solve(n: int) -> list[str]:
    """
    Finds all strobogrammatic numbers of length n using a recursive approach.
    
    A strobogrammatic number is a number that looks the same when rotated 180 degrees.
    The valid pairs are (0,0), (1,1), (6,9), (8,8), and (9,6).

    Args:
        n: The length of the strobogrammatic numbers to find.

    Returns:
        A list of strings representing all strobogrammatic numbers of length n.

    Examples:
        >>> solve(1)
        ['0', '1', '8']
        >>> solve(2)
        ['11', '69', '88', '96']
    """
    # Valid pairs that can be placed on the outside of a strobogrammatic number
    # We include (0,0) to allow building inner numbers, but handle the 
    # leading zero constraint at the top-level call.
    ST_PAIRS = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

    def build_strobogrammatic(current_n: int, target_n: int) -> list[str]:
        """
        Recursive helper to build numbers from the inside out.
        
        Args:
            current_n: The current length of the numbers being built.
            target_n: The final target length.
            
        Returns:
            List of strobogrammatic strings of length current_n.
        """
        # Base case: length 0 is an empty string
        if current_n == 0:
            return [""]
        # Base case: length 1 contains the single-digit strobogrammatic numbers
        if current_n == 1:
            return ["0", "1", "8"]

        # Recursive step: get all strobogrammatic numbers of length n-2
        inner_numbers = build_strobogrammatic(current_n - 2, target_n)
        results = []

        for left, right in ST_PAIRS:
            # A number cannot have a leading zero unless it is the single digit '0'
            # This check ensures we don't add '0' to the outermost layer if n > 1
            if left == "0" and current_n == target_n:
                continue
            
            # Wrap the inner numbers with the current pair
            for inner in inner_numbers:
                results.append(left + inner + right)
        
        return results

    return build_strobogrammatic(n, n)
