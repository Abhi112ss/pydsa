METADATA = {
    "id": 3860,
    "name": "Unique Email Groups",
    "slug": "unique_email_groups",
    "category": "String",
    "aliases": [],
    "tags": ["string", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Count the number of unique email addresses after normalizing them by handling special characters in the local name.",
}

def solve(emails: list[str]) -> int:
    """
    Counts the number of unique email addresses after applying normalization rules.

    Normalization rules:
    1. The local name is the part before the '@' symbol.
    2. In the local name, '.' characters are ignored.
    3. In the local name, '+' characters and everything following them are ignored.
    4. The domain name is the part after the '@' symbol and remains unchanged.

    Args:
        emails: A list of strings representing email addresses.

    Returns:
        The count of unique normalized email addresses.

    Examples:
        >>> solve(["test.email+alex@leetcode.com", "test.e.mail+bob@leetcode.com", "testemail+david@lee.tcode.com"])
        2
        >>> solve(["a@b.com", "b@c.com", "c@d.com"])
        3
    """
    unique_emails = set()

    for email in emails:
        # Split the email into local name and domain parts
        local_part, domain_part = email.split("@")

        # Handle the '+' rule: ignore everything from the first '+' onwards
        if "+" in local_part:
            local_part = local_part.split("+")[0]

        # Handle the '.' rule: remove all dots from the local name
        local_part = local_part.replace(".", "")

        # Reconstruct the normalized email
        normalized_email = f"{local_part}@{domain_part}"
        
        # Add to set to ensure uniqueness
        unique_emails.add(normalized_email)

    return len(unique_emails)
