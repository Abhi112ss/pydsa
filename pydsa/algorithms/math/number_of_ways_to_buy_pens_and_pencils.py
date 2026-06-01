METADATA = {
    "id": 2240,
    "name": "Number of Ways to Buy Pens and Pencils",
    "slug": "number-of-ways-to-buy-pens-and-pencils",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to buy one pen and one pencil such that their total cost does not exceed a given budget.",
}

def solve(pens: list[int], pencils: list[int], budget: int) -> int:
    """
    Calculates the number of pairs (pen, pencil) such that pen + pencil <= budget.

    Args:
        pens: A list of integers representing the prices of pens.
        pencils: A list of integers representing the prices of pencils.
        budget: An integer representing the maximum total cost allowed.

    Returns:
        The total number of valid combinations.

    Examples:
        >>> solve([1, 2, 3], [1, 2, 3], 4)
        6
        >>> solve([10, 20], [1, 2], 15)
        2
    """
    # Sort both lists to enable the two-pointer approach
    # Sorting takes O(n log n + m log m), but the problem constraints 
    # and logic suggest we can treat the traversal as O(n + m) after sorting.
    pens.sort()
    pencils.sort()

    total_ways = 0
    pen_count = len(pens)
    pencil_count = len(pencils)

    # Use a two-pointer approach:
    # For each pen, find the largest index in pencils such that pens[i] + pencils[j] <= budget.
    # As the pen price increases, the maximum possible pencil index decreases.
    pencil_ptr = pencil_count - 1

    for pen_price in pens:
        # If the current pen is already more expensive than the budget, 
        # no pencil can be paired with it (since pencils are sorted and >= 0).
        if pen_price >= budget:
            break
            
        # Move the pencil pointer left until the sum is within the budget
        while pencil_ptr >= 0 and pen_price + pencils[pencil_ptr] > budget:
            pencil_ptr -= 1
        
        # If pencil_ptr is -1, no pencils can be paired with this pen or any subsequent (more expensive) pen
        if pencil_ptr < 0:
            break
            
        # All pencils from index 0 to pencil_ptr are valid for the current pen
        total_ways += (pencil_ptr + 1)

    return total_ways
