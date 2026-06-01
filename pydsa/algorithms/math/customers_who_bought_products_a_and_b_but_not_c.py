METADATA = {
    "id": 1398,
    "name": "Customers Who Bought Products A and B but Not C",
    "slug": "customers-who-bought-products-a-and-b-but-not-c",
    "category": "Database/Logic",
    "aliases": [],
    "tags": ["math", "logic", "set-theory"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find customers who purchased both product A and product B, but did not purchase product C.",
}

def solve(customer: list[int], product: list[int]) -> list[int]:
    """
    Identifies customers who bought products 'A' (1) and 'B' (2) but not 'C' (3).

    Args:
        customer: A list of customer IDs corresponding to each product purchase.
        product: A list of product IDs corresponding to each customer purchase.

    Returns:
        A list of customer IDs that satisfy the condition.

    Examples:
        >>> solve([1, 2, 3, 3, 4, 4], [1, 2, 1, 2, 3, 3])
        [3]
        >>> solve([1, 2, 3, 1, 2, 3], [1, 2, 3, 2, 1, 1])
        [1, 2]
    """
    # Map each customer to a set of products they have purchased
    customer_purchases: dict[int, set[int]] = {}
    
    for cust_id, prod_id in zip(customer, product):
        if cust_id not in customer_purchases:
            customer_purchases[cust_id] = set()
        customer_purchases[cust_id].add(prod_id)
    
    result: list[int] = []
    
    # Iterate through the grouped purchases to check the logic conditions
    for cust_id, products in customer_purchases.items():
        # Condition: Must have product 1 (A) AND product 2 (B) AND NOT product 3 (C)
        has_a = 1 in products
        has_b = 2 in products
        has_c = 3 in products
        
        if has_a and has_b and not has_c:
            result.append(cust_id)
            
    return result
