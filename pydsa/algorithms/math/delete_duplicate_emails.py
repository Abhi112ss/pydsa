METADATA = {
    "id": 196,
    "name": "Delete Duplicate Emails",
    "slug": "delete_duplicate_emails",
    "category": "Database",
    "aliases": [],
    "tags": ["sql"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Delete all duplicate email entries in a Person table, keeping only the entry with the smallest id.",
}

def solve() -> str:
    """
    Returns the SQL query to delete duplicate emails, keeping the row with the smallest id.

    Args:
        None

    Returns:
        str: The SQL DELETE statement as a string.

    Examples:
        >>> solve()
        'DELETE p1 FROM Person p1, Person p2 WHERE p1.Email = p2.Email AND p1.Id > p2.Id;'
    """
    # Self-join the Person table on matching emails
    # Delete rows where the id is greater than the matching row's id
    # This keeps only the row with the smallest id for each email
    query = "DELETE p1 FROM Person p1, Person p2 WHERE p1.Email = p2.Email AND p1.Id > p2.Id;"
    return query