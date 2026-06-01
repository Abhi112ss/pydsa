METADATA = {
    "id": 2606,
    "name": "Find the Substring With Maximum Cost",
    "slug": "find-the-substring-with-maximum-cost",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "kadane_algorithm", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the substring with the maximum cost where cost is defined by the sum of character values in a given range.",
}

def solve(s: str, max_length: int) -> str:
    """
    Finds the substring of length at most max_length with the maximum cost.
    The cost of a character is defined by its position in the alphabet (a=1, b=2, ...).

    Args:
        s: The input string.
        max_length: The maximum allowed length of the substring.

    Returns:
        The substring with the maximum cost.

    Examples:
        >>> solve("aabc", 2)
        'bc'
        >>> solve("abcd", 2)
        'cd'
    """
    n = len(s)
    # Pre-calculate costs for each character: 'a' -> 1, 'b' -> 2, etc.
    # We use a list to store costs to avoid repeated ord() calls.
    costs = [ord(char) - ord('a') + 1 for char in s]
    
    max_cost = -1
    best_start = 0
    best_end = 0
    
    current_cost = 0
    window_start = 0
    
    # We use a sliding window approach similar to Kadane's algorithm,
    # but with an additional constraint on the window size (max_length).
    for window_end in range(n):
        current_cost += costs[window_end]
        
        # If the current window exceeds max_length, shrink it from the left.
        if window_end - window_start + 1 > max_length:
            current_cost -= costs[window_start]
            window_start += 1
            
        # If the current window's cost becomes negative (not possible here since costs >= 1),
        # or if we find a better cost, we update. 
        # Note: Since all costs are positive, Kadane's logic simplifies to 
        # maximizing the window size up to max_length. However, we must handle 
        # the case where a smaller window might be better if costs were negative.
        # Given costs are [1, 26], the max cost will always be a window of size max_length
        # or the largest possible window ending at window_end.
        
        # However, to strictly follow the "maximum cost" logic for any cost array:
        # If current_cost is less than the cost of the current single element, 
        # we should reset the window. But since costs are positive, we just 
        # check if the current window is better than our global max.
        
        # Because all costs are positive, the optimal substring will always 
        # attempt to be as long as possible (up to max_length).
        # But we must check if the current window is better than the previous max.
        if current_cost > max_cost:
            max_cost = current_cost
            best_start = window_start
            best_end = window_end
        elif current_cost == max_cost:
            # If costs are equal, the problem doesn't specify, but usually 
            # we keep the first one found or follow specific tie-breaking.
            # LeetCode usually accepts any if not specified, but we'll keep the first.
            pass

        # Standard Kadane's optimization: if current_cost becomes worse than 
        # starting fresh at the current element, reset. 
        # (Though with positive costs, this only triggers if window_start moves).
        if current_cost < 0:
            current_cost = 0
            window_start = window_end + 1

    return s[best_start : best_end + 1]
