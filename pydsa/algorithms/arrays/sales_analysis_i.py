METADATA = {
    "id": 1082,
    "name": "Sales Analysis I",
    "slug": "sales_analysis_i",
    "category": "Database",
    "aliases": [],
    "tags": ["sql", "join"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Compute total sales amount per product by joining sales and product tables.",
}

def solve(sales: list[dict], products: list[dict]) -> list[tuple[str, int]]:
    """Compute total sales amount per product.

    Args:
        sales: A list of dictionaries, each representing a row in the Sales table
            with keys 'product_id' (int), 'quantity' (int), and 'price' (int).
        products: A list of dictionaries, each representing a row in the Product table
            with keys 'product_id' (int) and 'product_name' (str).

    Returns:
        A list of tuples (product_name, total_amount) sorted by total_amount descending
        and then product_name ascending.

    Examples:
        >>> sales = [
        ...     {"product_id": 1, "quantity": 10, "price": 100},
        ...     {"product_id": 2, "quantity": 5, "price": 200},
        ...     {"product_id": 1, "quantity": 3, "price": 100},
        ... ]
        >>> products = [
        ...     {"product_id": 1, "product_name": "Apple"},
        ...     {"product_id": 2, "product_name": "Banana"},
        ... ]
        >>> solve(sales, products)
        [('Apple', 1300), ('Banana', 1000)]
    """
    # Build a mapping from product_id to product_name for quick lookup.
    product_name_by_id: dict[int, str] = {}
    for product in products:
        product_name_by_id[product["product_id"]] = product["product_name"]

    # Aggregate total sales amount per product_id.
    total_amount_by_id: dict[int, int] = {}
    for record in sales:
        product_id = record["product_id"]
        amount = record["quantity"] * record["price"]
        total_amount_by_id[product_id] = total_amount_by_id.get(product_id, 0) + amount

    # Combine product names with aggregated amounts.
    result: list[tuple[str, int]] = []
    for product_id, total_amount in total_amount_by_id.items():
        product_name = product_name_by_id.get(product_id, "")
        result.append((product_name, total_amount))

    # Sort by total_amount descending, then product_name ascending.
    result.sort(key=lambda x: (-x[1], x[0]))
    return result