METADATA = {
    "id": 2724,
    "name": "Sort By",
    "slug": "sort-by",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Sort an array based on a custom comparison rule involving a given function.",
}

from functools import cmp_to_key

def solve(nums: list[int], value: int, sort_fn: callable) -> list[int]:
    """
    Sorts the array nums based on the result of sort_fn(nums[i], value).

    The sorting rule is:
    - If sort_fn(nums[i], value) < sort_fn(nums[j], value), nums[i] comes before nums[j].
    - If sort_fn(nums[i], value) > sort_fn(nums[j], value), nums[i] comes after nums[j].
    - If sort_fn(nums[i], value) == sort_fn(nums[j], value), the original relative 
      order is preserved (stable sort).

    Args:
        nums: A list of integers to be sorted.
        value: An integer value used as a parameter for the sort_fn.
        sort_fn: A function that takes two integers and returns an integer.

    Returns:
        A new list containing the elements of nums sorted according to the rule.

    Examples:
        >>> def example_fn(x, v): return x % v
        >>> solve([1, 2, 3, 4, 5], 2, example_fn)
        [2, 4, 1, 3, 5]
    """

    def custom_comparator(a: int, b: int) -> int:
        """
        Comparator function to bridge sort_fn with Python's cmp_to_key.
        """
        # Calculate the comparison values using the provided function
        val_a = sort_fn(a, value)
        val_b = sort_fn(b, value)

        # Standard comparator logic:
        # Return negative if a < b, positive if a > b, zero if equal
        if val_a < val_b:
            return -1
        elif val_a > val_b:
            return 1
        else:
            return 0

    # Python's sort (Timsort) is stable by default, satisfying the requirement
    # that elements with equal sort_fn results maintain their relative order.
    # We use cmp_to_key to convert our custom logic into a sort key.
    return sorted(nums, key=cmp_to_key(custom_comparator))
