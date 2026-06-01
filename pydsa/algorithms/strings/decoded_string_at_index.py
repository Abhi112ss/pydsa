METADATA = {
    "id": 880,
    "name": "Decoded String at Index",
    "slug": "decoded-string-at-index",
    "category": "String",
    "aliases": [],
    "tags": ["math", "string", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(1)",
    "description": "Find the k-th character of a string that is repeatedly decoded by repeating its previous version k times.",
}

def solve(s: str, k: int) -> str:
    """
    Finds the k-th character of the decoded string without fully expanding it.

    The decoding process follows the rule: s_new = s_old * int(s_old[-1]).
    Instead of building the string, we work backwards from the final length 
    to determine which character at which position corresponds to the k-th index.

    Args:
        s: The encoded string where the last character is the multiplier.
        k: The 1-based index of the character to retrieve.

    Returns:
        The character at the k-th position.

    Examples:
        >>> solve("a2i1", 5)
        'a'
        >>> solve("abc2", 3)
        'b'
    """
    # Convert k to 0-based index for easier calculation
    current_k = k - 1
    
    # We need to track the length of the string at each step of the decoding process.
    # Since we work backwards, we first calculate the lengths of all intermediate strings.
    lengths = [0]
    current_length = 0
    
    for char in s:
        if char.isdigit():
            multiplier = int(char)
            current_length *= multiplier
        else:
            current_length += 1
        lengths.append(current_length)

    # Work backwards from the last decoded state to the original string
    # We iterate through the string in reverse to undo the multiplication/addition
    for i in range(len(s) - 1, -1, -1):
        char = s[i]
        
        if char.isdigit():
            # If the current character is a multiplier, the string was repeated.
            # We use modulo to find the position within the previous (un-multiplied) string.
            multiplier = int(char)
            # The length before this multiplication was lengths[i]
            # But we need to find the length of the string *before* this multiplier was applied.
            # The length of the string before this step is lengths[i] (which is the length of the prefix)
            # However, the logic is simpler: the length of the string before this digit was applied
            # is the length of the string formed by s[:i].
            # We use the modulo operator to map the current_k into the range of the previous string.
            prev_length = lengths[i]
            if prev_length > 0:
                current_k %= prev_length
        else:
            # If the current character is a letter, it was appended to the previous string.
            # If our current_k is at the very end of the current string, it must be this character.
            # The length of the string before this character was lengths[i].
            prev_length = lengths[i]
            if current_k == prev_length:
                return char
            # Otherwise, current_k remains the same as we move to the prefix.

    # This part should theoretically not be reached if k is valid
    return ""
