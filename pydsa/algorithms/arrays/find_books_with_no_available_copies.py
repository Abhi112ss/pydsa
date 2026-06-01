METADATA = {
    "id": 3570,
    "name": "Find Books with No Available Copies",
    "slug": "find_books_with_no_available_copies",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify books from a master list that do not appear in the list of available copies.",
}

def solve(all_books: list[int], available_copies: list[int]) -> list[int]:
    """
    Identifies books from the master list that have zero available copies.

    Args:
        all_books: A list of integers representing the IDs of all books in the library.
        available_copies: A list of integers representing the IDs of books currently available.

    Returns:
        A sorted list of book IDs that are present in all_books but not in available_copies.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [2, 4])
        [1, 3, 5]
        >>> solve([10, 20, 30], [10, 20, 30])
        []
        >>> solve([1, 1, 2], [2])
        [1]
    """
    # Convert available_copies to a set for O(1) average time complexity lookups
    available_set = set(available_copies)
    
    # Use a set for all_books to handle potential duplicates in the master list 
    # and ensure we only check unique book IDs
    unique_all_books = set(all_books)
    
    missing_books = []
    
    # Iterate through the unique books and check if they exist in the available set
    for book_id in unique_all_books:
        if book_id not in available_set:
            missing_books.append(book_id)
            
    # Return the result sorted as per standard requirement for such problems
    return sorted(missing_books)
