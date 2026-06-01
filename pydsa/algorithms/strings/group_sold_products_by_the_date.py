METADATA = {
    "id": 1484,
    "name": "Group Sold Products By The Date",
    "slug": "group-sold-products-by-the-date",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Group product names by their sale dates and return them sorted by date and then by product name.",
}

def solve(sold_items: list[str]) -> dict[str, list[str]]:
    """
    Groups products by their sale dates and returns a dictionary where keys are dates
    and values are sorted lists of product names.

    Args:
        sold_items: A list of strings where each string is formatted as "ProductCode Date".

    Returns:
        A dictionary where keys are dates (strings) and values are sorted lists 
        of product names (strings).

    Examples:
        >>> solve(["L04 20210101", "L04 20210101", "L01 20210101"])
        {'20210101': ['L01', 'L04', 'L04']}
        >>> solve(["L04 20210101", "L04 20210102", "L01 20210101"])
        {'20210101': ['L01', 'L04'], '20210102': ['L04']}
    """
    # Map to store date -> list of product names
    date_to_products: dict[str, list[str]] = {}

    for item in sold_items:
        # Split each entry into product code and date
        product_code, sale_date = item.split(" ")
        
        if sale_date not in date_to_products:
            date_to_products[sale_date] = []
        
        date_to_products[sale_date].append(product_code)

    # Sort the product names for each date to satisfy the requirement
    # The problem requires the list of products to be sorted lexicographically
    for sale_date in date_to_products:
        date_to_products[sale_date].sort()

    return date_to_products
