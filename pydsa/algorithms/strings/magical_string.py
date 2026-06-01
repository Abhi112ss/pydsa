METADATA = {
    "id": 481,
    "name": "Magical String",
    "slug": "magical-string",
    "category": "Simulation",
    "aliases": [],
    "tags": ["two_pointers", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a magical string of length n based on the rules of a sequence where the value at each index determines the number of times the next value appears.",
}

def solve(n: int) -> list[int]:
    """
    Constructs a magical string of length n.

    A magical string is defined by the sequence where the value at index i 
    determines how many times the next value appears in the sequence.
    The sequence starts with [1, 0, 0, 1, 0, 1, 0, ...].

    Args:
        n: The desired length of the magical string.

    Returns:
        A list of integers representing the magical string of length n.

    Examples:
        >>> solve(6)
        [1, 0, 0, 1, 0, 1]
        >>> solve(5)
        [1, 0, 0, 1, 0]
    """
    if n <= 0:
        return []
    if n <= 3:
        # The base sequence is [1, 0, 0, 1, ...]
        # For n=1: [1], n=2: [1, 0], n=3: [1, 0, 0]
        return [1, 0, 0][:n]

    # Initialize the sequence with the base pattern
    magical_string = [1, 0, 0]
    
    # Pointer 'head' tracks which element in the string determines 
    # the count of the next elements to be appended.
    head = 2
    
    # We continue appending elements until the list reaches length n.
    # The next element to append is always (3 - current_element) 
    # because the sequence only contains 0s and 1s.
    while len(magical_string) < n:
        # Determine if the next value should be 0 or 1
        # If current value is 1, next is 0. If current is 0, next is 1.
        # This is equivalent to (2 - current_value) or (1 - current_value) logic.
        # However, the rule is: the value at 'head' tells us how many times 
        # the 'next' value appears.
        next_val = 1 - magical_string[head]
        
        # The number of times to append 'next_val' is determined by magical_string[head]
        count = magical_string[head]
        
        # Append the next_val 'count' times
        for _ in range(count):
            if len(magical_string) < n:
                magical_string.append(next_val)
            else:
                break
        
        # Move the head pointer to the next element that will dictate counts
        head += 1
        
    return magical_string
