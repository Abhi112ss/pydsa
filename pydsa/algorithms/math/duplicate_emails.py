METADATA = {
    "id": 182,
    "name": "Duplicate Emails",
    "slug": "duplicate_emails",
    "category": "database",
    "aliases": [],
    "tags": ["sql", "group_by"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all duplicate emails in a list of records.",
}


def solve(emails: list[str]) -> list[str]:
    """Finds all emails that appear more than once in the input list.

    Args:
        emails: A list of email strings.

    Returns:
        A list of strings containing emails that appear at least twice.

    Examples:
        >>> solve(["a@b.com", "c@d.com", "a@b.com"])
        ['a@b.com']
    """
    # Use a dictionary to store the frequency of each email
    email_counts: dict[str, int] = {}

    # Iterate through the list once to count occurrences
    for email in emails:
        email_counts[email] = email_counts.get(email, 0) + 1

    # Filter the dictionary for emails with a count greater than one
    duplicate_emails: list[str] = [
        email for email, count in email_counts.items() if count > 1
    ]

    return duplicate_emails
