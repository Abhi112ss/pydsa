METADATA = {
    "id": 2195,
    "name": "Append K Integers With Minimal Sum",
    "slug": "append-k-integers-with-minimal-sum",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Append k integers to an array such that the array is strictly increasing and the sum of appended integers is minimized.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Appends k integers to the array such that the array becomes strictly increasing
    and the sum of the appended integers is minimized.

    The strategy is to find the last element of the array and start appending 
    integers starting from (last_element + 1) up to (last_element + k).
    The sum of an arithmetic progression is used to calculate this in O(1).

    Args:
        nums: A list of integers representing the initial array.
        k: The number of integers to append.

    Returns:
        The minimum sum of the k appended integers.

    Examples:
        >>> solve([4, 2, 1, 3], 3)
        15
        # Appended: 4, 5, 6. Sum: 15.
        >>> solve([1, 1, 1, 1], 1)
        2
        # Appended: 2. Sum: 2.
    """
    # The problem asks for the minimum sum of k integers that make the array strictly increasing.
    # To minimize the sum, we must append the smallest possible integers that are 
    # greater than the current last element of the array.
    
    last_val = nums[-1]
    
    # The sequence to append is: (last_val + 1), (last_val + 2), ..., (last_val + k)
    # This is an arithmetic progression.
    # First term (a) = last_val + 1
    # Last term (l) = last_val + k
    # Number of terms (n) = k
    
    first_term = last_val + 1
    last_term = last_val + k
    
    # Sum of arithmetic progression formula: S = n * (a + l) / 2
    # We use integer division // because the sum of integers is always an integer.
    min_sum = (k * (first_term + last_term)) // 2
    
    return min_sum
