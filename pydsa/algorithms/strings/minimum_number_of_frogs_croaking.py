METADATA = {
    "id": 1419,
    "name": "Minimum Number of Frogs Croaking",
    "slug": "minimum-number-of-frogs-croaking",
    "category": "String",
    "aliases": [],
    "tags": ["string", "greedy", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of frogs required to make the given croak sequence.",
}

def solve(croak: str) -> int:
    """
    Calculates the minimum number of frogs needed to produce the given croak sequence.

    The algorithm tracks the state of frogs in the middle of a 'croak' sequence.
    A frog must follow the exact sequence: 'c' -> 'r' -> 'o' -> 'a' -> 'k'.
    We maintain counts of frogs that have completed each prefix of the sequence.

    Args:
        croak: A string consisting of characters 'c', 'r', 'o', 'a', 'k'.

    Returns:
        The minimum number of frogs required. Returns -1 if the sequence is invalid.

    Examples:
        >>> solve("croakcroak")
        1
        >>> solve("croakcroakcroak")
        1
        >>> solve("cccrooorraakk")
        -1
        >>> solve("crcoak")
        -1
    """
    # Counts of frogs that have completed specific stages of the 'croak' sequence
    # c_count: frogs that just said 'c'
    # r_count: frogs that just said 'r'
    # o_count: frogs that just said 'o'
    # a_count: frogs that just said 'a'
    # k_count: frogs that just finished 'k' (not strictly needed for logic, but helps tracking)
    
    c_count = 0
    r_count = 0
    o_count = 0
    a_count = 0
    
    active_frogs = 0
    max_frogs = 0

    for char in croak:
        if char == 'c':
            c_count += 1
            active_frogs += 1
            # Track the peak number of frogs active at any single moment
            if active_frogs > max_frogs:
                max_frogs = active_frogs
        elif char == 'r':
            # A 'r' must follow a 'c'
            if c_count <= 0:
                return -1
            c_count -= 1
            r_count += 1
        elif char == 'o':
            # An 'o' must follow an 'r'
            if r_count <= 0:
                return -1
            r_count -= 1
            o_count += 1
        elif char == 'a':
            # An 'a' must follow an 'o'
            if o_count <= 0:
                return -1
            o_count -= 1
            a_count += 1
        elif char == 'k':
            # A 'k' must follow an 'a'
            if a_count <= 0:
                return -1
            a_count -= 1
            # A frog has finished its sequence, it is no longer "active"
            active_frogs -= 1
        else:
            # Invalid character in input
            return -1

    # If any frog is left in the middle of a sequence, the input is invalid
    if active_frogs != 0:
        return -1

    return max_frogs
