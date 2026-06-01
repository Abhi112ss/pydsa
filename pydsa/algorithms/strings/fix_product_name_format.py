METADATA = {
    "id": 1543,
    "name": "Fix Product Name Format",
    "slug": "fix-product-name-format",
    "category": "String",
    "aliases": [],
    "tags": ["string", "manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Transform a product name by capitalizing the first letter, making the rest lowercase, and replacing all hyphens with spaces.",
}

def solve(product_name: str) -> str:
    """
    Transforms the product name according to specific formatting rules.
    
    Rules:
    1. The first character must be uppercase.
    2. All other characters must be lowercase.
    3. All hyphens ('-') must be replaced with spaces (' ').

    Args:
        product_name: The original product name string.

    Returns:
        The formatted product name string.

    Examples:
        >>> solve("leet-code-platform")
        'Leet code platform'
        >>> solve("a-b-c")
        'A b c'
        >>> solve("PRODUCT-NAME")
        'Product name'
    """
    if not product_name:
        return ""

    # Replace all hyphens with spaces first to handle the delimiter requirement
    replaced_name = product_name.replace("-", " ")

    # Capitalize the first letter and ensure the rest are lowercase.
    # Python's .capitalize() method does exactly this: 
    # it converts the first character to uppercase and the rest to lowercase.
    return replaced_name.capitalize()
