METADATA = {
    "id": 1084,
    "name": "Sales Analysis III",
    "slug": "sales_analysis_iii",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "group_by", "subquery"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all sales records for products that were sold for the very first time on a specific date.",
}

def solve(sales: list[dict], products: list[dict]) -> list[dict]:
    """
    Finds all sales records for products that were sold for the first time on a specific date.
    
    Since this is a SQL problem being implemented in Python, we simulate the 
    relational algebra using dictionaries to achieve O(n) time complexity.

    Args:
        sales: A list of dictionaries representing the 'Sales' table.
               Each dict contains 'sale_id', 'product_id', 'buyer_id', 'seller_id', 'sale_date'.
        products: A list of dictionaries representing the 'Product' table.
                  Each dict contains 'product_id', 'product_name'.

    Returns:
        A list of dictionaries containing 'product_name', 'sale_id', 'buyer_id', 'seller_id', 'sale_date'.

    Examples:
        >>> sales = [
        ...     {"sale_id": 1, "product_id": 100, "buyer_id": 1, "seller_id": 2, "sale_date": "2008-01-01"},
        ...     {"sale_id": 2, "product_id": 100, "buyer_id": 3, "seller_id": 4, "sale_date": "2009-01-01"},
        ...     {"sale_id": 3, "product_id": 200, "buyer_id": 5, "seller_id": 6, "sale_date": "2008-01-01"}
        ... ]
        >>> products = [{"product_id": 100, "product_name": "Nokia"}, {"product_id": 200, "product_name": "Apple"}]
        >>> solve(sales, products)
        [{'product_name': 'Nokia', 'sale_id': 1, 'buyer_id': 1, 'seller_id': 2, 'sale_date': '2008-01-01'},
         {'product_name': 'Apple', 'sale_id': 3, 'buyer_id': 5, 'seller_id': 6, 'sale_date': '2008-01-01'}]
    """
    # Step 1: Find the first sale date for each product
    # We use a dictionary to map product_id -> earliest_sale_date
    first_sale_dates: dict[int, str] = {}
    
    for sale in sales:
        product_id = sale["product_id"]
        current_date = sale["sale_date"]
        
        if product_id not in first_sale_dates or current_date < first_sale_dates[product_id]:
            first_sale_dates[product_id] = current_date

    # Step 2: Map product_id to product_name for efficient lookup
    product_name_map: dict[int, str] = {
        p["product_id"]: p["product_name"] for p in products
    }

    # Step 3: Filter sales that match the first sale date for that product
    # and join with product names
    result: list[dict] = []
    for sale in sales:
        product_id = sale["product_id"]
        # Check if this specific sale record matches the minimum date found in Step 1
        if sale["sale_date"] == first_sale_dates.get(product_id):
            result.append({
                "product_name": product_name_map[product_id],
                "sale_id": sale["sale_id"],
                "buyer_id": sale["buyer_id"],
                "seller_id": sale["seller_id"],
                "sale_date": sale["sale_date"]
            })

    return result