METADATA = {
    "id": 1415,
    "name": "The k-th Lexicographical String of All Happy Strings of Length n",
    "slug": "the-k-th-lexicographical-string-of-all-happy-strings-of-length-n",
    "category": "String",
    "aliases": [],
    "tags": ["backtracking", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(3^n)",
    "space_complexity": "O(n)",
    "description": "Find the k-th lexicographically smallest happy string of length n, where a happy string contains no two consecutive identical characters.",
}

def solve(n: int, k: int) -> str:
    """
    Finds the k-th lexicographical happy string of length n.
    
    A happy string is defined as a string containing only 'a', 'b', and 'c' 
    where no two adjacent characters are the same.

    Args:
        n: The required length of the happy string.
        k: The index (1-indexed) of the lexicographical string to find.

    Returns:
        The k-th lexicographical happy string, or an empty string if it doesn't exist.

    Examples:
        >>> solve(1, 3)
        'c'
        >>> solve(2, 3)
        'ba'
        >>> solve(3, 10)
        ''
    """
    happy_strings = []
    chars = ['a', 'b', 'c']

    def backtrack(current_string: list[str]) -> bool:
        """
        Standard backtracking to generate strings in lexicographical order.
        Returns True if the k-th string is found to prune the search.
        """
        # Base case: if the string reaches length n, we found a valid happy string
        if len(current_string) == n:
            happy_strings.append("".join(current_string))
            # Return True if we have reached the k-th string to stop further recursion
            return len(happy_strings) == k

        for char in chars:
            # Check the 'happy' condition: current char must not be same as previous
            if not current_string or current_string[-1] != char:
                current_string.append(char)
                # If the k-th string is found in the subtree, propagate the stop signal
                if backtrack(current_string):
                    return True
                current_string.pop()
        
        return False

    # Start backtracking with an empty list
    backtrack([])

    # If the list contains k elements, return the last one; otherwise return empty string
    if len(happy_strings) < k:
        return ""
    
    return happy_strings[k - 1]
