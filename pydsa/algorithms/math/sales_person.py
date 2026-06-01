METADATA = {
    "id": 607,
    "name": "Sales Person",
    "slug": "sales_person",
    "category": "Database",
    "aliases": [],
    "tags": ["set_difference", "filtering"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n)",
    "description": "Return names of salespersons who have never sold the product 'RED'.",
}


def solve(sales: list[list[object]], orders: list[list[object]]) -> list[str]:
    """Return the names of salespersons who have never sold the product 'RED'.

    Args:
        sales: A list of rows representing the SalesPerson table.
            Each row is expected to be [sales_id, name, sales_city, salary].
        orders: A list of rows representing the Orders table.
            Each row is expected to be [order_id, order_date, customer_id, product, amount].

    Returns:
        A list of salesperson names sorted in ascending alphabetical order
        who have not made any order for the product 'RED'.

    Examples:
        >>> sales = [
        ...     [1, "John", "New York", 5000],
        ...     [2, "Jane", "Los Angeles", 6000],
        ...     [3, "Doe", "Chicago", 5500]
        ... ]
        >>> orders = [
        ...     [101, "2023-01-01", 1, "RED", 100],
        ...     [102, "2023-01-02", 2, "BLUE", 150]
        ... ]
        >>> solve(sales, orders)
        ['Doe', 'Jane']
    """
    # Map each sales_id to its corresponding name.
    sales_id_to_name: dict[int, str] = {}
    for row in sales:
        sales_id = int(row[0])          # sales_id is the first column
        name = str(row[1])              # name is the second column
        sales_id_to_name[sales_id] = name

    # Collect all sales_id values that have sold the product 'RED'.
    red_product_sales_ids: set[int] = set()
    for row in orders:
        sales_id = int(row[2])          # customer_id (sales_id) is the third column
        product = str(row[3])           # product is the fourth column
        if product == "RED":
            red_product_sales_ids.add(sales_id)

    # Filter names whose sales_id is not in the RED set and sort them.
    result_names: list[str] = [
        name
        for sales_id, name in sales_id_to_name.items()
        if sales_id not in red_product_sales_ids
    ]
    result_names.sort()
    return result_names