METADATA = {
    "id": 2306,
    "name": "Naming a Company",
    "slug": "naming-a-company",
    "category": "Simulation",
    "aliases": [],
    "tags": ["strings", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a company name based on a set of rules involving prefixes, suffixes, and a separator.",
}

def solve(companyName: str, prefix: str, suffix: str) -> str:
    """
    Constructs a company name based on specific rules.

    Rules:
    1. If the name is empty, return prefix + separator + suffix.
    2. If the name is not empty, return prefix + separator + name + separator + suffix.
    3. The separator is always " - ".

    Args:
        companyName: The existing name of the company.
        prefix: The prefix to be added.
        suffix: The suffix to be added.

    Returns:
        The newly constructed company name.

    Examples:
        >>> solve("", "abc", "def")
        'abc - def'
        >>> solve("g", "abc", "def")
        'abc - g - def'
    """
    separator = " - "
    
    # If companyName is empty, we only need prefix and suffix joined by the separator
    if not companyName:
        return f"{prefix}{separator}{suffix}"
    
    # If companyName exists, we sandwich it between the prefix and suffix
    return f"{prefix}{separator}{companyName}{separator}{suffix}"
