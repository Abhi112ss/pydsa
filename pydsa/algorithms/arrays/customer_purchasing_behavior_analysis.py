METADATA = {
    "id": 3230,
    "name": "Customer Purchasing Behavior Analysis",
    "slug": "customer-purchasing-behavior-analysis",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["arrays", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Analyze customer purchasing behavior by counting the frequency of specific product purchases per customer.",
}

def solve(transactions: list[dict[str, str]], target_product: str) -> dict[str, int]:
    """
    Analyzes transaction data to find how many times each customer purchased a specific product.

    Args:
        transactions: A list of dictionaries where each dictionary represents a transaction
            containing 'customer_id' and 'product_id'.
        target_product: The specific product ID to count for each customer.

    Returns:
        A dictionary mapping customer_id to the count of times they purchased the target_product.
        Only customers who purchased the target_product at least once are included.

    Examples:
        >>> txs = [
        ...     {"customer_id": "C1", "product_id": "P1"},
        ...     {"customer_id": "C1", "product_id": "P2"},
        ...     {"customer_id": "C2", "product_id": "P1"},
        ...     {"customer_id": "C1", "product_id": "P1"}
        ... ]
        >>> solve(txs, "P1")
        {'C1': 2, 'C2': 1}
    """
    # Dictionary to store the frequency of the target product per customer
    purchase_counts: dict[str, int] = {}

    for transaction in transactions:
        customer_id = transaction.get("customer_id")
        product_id = transaction.get("product_id")

        # Check if the current transaction involves the product we are interested in
        if product_id == target_product:
            # Increment the count for this customer, initializing to 0 if not present
            purchase_counts[customer_id] = purchase_counts.get(customer_id, 0) + 1

    return purchase_counts
