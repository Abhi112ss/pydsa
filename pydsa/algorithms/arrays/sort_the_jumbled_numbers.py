METADATA = {
    "id": 2191,
    "name": "Sort the Jumbled Numbers",
    "slug": "sort-the-jumbled-numbers",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort an array based on the sum of digits, and then by the value of the number itself if sums are equal.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Sorts the jumbled numbers based on the sum of their digits.
    If two numbers have the same sum of digits, they are sorted by their actual value.

    Args:
        nums: A list of integers to be sorted.

    Returns:
        A list of integers sorted according to the specified rules.

    Examples:
        >>> solve([10, 2, 7, 1])
        [1, 10, 2, 7]
        >>> solve([834, 626, 214, 738, 539, 123, 985])
        [123, 214, 539, 626, 738, 834, 985]
    """

    def get_digit_sum(number: int) -> int:
        """Calculates the sum of the digits of a given integer."""
        digit_sum = 0
        # Use absolute value to handle potential negative inputs, 
        # though problem constraints usually imply non-negative.
        temp_num = abs(number)
        while temp_num > 0:
            digit_sum += temp_num % 10
            temp_num //= 10
        return digit_sum

    # We create a list of tuples where each tuple is (digit_sum, original_value).
    # Python's sort is stable and handles tuple comparison lexicographically:
    # It compares the first element (digit_sum), and if they are equal, 
    # it compares the second element (original_value).
    decorated_list: list[tuple[int, int]] = []
    for num in nums:
        decorated_list.append((get_digit_sum(num), num))

    # Sort the decorated list. Time complexity: O(n log n)
    decorated_list.sort()

    # Extract the original values from the sorted tuples.
    return [item[1] for item in decorated_list]
