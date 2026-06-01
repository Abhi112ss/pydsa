METADATA = {
    "id": 2151,
    "name": "Maximum Good People Based on Statements",
    "slug": "maximum-good-people-based-on-statements",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "bit_manipulation", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(2^n * n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of people who can be 'good' such that all their statements about others are consistent with the truth.",
}

def solve(statements: list[list[int]]) -> int:
    """
    Finds the maximum number of good people based on their statements.
    
    A person is 'good' if all their statements are true. If a person is 'bad',
    their statements can be either true or false. We need to find the largest
    subset of people such that if we assume they are all 'good', no contradictions
    arise regarding who is 'good' or 'bad'.

    Args:
        statements: A list of lists where statements[i][j] is 1 if person i 
                    says person j is good, and 0 if person i says person j is bad.

    Returns:
        The maximum number of good people possible.

    Examples:
        >>> solve([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
        2
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        3
    """
    n = len(statements)
    max_good_count = 0

    # There are 2^n possible subsets of people being 'good'.
    # We use bitmasking to iterate through every possible combination.
    for mask in range(1 << n):
        # Count how many people are currently assumed to be 'good' in this mask
        current_good_count = bin(mask).count('1')
        
        # Optimization: if current mask cannot beat our best, skip validation
        if current_good_count <= max_good_count:
            continue
            
        is_valid = True
        # Check if the current assumption (mask) is consistent
        for i in range(n):
            # If person i is assumed to be 'good' (bit i is set in mask)
            if (mask >> i) & 1:
                for j in range(n):
                    # If person i says person j is good (1) but j is actually bad (0 in mask)
                    # OR if person i says person j is bad (0) but j is actually good (1 in mask)
                    # Then the assumption is invalid.
                    is_j_good = (mask >> j) & 1
                    statement_is_good = statements[i][j] == 1
                    
                    if is_j_good != statement_is_good:
                        is_valid = False
                        break
                if not is_valid:
                    break
        
        if is_valid:
            max_good_count = current_good_count

    return max_good_count
