METADATA = {
    "id": 811,
    "name": "Subdomain Visit Count",
    "slug": "subdomain_visit_count",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string_parsing"],
    "difficulty": "easy",
    "time_complexity": "O(n * l)",
    "space_complexity": "O(n * l)",
    "description": "Given a list of count-paired domains, return the count-paired domains for each subdomain.",
}

def solve(cpdomains: list[str]) -> list[str]:
    """Return count-paired domains for each subdomain.

    Args:
        cpdomains: List of strings in the format "count domain" (e.g., "9001 discuss.leetcode.com").

    Returns:
        List of strings in the format "count subdomain" for each subdomain.

    Examples:
        >>> solve(["9001 discuss.leetcode.com"])
        ['9001 discuss.leetcode.com', '9001 leetcode.com', '9001 com']
        >>> solve(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
        ['901 mail.com', '50 yahoo.com', '900 google.mail.com', '5 wiki.org', '5 org', '1 intel.mail.com', '951 com']
    """
    subdomain_counts: dict[str, int] = {}

    for cpdomain in cpdomains:
        # Split the count and domain parts
        count_str, domain = cpdomain.split(" ")
        count = int(count_str)

        # Split domain into parts and iterate through all subdomain levels
        parts = domain.split(".")
        for i in range(len(parts)):
            # Reconstruct subdomain from index i to end (e.g., "discuss.leetcode.com", "leetcode.com", "com")
            subdomain = ".".join(parts[i:])
            subdomain_counts[subdomain] = subdomain_counts.get(subdomain, 0) + count

    # Format the result as "count subdomain" strings
    result = [f"{count} {subdomain}" for subdomain, count in subdomain_counts.items()]
    return result