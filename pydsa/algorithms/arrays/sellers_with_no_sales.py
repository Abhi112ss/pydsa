METADATA = {
    "id": 1607,
    "name": "Sellers With No Sales",
    "slug": "sellers-with-no-sales",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Find all seller IDs that do not appear in the sales list.",
}

def solve(seller_id: list[int], product_id: list[int], seller_id_sales: list[int], product_id_sales: list[int]) -> list[int]:
    """
    Identifies sellers who have not made any sales.

    Args:
        seller_id: A list of all available seller IDs.
        product_id: A list of all available product IDs (not used in this logic).
        seller_id_sales: A list of seller IDs present in the sales records.
        product_id_sales: A list of product IDs present in the sales records (not used in this logic).

    Returns:
        A list of seller IDs that do not appear in the seller_id_sales list, 
        sorted in ascending order.

    Examples:
        >>> solve([4, 2, 5, 5, 1], [1, 2, 3, 4, 5], [1, 2, 4, 4], [5, 4, 3, 1])
        [2, 5]
        >>> solve([1, 2, 3], [1, 2, 3], [1, 2], [1, 2])
        [3]
    """
    # Convert the list of sellers who made sales into a set for O(1) average lookup time
    sellers_with_sales = set(seller_id_sales)
    
    # Identify sellers from the master list who are not in the sales set
    no_sales_sellers = []
    for seller in seller_id:
        if seller not in sellers_with_sales:
            no_sales_sellers.append(seller)
            
    # The problem requires the result to be sorted in ascending order
    no_sales_sellers.sort()
    
    return no_sales_sellers
