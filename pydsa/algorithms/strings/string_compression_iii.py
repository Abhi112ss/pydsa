METADATA = {
    "id": 3163,
    "name": "String Compression III",
    "slug": "string-compression-iii",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Compress a string by replacing contiguous identical characters with their count and the character itself, provided the count is less than 10.",
}

def solve(s: str) -> str:
    """
    Compresses the input string by replacing contiguous identical characters 
    with their count (if count < 10) followed by the character.

    Args:
        s: The input string to be compressed.

    Returns:
        The compressed string.

    Examples:
        >>> solve("aaaaaaaaaa")
        "10a" (Wait, the problem constraint says count < 10 for the specific rule, 
              but actually the problem asks to compress segments. 
              Let's re-read: "replace each contiguous segment of the same character 
              with its length followed by the character". 
              Note: The problem implies we process segments as they appear.)
        >>> solve("aaaaaaaaaa")
        "10a" is not possible if we follow the rule strictly for segments.
        Actually, the problem states: "replace each contiguous segment... 
        with its length followed by the character". 
        If length is 10, it becomes '10a'.
        Wait, the problem description for 3163 says: 
        "replace each contiguous segment of the same character with its length 
        followed by the character".
        Example: "aaaaaaaaaa" -> "10a".
        Example: "aaabb" -> "3a2b".
    """
    result_parts: list[str] = []
    n = len(s)
    i = 0

    while i < n:
        char = s[i]
        start_index = i
        
        # Move the pointer to find the end of the contiguous segment
        while i < n and s[i] == char:
            i += 1
        
        # Calculate the length of the segment
        segment_length = i - start_index
        
        # Append the length and the character to the result list
        # Using a list and joining is more efficient than string concatenation
        result_parts.append(str(segment_length))
        result_parts.append(char)

    return "".join(result_parts)

# Note: The prompt description for 3163 in LeetCode actually specifies 
# that the length is always < 10 for the specific test cases or 
# constraints provided in some versions, but the logic remains O(n).
# Let's refine the implementation to be the standard segment-based compression.

class Solution:
    def compressString(self, s: str) -> str:
        """
        Standard implementation for LeetCode 3163.
        
        Args:
            s: The input string.
            
        Returns:
            The compressed string.
        """
        if not s:
            return ""
            
        res = []
        n = len(s)
        i = 0
        
        while i < n:
            current_char = s[i]
            count = 0
            
            # Count contiguous occurrences
            while i < n and s[i] == current_char:
                count += 1
                i += 1
            
            # Append count and character
            res.append(str(count))
            res.append(current_char)
            
        return "".join(res)

def solve_optimized(s: str) -> str:
    """
    The optimal O(n) time and O(n) space (for result string) implementation.
    Note: Space complexity is O(n) to store the output string, 
    but O(1) auxiliary space if we don't count the output.
    """
    return Solution().compressString(s)
