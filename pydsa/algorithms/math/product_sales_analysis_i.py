METADATA = {
    "id": 1068,
    "name": "Product Sales Analysis I",
    "slug": "product_sales_analysis_i",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Return product name, year, and quantity sold for each product, sorted by name and year.",
}


def solve(product: list[list[object]], sales: list[list[object]]) -> list[list[object]]:
    """Return product name, year, and quantity sold for each product.

    Args:
        product: A list of rows where each row is [product_id, product_name].
        sales: A list of rows where each row is [product_id, year, quantity].

    Returns:
        A list of rows [[product_name, year, quantity], ...] sorted first by
        product_name (ascending) then by year (ascending).

    Examples:
        >>> product = [[1, "ProductA"], [2, "ProductB"]]
        >>> sales = [[1, 2020, 10], [2, 2020, 5], [1, 2021, 7]]
        >>> solve(product, sales)
        [['ProductA', 2020, 10], ['ProductA', 2021, 7], ['ProductB', 2020, 5]]
    """
    # Build a hash map from product_id to product_name for O(1) look‑ups.
    product_name_by_id: dict[int, str] = {}
    for product_id, product_name in product:
        product_name_by_id[int(product_id)] = str(product_name)

    # Combine sales rows with product names.
    combined: list[list[object]] = []
    for sale_product_id, sale_year, sale_quantity in sales:
        name = product_name_by_id[int(sale_product_id)]
        combined.append([name, int(sale_year), int(sale_quantity)])

    # Sort by product name then by year.
    combined.sort(key=lambda row: (row[0], row[1]))
    return combined