METADATA = {
    "id": 3642,
    "name": "Find Books with Polarized Opinions",
    "slug": "find_books_with_polarized_opinions",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "filtering"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify books where the ratings do not contain any neutral values within their range.",
}

def solve(ratings: list[list[int]], neutral_values: list[int]) -> list[int]:
    """
    Identifies the indices of books that have polarized opinions.
    A book is polarized if none of its rating values are present in the neutral_values list.

    Args:
        ratings: A list of lists, where each inner list contains the ratings for a book.
        neutral_values: A list of integers representing values considered neutral.

    Returns:
        A list of indices of the books that are polarized.

    Examples:
        >>> solve([[1, 2, 5], [1, 3, 5], [2, 4, 6]], [3])
        [0, 2]
        >>> solve([[1, 2], [3, 4], [5, 6]], [1, 3, 5])
        []
    """
    # Convert neutral_values to a set for O(1) average time complexity lookups
    neutral_set = set(neutral_values)
    polarized_book_indices = []

    for index, book_ratings in enumerate(ratings):
        is_polarized = True
        
        # Check if any rating in the current book is in the neutral set
        for rating in book_ratings:
            if rating in neutral_set:
                is_polarized = False
                break
        
        # If no neutral rating was found, the book is polarized
        if is_polarized:
            polarized_book_indices.append(index)

    return polarized_book_indices
