METADATA = {
    "id": 3358,
    "name": "Books with NULL Ratings",
    "slug": "books-with-null-ratings",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Identify indices of elements that follow a specific pattern of being null or non-null.",
}

def solve(ratings: list[int | None]) -> list[int]:
    """
    Identifies the indices of books that have a 'NULL' rating pattern.
    
    A book is considered to have a NULL rating if its rating is None.
    The problem asks for the indices of all such books.

    Args:
        ratings: A list of integers or None representing book ratings.

    Returns:
        A list of integers representing the indices where the rating is None.

    Examples:
        >>> solve([1, None, 3, None, 5])
        [1, 3]
        >>> solve([None, None, None])
        [0, 1, 2]
        >>> solve([1, 2, 3])
        []
    """
    null_indices = []
    
    # Iterate through the list once to find all occurrences of None
    for index, rating in enumerate(ratings):
        # Check if the current rating is None (representing NULL)
        if rating is None:
            null_indices.append(index)
            
    return null_indices
