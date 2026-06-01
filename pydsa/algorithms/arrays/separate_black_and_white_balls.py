METADATA = {
    "id": 2938,
    "name": "Separate Black and White Balls",
    "slug": "separate-black-and-white-balls",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of swaps required to move all black balls to the left of all white balls.",
}

def solve(balls: list[str]) -> int:
    """
    Calculates the minimum number of swaps to move all black balls ('B') 
    to the left of all white balls ('W').

    The problem can be solved by counting how many white balls have appeared 
    before each black ball. Every time we encounter a black ball, the number 
    of white balls seen so far represents the number of swaps needed to 
    move this specific black ball to its correct relative position on the left.

    Args:
        balls: A list of strings where each string is either 'B' or 'W'.

    Returns:
        The minimum number of swaps required.

    Examples:
        >>> solve(["W", "B", "B", "W"])
        1
        >>> solve(["W", "W", "B"])
        2
        >>> solve(["B", "B", "W", "W"])
        0
    """
    total_swaps = 0
    white_ball_count = 0

    for ball in balls:
        if ball == "W":
            # Increment the count of white balls encountered so far
            white_ball_count += 1
        else:
            # When a black ball is found, it must jump over all 
            # white balls currently to its left to reach the 'black' section.
            total_swaps += white_ball_count

    return total_swaps
