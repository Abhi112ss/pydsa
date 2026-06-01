METADATA = {
    "id": 1431,
    "name": "Kids With the Greatest Number of Candies",
    "slug": "kids_with_the_greatest_number_of_candies",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return a list indicating which kids can have the greatest number of candies after receiving extra candies.",
}


def solve(candies: list[int], extraCandies: int) -> list[bool]:
    """Determine which kids can reach the greatest candy count after receiving extra candies.

    Args:
        candies: List of integers where each integer represents the number of candies a kid currently has.
        extraCandies: Integer representing the number of extra candies each kid could potentially receive.

    Returns:
        A list of booleans where each boolean corresponds to a kid; True if the kid can have the greatest
        number of candies after receiving extraCandies, otherwise False.

    Examples:
        >>> solve([2, 3, 5, 1, 3], 3)
        [True, True, True, False, True]
        >>> solve([4, 2, 1, 1, 2], 1)
        [True, False, False, False, False]
    """
    # Find the current maximum number of candies among all kids.
    maximum_candies = max(candies)

    # Build the result list by checking each kid's potential candy count.
    result: list[bool] = []
    for current_candies in candies:
        # If the kid receives extraCandies and reaches or exceeds the maximum, they can be greatest.
        can_be_greatest = current_candies + extraCandies >= maximum_candies
        result.append(can_be_greatest)

    return result