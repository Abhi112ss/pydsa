METADATA = {
    "id": 3114,
    "name": "Latest Time You Can Obtain After Replacing Characters",
    "slug": "latest-time-you-can-obtain-after-replacing-characters",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Replace question marks in a 4-digit time string to obtain the latest possible valid time.",
}

def solve(s: str) -> str:
    """
    Replaces question marks in a 4-digit time string to obtain the latest possible valid time.

    Args:
        s: A string of length 4 representing a time in "HH:MM" format.

    Returns:
        A string representing the latest possible valid time.

    Examples:
        >>> solve("2?:??")
        '23:59'
        >>> solve("?4:5?")
        '14:59'
        >>> solve("??:??")
        '23:59'
        >>> solve("0?:??")
        '09:59'
    """
    # Convert string to list for mutability
    chars = list(s)
    
    # Handle the first digit (Hours tens place)
    if chars[0] == '?':
        # If the second digit is a digit, we can only use '2' if the second digit is < 4
        # Otherwise, we must use '1' to allow for times like 19:xx
        if chars[1] != '?' and int(chars[1]) > 3:
            chars[0] = '1'
        else:
            chars[0] = '2'
            
    # Handle the second digit (Hours units place)
    if chars[1] == '?':
        # If the first digit is '2', the max second digit is '3' (23:xx)
        # If the first digit is '0' or '1', the max second digit is '9' (09:xx or 19:xx)
        if chars[0] == '2':
            chars[1] = '3'
        else:
            chars[1] = '9'
            
    # Handle the fourth digit (Minutes units place)
    if chars[3] == '?':
        # Minutes can always go up to 59, so the last digit is always '9'
        chars[3] = '9'
        
    # Handle the third digit (Minutes tens place)
    if chars[2] == '?':
        # Minutes tens place can always be '5' (x:59)
        chars[2] = '5'
        
    # Note: The colon at index 2 is handled by the logic above (index 2 is the colon in "HH:MM")
    # Wait, the input format is "HH:MM", so indices are: 0, 1, 2 (colon), 3, 4.
    # Let's re-align the indices based on "HH:MM" structure.
    
    # Re-implementing with correct index mapping for "HH:MM"
    # Index 0: H1, Index 1: H2, Index 2: ':', Index 3: M1, Index 4: M2
    
    res = list(s)
    
    # 1. Handle H1 (Index 0)
    if res[0] == '?':
        # If H2 is a digit and > 3, H1 must be '1' (e.g., ?4:xx -> 14:xx)
        if res[1] != '?' and int(res[1]) > 3:
            res[0] = '1'
        else:
            res[0] = '2'
            
    # 2. Handle H2 (Index 1)
    if res[1] == '?':
        # If H1 is '2', H2 max is '3'
        if res[0] == '2':
            res[1] = '3'
        else:
            res[1] = '9'
            
    # 3. Handle M1 (Index 3)
    if res[3] == '?':
        # Minutes tens place max is '5'
        res[3] = '5'
        
    # 4. Handle M2 (Index 4)
    if res[4] == '?':
        # Minutes units place max is '9'
        res[4] = '9'
        
    return "".join(res)
