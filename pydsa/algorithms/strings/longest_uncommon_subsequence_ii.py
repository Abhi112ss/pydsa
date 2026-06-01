METADATA = {
    "id": 522,
    "name": "Longest Uncommon Subsequence II",
    "slug": "longest-uncommon-subsequence-ii",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "enumeration"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 * l)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest string in the array that is not a subsequence of any other string in the array.",
}

def is_subsequence(sub: str, full: str) -> bool:
    """
    Checks if string 'sub' is a subsequence of string 'full'.

    Args:
        sub: The potential subsequence string.
        full: The target string to check against.

    Returns:
        True if 'sub' is a subsequence of 'full', False otherwise.
    """
    sub_index = 0
    full_index = 0
    
    while sub_index < len(sub) and full_index < len(full):
        if sub[sub_index] == full[full_index]:
            sub_index += 1
        full_index += 1
        
    return sub_index == len(sub)

def solve(arr: list[str]) -> int:
    """
    Finds the length of the longest uncommon subsequence.

    A string is an uncommon subsequence if it is not a subsequence of any 
    other string in the array.

    Args:
        arr: A list of strings.

    Returns:
        The length of the longest uncommon subsequence, or -1 if none exists.

    Examples:
        >>> solve(["aba", "cdc", "eae"])
        3
        >>> solve(["aaa", "aaa"])
        -1
        >>> solve(["a", "bb", "ccc"])
        3
    """
    # Sort strings by length in descending order to find the longest one first
    # This allows us to return immediately once we find a valid candidate
    sorted_arr = sorted(arr, key=len, reverse=True)
    
    for i in range(len(sorted_arr)):
        candidate = sorted_arr[i]
        is_uncommon = True
        
        for j in range(len(sorted_arr)):
            # We only compare the candidate against OTHER strings in the array
            if i == j:
                continue
            
            # If the candidate is a subsequence of any other string, 
            # it cannot be the longest uncommon subsequence
            if is_subsequence(candidate, sorted_arr[j]):
                is_uncommon = False
                break
        
        if is_uncommon:
            return len(candidate)
            
    return -1
