METADATA = {
    "id": 1963,
    "name": "Minimum Number of Swaps to Make the String Balanced",
    "slug": "minimum-number-of-swaps-to-make-the-string-balanced",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of swaps required to make a string of brackets balanced.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of swaps to make a string of brackets balanced.
    
    The algorithm uses a greedy approach by tracking the net balance of 
    unmatched opening brackets. Since we only care about the maximum 
    imbalance (the number of '[' that don't have a corresponding ']'), 
    we can calculate the result based on that imbalance.

    Args:
        s: A string consisting of '[' and ']'.

    Returns:
        The minimum number of swaps needed to balance the string.

    Examples:
        >>> solve("][][")
        1
        >>> solve("]]][[[")
        2
    """
    max_imbalance = 0
    current_balance = 0

    for char in s:
        if char == '[':
            # An opening bracket increases the potential for a balanced pair
            current_balance += 1
        else:
            # A closing bracket decreases the balance
            current_balance -= 1
        
        # We track the most negative the balance gets.
        # This represents the maximum number of unmatched ']' encountered.
        # However, it is easier to track the 'unmatched' '[' by looking at 
        # how many '[' are left open after all ']' are processed.
        # Alternatively, we can track the depth of unmatched ']'.
        if current_balance < 0:
            # We use the absolute value of the most negative balance 
            # to represent the number of unmatched closing brackets.
            max_imbalance = max(max_imbalance, -current_balance)

    # Each swap of a ']' with a '[' can resolve two unmatched closing brackets
    # and two unmatched opening brackets simultaneously.
    # The formula (max_imbalance + 1) // 2 accounts for this efficiency.
    return (max_imbalance + 1) // 2
