METADATA = {
    "id": 679,
    "name": "24 Game",
    "slug": "24-game",
    "category": "Math",
    "aliases": [],
    "tags": ["recursion", "math", "backtracking"],
    "difficulty": "hard",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if you can obtain the value 24 using four given numbers and basic arithmetic operations.",
}

def solve(cards: list[float]) -> bool:
    """
    Determines if the given list of four numbers can be combined using 
    addition, subtraction, multiplication, and division to equal 24.

    Args:
        cards: A list of four floating-point numbers.

    Returns:
        True if 24 can be achieved, False otherwise.

    Examples:
        >>> solve([4, 1, 8, 7])
        True
        >>> solve([1, 2, 1, 2])
        False
    """
    # Use a small epsilon to handle floating point precision issues
    EPSILON = 1e-6

    def backtrack(nums: list[float]) -> bool:
        # Base case: if only one number remains, check if it is approximately 24
        if len(nums) == 1:
            return abs(nums[0] - 24) < EPSILON

        # Try every pair of numbers in the current list
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                # Create a new list for the next recursion level
                # containing all numbers except the two selected
                next_nums = []
                for k in range(len(nums)):
                    if k != i and k != j:
                        next_nums.append(nums[k])

                # Get the two numbers to operate on
                a, b = nums[i], nums[j]
                
                # Generate all possible results from the four operations
                # Note: subtraction and division are order-dependent, 
                # but since we iterate through all i, j pairs, we cover both (a-b) and (b-a)
                possible_results = [a + b, a - b, a * b]
                if abs(b) > EPSILON:
                    possible_results.append(a / b)

                # Recurse with the new set of numbers
                for res in possible_results:
                    next_nums.append(res)
                    if backtrack(next_nums):
                        return True
                    next_nums.pop()  # Backtrack

        return False

    return backtrack(cards)
