METADATA = {
    "id": 838,
    "name": "Push Dominoes",
    "slug": "push-dominoes",
    "category": "Simulation",
    "aliases": [],
    "tags": ["two_pointer", "simulation", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine the final state of dominoes after a series of pushes using net force calculation.",
}

def solve(dominoes: str) -> str:
    """
    Calculates the final state of dominoes after they are pushed.

    The algorithm uses a two-pointer approach to identify segments between 
    fixed dominoes ('L' or 'R') and determines the behavior of the 
    dominoes in between based on the forces applied from both ends.

    Args:
        dominoes: A string representing the initial state of the dominoes.

    Returns:
        A string representing the final state of the dominoes.

    Examples:
        >>> solve(".L.R...LR..L..")
        'LL.RR.LLRRLL..'
        >>> solve("..R..")
        '..RRR'
    """
    # Add virtual boundaries to handle edge cases (start and end of the string)
    # A virtual 'L' at the far left and 'R' at the far right won't affect 
    # the actual dominoes but simplify the segment logic.
    symbols = [('L', -1)]
    for index, char in enumerate(dominoes):
        if char != '.':
            symbols.append((char, index))
    symbols.append(('R', len(dominoes)))

    result = list(dominoes)
    
    # Iterate through segments defined by the fixed dominoes
    for i in range(len(symbols) - 1):
        left_char, left_idx = symbols[i]
        right_char, right_idx = symbols[i + 1]
        
        # Calculate the number of empty dominoes between the two fixed points
        num_empty = right_idx - left_idx - 1
        
        if left_char == right_char:
            # Case 1: Both sides are the same (e.g., R...R or L...L)
            # All dominoes in between fall in that direction
            for j in range(left_idx + 1, right_idx):
                result[j] = left_char
        elif left_char == 'R' and right_char == 'L':
            # Case 2: Forces meet (R...L)
            # Dominoes fall towards the center; if odd, the middle stays upright
            for j in range(1, (num_empty // 2) + 1):
                result[left_idx + j] = 'R'
                result[right_idx - j] = 'L'
        else:
            # Case 3: Forces diverge (L...R)
            # Dominoes in between remain upright ('.')
            pass

    return "".join(result)
