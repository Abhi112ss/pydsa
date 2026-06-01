METADATA = {
    "id": 93,
    "name": "Restore IP Addresses",
    "slug": "restore-ip-addresses",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "string", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Given a string containing only digits, return all possible valid IP address combinations.",
}

def solve(s: str) -> list[str]:
    """
    Finds all possible valid IP address combinations from a given string of digits.

    A valid IP address consists of exactly four integers separated by dots. 
    Each integer must be between 0 and 255 and cannot have leading zeros 
    unless the integer is exactly '0'.

    Args:
        s: A string containing only digits.

    Returns:
        A list of strings, where each string is a valid IP address.

    Examples:
        >>> solve("25525511135")
        ['255.255.11.135', '255.255.111.35']
        >>> solve("0000")
        ['0.0.0.0']
        >>> solve("101023")
        ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']
    """
    results: list[str] = []
    n = len(s)

    # An IP address must have between 4 and 12 digits
    if n < 4 or n > 12:
        return []

    def backtrack(start_index: int, current_segments: list[str]) -> None:
        """
        Explores possible splits using depth-first search.

        Args:
            start_index: The current position in the string s.
            current_segments: The list of valid IP segments found so far.
        """
        # Base case: If we have found 4 segments
        if len(current_segments) == 4:
            # If we have also consumed the entire string, it's a valid IP
            if start_index == n:
                results.append(".".join(current_segments))
            return

        # Optimization: If remaining characters are too many or too few for remaining segments
        remaining_segments = 4 - len(current_segments)
        remaining_chars = n - start_index
        if remaining_chars < remaining_segments or remaining_chars > remaining_segments * 3:
            return

        # Try segments of length 1, 2, and 3
        for length in range(1, 4):
            # Ensure we don't go out of bounds
            if start_index + length > n:
                break
            
            segment_str = s[start_index : start_index + length]
            segment_val = int(segment_str)

            # Validation rules:
            # 1. Value must be <= 255
            # 2. No leading zeros (e.g., "01" is invalid, but "0" is valid)
            if segment_val > 255:
                continue
            if length > 1 and segment_str[0] == '0':
                continue

            # Recurse to find the next segment
            current_segments.append(segment_str)
            backtrack(start_index + length, current_segments)
            # Backtrack: remove the last segment to try the next length
            current_segments.pop()

    backtrack(0, [])
    return results
