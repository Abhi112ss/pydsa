METADATA = {
    "id": 1098,
    "name": "Unpopular Books",
    "slug": "unpopular_books",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "group_by", "filtering"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the book IDs that have the minimum number of readers.",
}

def solve(readers: list[dict[str, int]]) -> list[int]:
    """
    Finds the book IDs that have the minimum number of readers.

    Args:
        readers: A list of dictionaries where each dictionary represents a 
                 reading record with 'book_id' and 'user_id'.

    Returns:
        A list of integers representing the book IDs with the minimum reader count,
        sorted in ascending order.

    Examples:
        >>> readers = [{"book_id": 1, "user_id": 1}, {"book_id": 1, "user_id": 2}, {"book_id": 2, "user_id": 1}]
        >>> solve(readers)
        [2]
        >>> readers = [{"book_id": 1, "user_id": 1}, {"book_id": 2, "user_id": 2}]
        >>> solve(readers)
        [1, 2]
    """
    if not readers:
        return []

    # Step 1: Count the number of readers for each book_id
    book_counts: dict[int, int] = {}
    for record in readers:
        book_id = record["book_id"]
        book_counts[book_id] = book_counts.get(book_id, 0) + 1

    # Step 2: Find the minimum reader count among all books
    min_readers = min(book_counts.values())

    # Step 3: Collect all book_ids that have this minimum count
    unpopular_books = [
        book_id 
        for book_id, count in book_counts.items() 
        if count == min_readers
    ]

    # Return the result sorted as per standard SQL behavior for such problems
    return sorted(unpopular_books)
