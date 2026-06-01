METADATA = {
    "id": 1083,
    "name": "Sales Analysis II",
    "slug": "sales_analysis_ii",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "join"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Retrieve the product name and total quantity sold for products with a total quantity sold greater than 100.",
}

def solve(sales: list[dict], products: list[dict]) -> list[dict]:
    """
    Simulates the SQL query to find product names and their total quantities sold,
    filtering for those where the total quantity is greater than 100.

    Args:
        sales: A list of dictionaries representing the Sales table.
               Each dict contains 'product_id' and 'quantity'.
        products: A list of dictionaries representing the Product table.
                  Each dict contains 'product_id' and 'product_name'.

    Returns:
        A list of dictionaries containing 'product_name' and 'total_quantity'
        for products meeting the criteria.

    Examples:
        >>> sales = [{'product_id': 1, 'quantity': 50}, {'product_id': 1, 'quantity': 60}, {'product_id': 2, 'quantity': 30}]
        >>> products = [{'product_id': 1, 'product_name': 'Apple'}, {'product_id': 2, 'product_name': 'Banana'}]
        >>> solve(sales, products)
        [{'product_name': 'Apple', 'total_quantity': 110}]
    """
    # Step 1: Aggregate quantities by product_id using a hash map (dictionary)
    # This simulates the GROUP BY product_id clause in SQL
    quantity_map: dict[int, int] = {}
    for sale in sales:
        pid = sale["product_id"]
        qty = sale["quantity"]
        quantity_map[pid] = quantity_map.get(pid, 0) + qty

    # Step 2: Create a lookup for product names to simulate the JOIN operation
    # This allows O(1) access to names during the final aggregation/filtering
    name_lookup: dict[int, str] = {p["product_id"]: p["product_name"] for p in products}

    results: list[dict] = []

    # Step 3: Iterate through the aggregated quantities, join with names, 
    # and apply the HAVING clause (total_quantity > 100)
    for pid, total_qty in quantity_map.items():
        if total_qty > 100:
            # Ensure the product exists in the product table (Inner Join behavior)
            if pid in name_lookup:
                results.append({
                    "product_name": name_lookup[pid],
                    "total_quantity": total_qty
                })

    return results
