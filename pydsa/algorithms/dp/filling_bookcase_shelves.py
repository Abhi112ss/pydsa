METADATA = {
    "id": 1105,
    "name": "Filling Bookcase Shelves",
    "slug": "filling-bookcase-shelves",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum height of a bookcase by placing books on shelves such that each shelf's width does not exceed a given limit.",
}

def solve(books: list[int], shelf_width: int) -> int:
    """
    Calculates the minimum height required to store books on shelves.

    Args:
        books: A list of integers representing the width of each book.
        shelf_width: The maximum width allowed for a single shelf.

    Returns:
        The minimum total height of the bookcase.

    Examples:
        >>> solve([1, 3, 3, 2], 4)
        4
        >>> solve([4, 4, 4, 4], 4)
        4
        >>> solve([1, 2, 3, 4, 5, 6], 10)
        6
    """
    n = len(books)
    # dp[i] represents the minimum height for the first i books.
    # We initialize with a large value (infinity).
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        current_shelf_width = 0
        current_shelf_height = 0
        
        # Try placing the i-th book (index i-1) on a new shelf,
        # and then try to include previous books (j) on the same shelf.
        for j in range(i, 0, -1):
            book_width = books[j - 1]
            current_shelf_width += book_width
            
            # If the current set of books exceeds the shelf width, we cannot
            # add more books to this specific shelf configuration.
            if current_shelf_width > shelf_width:
                break
            
            # The height of the current shelf is the height of the tallest book on it.
            current_shelf_height = max(current_shelf_height, book_width)
            
            # The total height is the height of the current shelf + 
            # the minimum height of all books placed before this shelf.
            dp[i] = min(dp[i], dp[j - 1] + current_shelf_height)

    return int(dp[n])
