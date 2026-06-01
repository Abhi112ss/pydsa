METADATA = {
    "id": 65,
    "name": "Valid Number",
    "slug": "valid-number",
    "category": "String",
    "aliases": [],
    "tags": ["string", "finite_state_machine"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a given string is a valid number according to specific rules regarding signs, decimals, and exponents.",
}

def solve(s: str) -> bool:
    """
    Determines if the input string represents a valid number using a Deterministic Finite Automaton (DFA).

    The DFA states represent the progress through a valid number structure:
    - State 0: Initial state
    - State 1: Sign (+/-) seen at the start
    - State 2: Integer part seen (before decimal)
    - State 3: Decimal point seen (no digits before it)
    - State 4: Decimal point seen (digits before or after it)
    - State 5: Exponent symbol (e/E) seen
    - State 6: Sign (+/-) seen after exponent
    - State 7: Digits seen after exponent

    Args:
        s: The input string to validate.

    Returns:
        True if the string is a valid number, False otherwise.

    Examples:
        >>> solve("0")
        True
        >>> solve(" 0.1 ")
        True
        >>> solve("abc")
        False
        >>> solve("1e10")
        True
        >>> solve("e3")
        False
        >>> solve("99e2.5")
        False
        >>> solve("--6")
        False
        >>> solve("-+3")
        False
        >>> solve("95a54e53")
        False
    """
    s = s.strip()
    if not s:
        return False

    # State transitions table
    # Rows: current state, Columns: input type (digit, sign, dot, exponent, other)
    # Input types mapping:
    # 0: digit, 1: sign (+/-), 2: dot (.), 3: exponent (e/E), 4: other
    
    # State definitions:
    # 0: Start
    # 1: Sign seen
    # 2: Integer part seen
    # 3: Dot seen (no digits before)
    # 4: Valid number (integer or decimal)
    # 5: Exponent seen
    # 6: Sign after exponent seen
    # 7: Digits after exponent seen

    state = 0
    
    for char in s:
        if char.isdigit():
            # Digits move us to 'integer seen', 'decimal seen', or 'exponent digits seen'
            if state == 0 or state == 1:
                state = 2
            elif state == 2:
                state = 2
            elif state == 3:
                state = 4
            elif state == 4:
                state = 4
            elif state == 5:
                state = 7 # This shouldn't happen based on logic, but for completeness
            elif state == 6:
                state = 7
            elif state == 7:
                state = 7
            else:
                return False
        elif char in ('+', '-'):
            # Signs are only valid at the very start or immediately after an exponent
            if state == 0:
                state = 1
            elif state == 5:
                state = 6
            else:
                return False
        elif char == '.':
            # Dots are valid in the initial part, but not after an exponent
            if state == 0 or state == 1:
                state = 3
            elif state == 2:
                state = 4
            else:
                return False
        elif char in ('e', 'E'):
            # Exponents are valid only if we have already seen a valid number part
            if state == 2 or state == 4:
                state = 5
            else:
                return False
        else:
            # Any other character is invalid
            return False

    # Valid end states are:
    # 2: Integer part seen (e.g., "123")
    # 4: Decimal part seen (e.g., "123.", ".123", "123.456")
    # 7: Exponent digits seen (e.g., "1e10")
    return state in (2, 4, 7)
