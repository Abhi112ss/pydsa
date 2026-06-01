METADATA = {
    "id": 1069,
    "name": "Product Sales Analysis II",
    "slug": "product-sales-analysis-ii",
    "category": "Database/Simulation",
    "aliases": [],
    "tags": ["hash_map", "arrays", "aggregation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a list of sales records, find the first sale record for each unique product.",
}

def solve(sales: list[dict]) -> list[dict]:
    """
    Finds the first sale record for each unique product based on the sale_date.

    Args:
        sales: A list of dictionaries, where each dictionary represents a sale 
               containing 'product_id', 'year', 'quantity', and 'price'.

    Returns:
        A list of dictionaries containing the first sale record for each product.

    Examples:
        >>> sales = [
        ...     {"product_id": 100, "year": 2008, "quantity": 10, "price": 50},
        ...     {"product_id": 100, "year": 2009, "quantity": 12, "price": 55},
        ...     {"product_id": 200, "year": 2011, "quantity": 15, "price": 100}
        ... ]
        >>> solve(sales)
        [{'product_id': 100, 'year': 2008, 'quantity': 10, 'price': 50}, 
         {'product_id': 200, 'year': 2011, 'quantity': 15, 'price': 100}]
    """
    # Map to store the earliest sale record found so far for each product_id
    # Key: product_id, Value: sale_record_dict
    first_sales_map: dict[int, dict] = {}

    for record in sales:
        product_id = record["product_id"]
        
        # If product is not in map, or current record is earlier than the stored one
        # Note: In a real SQL scenario, we'd use MIN(sale_date). 
        # Since the input is a list of dicts, we assume 'year' acts as the temporal key.
        if product_id not in first_sales_map:
            first_sales_map[product_id] = record
        else:
            # Compare years to ensure we keep the record with the minimum year
            if record["year"] < first_sales_map[product_id]["year"]:
                first_sales_map[product_id] = record

    # Convert the hash map values back into a list for the final result
    return list(first_sales_map.values())
