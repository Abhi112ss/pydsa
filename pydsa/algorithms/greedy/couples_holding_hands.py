METADATA = {
    "id": 765,
    "name": "Couples Holding Hands",
    "slug": "couples-holding-hands",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "union_find", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of swaps to ensure every couple is sitting together.",
}

def solve(row: list[int]) -> int:
    """
    Calculates the minimum number of swaps required to seat all couples together.

    The algorithm uses a greedy approach: iterate through the seats two at a time.
    If the person at the current seat and the person in the adjacent seat are not
    a couple, find the correct partner in the remaining seats and swap them into
    the adjacent seat.

    Args:
        row: A list of integers representing the people sitting in a row.

    Returns:
        The minimum number of swaps needed.

    Examples:
        >>> solve([3, 2, 0, 1])
        1
        >>> solve([1, 0, 2, 3, 4, 5, 6, 7])
        0
        >>> solve([3, 0, 2, 1])
        2
    """
    swaps = 0
    n = len(row)
    
    # Iterate through the row, jumping by 2 to check each pair of seats
    for i in range(0, n, 2):
        person_a = row[i]
        # The partner of person_a is found by XORing with 1
        # (0,1), (2,3), (4,5) etc. are couples
        target_partner = person_a ^ 1
        
        # If the person sitting next to person_a is not their partner
        if row[i + 1] != target_partner:
            swaps += 1
            
            # Find the index of the actual partner in the rest of the row
            # We start searching from i + 2 because i + 1 is already checked
            for j in range(i + 2, n):
                if row[j] == target_partner:
                    # Swap the current incorrect person with the correct partner
                    row[i + 1], row[j] = row[j], row[i + 1]
                    break
                    
    return swaps
