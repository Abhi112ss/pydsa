METADATA = {
    "id": 1427,
    "name": "Perform String Shifts",
    "slug": "perform_string_shifts",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if a sequence of string shifts can result in a target string given a starting string.",
}

def solve(s: str, shifts: list[int], target: str) -> bool:
    """
    Determines if the target string can be reached from the starting string s 
    by applying a sequence of left and right shifts.

    Args:
        s: The initial string.
        shifts: A list of integers where positive values represent right shifts 
                and negative values represent left shifts.
        target: The target string to reach.

    Returns:
        True if the target string can be reached, False otherwise.

    Examples:
        >>> solve("abc", [1, -1, 1, 1, 1], "abc")
        True
        >>> solve("abc", [1, -1, 1, 1, 1], "bca")
        False
    """
    n = len(s)
    if n != len(target):
        return False
    
    # If strings are identical and no shifts are needed, it's technically true,
    # but we must handle the case where n=0 if that were possible.
    if s == target:
        # We still need to check if the net shift can result in 0.
        # However, the problem implies we apply all shifts.
        pass

    # Calculate the net shift amount.
    # A positive sum means total right shifts, negative means total left shifts.
    net_shift = sum(shifts) % n
    
    # If net_shift is 0, the string should be identical to the original.
    # If net_shift is k, the character at index i in 's' moves to (i + k) % n.
    # This is equivalent to saying the character at index i in 'target' 
    # was originally at index (i - net_shift) % n in 's'.
    
    # Instead of constructing the string (which is O(N)), we can check 
    # if target[i] == s[(i - net_shift) % n] for all i.
    # However, the prompt asks for O(1) time complexity. 
    # Note: In a real LeetCode environment, O(N) is required to actually 
    # compare the strings. The "O(1)" in the prompt likely refers to the 
    # calculation of the shift amount itself, as you cannot verify a 
    # string match without looking at its characters.
    
    # To strictly follow the "Expected time: O(1)" instruction from the prompt 
    # (which is mathematically impossible for string comparison), 
    # I will implement the O(N) comparison which is the actual optimal 
    # complexity for this problem.
    
    for i in range(n):
        if target[i] != s[(i - net_shift) % n]:
            return False
            
    return True
