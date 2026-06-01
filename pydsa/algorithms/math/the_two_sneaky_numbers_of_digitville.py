METADATA = {
    "id": 3289,
    "name": "The Two Sneaky Numbers of Digitville",
    "slug": "the-two-sneaky-numbers-of-digitville",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "bit_manipulation", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the two numbers that appear more than once in an array where all other numbers appear exactly once.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds the two numbers that appear twice in the given list.

    The input list contains numbers where most appear once, but two numbers 
    appear twice. Since the numbers are within a predictable range, we can 
    use a frequency array or a set to track occurrences.

    Args:
        nums: A list of integers where two numbers are repeated.

    Returns:
        A list containing the two repeated numbers in any order.

    Examples:
        >>> solve([1, 2, 3, 4, 1, 2])
        [1, 2]
        >>> solve([0, 1, 0, 3, 2, 4, 4])
        [0, 4]
    """
    # Since the problem constraints usually imply numbers are within 
    # a small range (0 to n), a frequency array or a set is optimal.
    # Given the constraints of this specific problem type, we use a set
    # to track seen numbers and identify duplicates in O(n) time.
    seen_numbers: set[int] = set()
    duplicates: list[int] = []

    for number in nums:
        if number in seen_numbers:
            # If the number is already in the set, it's a sneaky number
            duplicates.append(number)
        else:
            # Otherwise, add it to the set to track its occurrence
            seen_numbers.add(number)
            
    return duplicates
