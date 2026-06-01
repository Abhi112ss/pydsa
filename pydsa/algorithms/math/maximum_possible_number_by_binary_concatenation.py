METADATA = {
    "id": 3309,
    "name": "Maximum Possible Number by Binary Concatenation",
    "slug": "maximum-possible-number-by-binary-concatenation",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum possible number formed by concatenating a given list of binary strings.",
}

from functools import cmp_to_key

def solve(binary_strings: list[str]) -> str:
    """
    Finds the maximum possible number formed by concatenating all binary strings in the list.

    The problem is equivalent to finding the optimal permutation of strings to maximize 
    the resulting concatenated value. This is a classic variation of the 'Largest Number' 
    problem, where the optimal ordering is determined by comparing the concatenation 
    of two strings in both possible orders (a + b vs b + a).

    Args:
        binary_strings: A list of strings representing binary numbers.

    Returns:
        A string representing the maximum possible concatenated binary number.

    Examples:
        >>> solve(["1", "0"])
        "10"
        >>> solve(["10", "1"])
        "110"
        >>> solve(["0", "0", "0"])
        "000"
    """
    
    def compare_strings(a: str, b: str) -> int:
        """
        Custom comparator for sorting strings to maximize concatenation.
        
        If a + b > b + a, then 'a' should come before 'b'.
        """
        # Concatenate in both possible orders to determine which sequence is larger
        order_one = a + b
        order_two = b + a
        
        if order_one > order_two:
            return -1  # a should come before b
        elif order_one < order_two:
            return 1   # b should come before a
        else:
            return 0

    # Sort the strings using the custom comparator.
    # The time complexity is O(N log N * K) where K is the average length of strings,
    # because string concatenation and comparison take O(K) time.
    sorted_strings = sorted(binary_strings, key=cmp_to_key(compare_strings))
    
    # Join the sorted strings to form the final maximum number.
    return "".join(sorted_strings)
