METADATA = {
    "id": 1070,
    "name": "Product Sales Analysis III",
    "slug": "product-sales-analysis-iii",
    "category": "Database/SQL Simulation",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all sales records for each product that occurred in its earliest recorded year.",
}

from typing import List, Dict


def solve(sales: List[Dict[str, int]]) -> List[Dict[str, int]]:
    """
    Finds all sales records for each product that occurred in its first year of sales.

    Args:
        sales: A list of dictionaries where each dictionary represents a sale record.
               Each record contains 'product_id', 'year', 'quantity', and 'price'.

    Returns:
        A list of dictionaries containing only the sales records from the 
        earliest year for each product.

    Examples:
        >>> sales = [
        ...     {"product_id": 100, "year": 2008, "quantity": 10, "price": 5000},
        ...     {"product_id": 100, "year": 2009, "quantity": 12, "price": 5000},
        ...     {"product_id": 100, "year": 2008, "quantity": 15, "price": 5000},
        ...     {"product_id": 200, "year": 2011, "quantity": 20, "price": 9000}
        ... ]
        >>> solve(sales)
        [{'product_id': 100, 'year': 2008, 'quantity': 10, 'price': 5000}, 
         {'product_id': 100, 'year': 2008, 'quantity': 15, 'price': 5000}, 
         {'product_id': 200, 'year': 2011, 'quantity': 20, 'price': 9000}]
    """
    if not sales:
        return []

    # Step 1: Identify the minimum year for each product
    # We use a hash map to store product_id -> min_year
    min_years_per_product: Dict[int, int] = {}

    for record in sales:
        product_id = record["product_id"]
        year = record["year"]
        
        if product_id not in min_years_per_product:
            min_years_per_product[product_id] = year
        else:
            if year < min_years_per_product[product_id]:
                min_years_per_product[product_id] = year

    # Step 2: Filter the original sales list
    # Keep only records where the year matches the minimum year found for that product
    result: List[Dict[str, int]] = []
    for record in sales:
        product_id = record["product_id"]
        year = record["year"]
        
        if year == min_years_per_product[product_id]:
            result.append(record)

    return result
