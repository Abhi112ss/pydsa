METADATA = {
    "id": 1677,
    "name": "Product's Worth Over Invoices",
    "slug": "product_worth_over_invoices",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate total worth by summing price multiplied by quantity for each invoice.",
}


def solve(invoices: list[list[int]]) -> int:
    """Calculate the total worth of all invoices.

    Args:
        invoices: A list where each element is a two‑element list
                  [price, quantity] representing a single invoice.

    Returns:
        The sum of price * quantity for all invoices.

    Examples:
        >>> solve([[10, 2], [5, 3]])
        35
        >>> solve([[100, 1], [200, 2], [50, 4]])
        800
    """
    total_worth: int = 0
    for invoice in invoices:
        price, quantity = invoice  # unpack price and quantity
        total_worth += price * quantity  # accumulate product
    return total_worth