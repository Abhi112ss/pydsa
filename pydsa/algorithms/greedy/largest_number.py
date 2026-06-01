METADATA = {
    "id": 179,
    "name": "Largest Number",
    "slug": "largest_number",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "greedy", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given a list of non-negative integers, arrange them such that they form the largest number.",
}

from functools import cmp_to_key

def solve(nums: list[int]) -> str:
    """
    Arranges a list of non-negative integers to form the largest possible number.

    Args:
        nums: A list of non-negative integers.

    Returns:
        A string representing the largest number formed by concatenating the input integers.

    Examples:
        >>> solve([10, 2])
        '210'
        >>> solve([3, 30, 34, 5, 9])
        '9534330'
    """
    # Convert all integers to strings to facilitate concatenation and comparison
    num_strings = [str(num) for num in nums]

    # Define a custom comparator: for two strings x and y, we compare x+y and y+x.
    # If x+y > y+x, then x should come before y in the sorted list.
    def compare(first: str, second: str) -> int:
        if first + second > second + first:
            return -1
        elif first + second < second + first:
            return 1
        else:
            return 0

    # Sort the strings using the custom comparator
    num_strings.sort(key=cmp_to_key(compare))

    # Join the sorted strings to form the final result
    largest_num_str = "".join(num_strings)

    # Handle the edge case where the result is multiple zeros (e.g., [0, 0])
    # If the largest element is '0', the entire number is '0'.
    if largest_num_str[0] == "0":
        return "0"

    return largest_num_str