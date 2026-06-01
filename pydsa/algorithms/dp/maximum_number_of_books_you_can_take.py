METADATA = {
    "id": 2355,
    "name": "Maximum Number of Books You Can Take",
    "slug": "maximum-number-of-books-you-can-take",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of books you can take such that no two books are within a certain distance of each other.",
}

def solve(books: list[int], distance: int) -> int:
    """
    Calculates the maximum number of books that can be taken given a minimum distance constraint.
    
    The problem is a variation of the 'House Robber' or 'Interval Scheduling' problem.
    Since we want to maximize the count, and the 'cost' of picking a book is simply 
    the distance it forces us to skip, we can use dynamic programming.
    
    Args:
        books: A list of integers representing the positions of the books.
        distance: The minimum required distance between any two selected books.
        
    Returns:
        The maximum number of books that can be selected.
        
    Examples:
        >>> solve([1, 4, 5, 10], 3)
        3
        >>> solve([1, 2, 3, 4, 5], 2)
        3
    """
    n = len(books)
    if n == 0:
        return 0
    
    # dp[i] stores the maximum number of books we can take considering books from index 0 to i.
    dp = [0] * n
    
    for i in range(n):
        # Option 1: Don't take the current book.
        # The value is the same as the maximum books taken up to the previous index.
        res_exclude = dp[i - 1] if i > 0 else 0
        
        # Option 2: Take the current book.
        # We must find the latest book 'j' such that books[i] - books[j] >= distance.
        # Since the books array is sorted, we can use binary search or a pointer.
        # However, for a simple DP approach, we look for the largest j < i where books[i] - books[j] >= distance.
        
        # To maintain O(n) overall, we can use a pointer or binary search.
        # Let's use binary search to find the rightmost valid index 'j'.
        
        # Find the largest index 'j' such that books[j] <= books[i] - distance
        target = books[i] - distance
        
        # Binary search for the rightmost index satisfying the condition
        low = 0
        high = i - 1
        best_j = -1
        while low <= high:
            mid = (low + high) // 2
            if books[mid] <= target:
                best_j = mid
                low = mid + 1
            else:
                high = mid - 1
        
        # If a valid previous book exists, add 1 to its DP value.
        res_include = 1 + (dp[best_j] if best_j != -1 else 0)
        
        # The max for the current index is the better of including or excluding the book.
        dp[i] = max(res_exclude, res_include)
        
    return dp[n - 1]
