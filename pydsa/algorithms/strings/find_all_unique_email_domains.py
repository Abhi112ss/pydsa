METADATA = {
    "id": 3059,
    "name": "Find All Unique Email Domains",
    "slug": "find-all-unique-email-domains",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "hash_set"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Extract and return all unique domains from a list of email addresses.",
}

def solve(emails: list[str]) -> list[str]:
    """
    Extracts all unique domains from a list of email addresses.

    Args:
        emails: A list of strings where each string is a valid email address.

    Returns:
        A list of unique domain strings extracted from the input emails.

    Examples:
        >>> solve(["user@gmail.com", "admin@yahoo.com", "test@gmail.com"])
        ['gmail.com', 'yahoo.com']
        >>> solve(["a@b.c", "d@e.f"])
        ['b.c', 'e.f']
    """
    # Use a set to automatically handle uniqueness of the domains
    unique_domains = set()

    for email in emails:
        # Split the email at the '@' character. 
        # Since it's a valid email, there will be exactly one '@' separating local and domain parts.
        parts = email.split('@')
        
        # The domain is the second part of the split result
        domain = parts[1]
        unique_domains.add(domain)

    # Convert the set back to a list for the return type
    return list(unique_domains)
