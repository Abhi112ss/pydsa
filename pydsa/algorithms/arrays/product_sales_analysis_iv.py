METADATA = {
    "id": 2324,
    "name": "Product Sales Analysis IV",
    "slug": "product-sales-analysis-iv",
    "category": "SQL Logic Simulation",
    "aliases": [],
    "tags": ["filtering", "grouping", "aggregation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of orders sold in the first year for each product.",
}

from typing import Optional


def solve(sales: list[dict[str, int]]) -> dict[int, int]:
    """
    Calculates the number of orders sold in the first year for each product.

    Args:
        sales: A list of dictionaries where each dictionary represents a sale.
               Each dictionary contains 'product_id', 'year', and 'quantity'.

    Returns:
        A dictionary where keys are product_ids and values are the count of 
        orders (rows) that occurred in that product's minimum year.

    Examples:
        >>> sales = [
        ...     {"product_id": 100, "year": 2008, "quantity": 10},
        ...     {"product_id": 100, "year": 2009, "quantity": 12},
        ...     {"product_id": 100, "year": 2008, "quantity": 15},
        ...     {"product_id": 200, "year": 2011, "quantity": 20}
        ... ]
        >>> solve(sales)
        {100: 2, 200: 1}
    """
    if not sales:
        return {}

    # Step 1: Find the minimum year for each product
    # product_min_year maps product_id -> min_year
    product_min_year: dict[int, int] = {}
    for sale in sales:
        pid = sale["product_id"]
        year = sale["year"]
        if pid not in product_min_year or year < product_min_year[pid]:
            product_min_year[pid] = year

    # Step 2: Count occurrences of sales that happened in that minimum year
    # product_first_year_count maps product_id -> count of orders in min_year
    product_first_year_count: dict[int, int] = {}
    
    # Initialize all products found in the dataset to 0 to ensure all products are represented
    for pid in product_min_year:
        product_first_year_count[pid] = 0

    for sale in sales:
        pid = sale["product_id"]
        year = sale["year"]
        
        # If the current sale's year matches the product's first year, increment count
        if year == product_min_year[pid]:
            product_first_year_count[pid] += 1

    return product_first_year_count
