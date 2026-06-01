METADATA = {
    "id": 929,
    "name": "Unique Email Addresses",
    "slug": "unique_email_addresses",
    "category": "Array",
    "aliases": [],
    "tags": ["string", "hash_set"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Count the number of unique email addresses after normalizing the local part by removing dots and truncating at the first plus sign.",
}


def solve(emails: list[str]) -> int:
    """Count unique email addresses after applying normalization rules.

    Each email consists of a local name and a domain name separated by '@'.
    In the local name:
      - Dots ('.') are ignored.
      - Everything after the first plus ('+') is ignored.
    The domain name is taken as-is.

    Args:
        emails: A list of email address strings.

    Returns:
        The number of unique email addresses after normalization.

    Examples:
        >>> solve(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"])
        2
        >>> solve(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"])
        3
        >>> solve(["test.email+alex@leetcode.com", "test.email@leetcode.com"])
        1
    """
    unique_addresses: set[str] = set()

    for email in emails:
        # Split the email into local and domain parts at the '@' symbol.
        local_part, domain_part = email.split("@")

        # Truncate the local part at the first '+' character, if any.
        if "+" in local_part:
            local_part = local_part[: local_part.index("+")]

        # Remove all dots from the local part.
        normalized_local = local_part.replace(".", "")

        # Reconstruct the full normalized email and add it to the set.
        normalized_email = f"{normalized_local}@{domain_part}"
        unique_addresses.add(normalized_email)

    return len(unique_addresses)