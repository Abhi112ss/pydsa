METADATA = {
    "id": 932,
    "name": "Beautiful Array",
    "slug": "beautiful-array",
    "category": "Divide and Conquer",
    "aliases": [],
    "tags": ["divide_and_conquer", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n log n)",
    "description": "Construct an array of size n such that for every i < k < j, array[i] + array[j] != 2 * array[k].",
}

def solve(n: int) -> list[int]:
    """
    Constructs a beautiful array of size n using a divide and conquer approach.
    
    A beautiful array satisfies the property that for any i < k < j, 
    A[i] + A[j] != 2 * A[k]. This is equivalent to saying that no element 
    is the arithmetic mean of two other elements.
    
    The core idea is that if an array is beautiful, then:
    1. Linear transformation (ax + b) preserves beauty.
    2. If we split elements into 'odds' and 'evens', the sum of an odd and 
       an even number is always odd, while 2 * k is always even. 
       Thus, no k can be the mean of an odd and an even number.
    
    Args:
        n: The size of the array to construct.
        
    Returns:
        A list of integers from 1 to n that form a beautiful array.
        
    Examples:
        >>> solve(4)
        [1, 3, 2, 4]
        >>> solve(5)
        [1, 5, 3, 2, 4]
    """
    # Base case: an array of size 1 is always beautiful.
    if n == 1:
        return [1]

    # Divide: Separate the problem into odd-indexed and even-indexed components.
    # We transform the problem of size n into two smaller problems:
    # One for elements that will become odd (2*x - 1) and one for even (2*x).
    
    # Number of elements in the 'odd' part (1, 3, 5...)
    # If n=5, odds are 1, 3, 5 (size 3); evens are 2, 4 (size 2).
    num_odds = (n + 1) // 2
    num_evens = n // 2

    # Recursively solve for the smaller sub-problems.
    odds = solve(num_odds)
    evens = solve(num_evens)

    # Conquer: Map the results back to the required range.
    # Map elements in 'odds' to 2*x - 1 to ensure they are odd.
    # Map elements in 'evens' to 2*x to ensure they are even.
    # Concatenating them ensures no element from 'odds' and 'evens' can form 
    # an arithmetic mean with an element in between.
    result = []
    for x in odds:
        result.append(2 * x - 1)
    for x in evens:
        result.append(2 * x)

    return result
