METADATA = {
    "id": 2474,
    "name": "Customers With Strictly Increasing Purchases",
    "slug": "customers-with-strictly-increasing-purchases",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of customers whose purchase amounts are strictly increasing over time.",
}

def solve(purchases: list[list[int]]) -> int:
    """
    Counts how many customers have a sequence of purchase amounts that is strictly increasing.

    Args:
        purchases: A list of lists, where each inner list represents a customer's 
                   purchase history [customer_id, purchase_amount].

    Returns:
        The total count of customers whose purchase amounts are strictly increasing.

    Examples:
        >>> solve([[1, 10], [2, 5], [1, 15], [2, 10], [1, 20]])
        2
        >>> solve([[1, 10], [1, 10], [1, 10]])
        0
    """
    # Map to store the last purchase amount for each customer
    # and a flag to track if they have already failed the strictly increasing condition.
    # customer_id -> [last_amount, is_valid]
    customer_status: dict[int, list[float]] = {}
    
    # To handle the "strictly increasing" requirement, we need to know if a customer
    # has ever had a purchase that was less than or equal to their previous purchase.
    # We use a dictionary to track the last amount and a set to track "invalid" customers.
    last_amounts: dict[int, int] = {}
    invalid_customers: set[int] = set()
    all_customers: set[int] = set()

    for customer_id, amount in purchases:
        all_customers.add(customer_id)
        
        if customer_id in last_amounts:
            # If the current amount is not strictly greater than the previous,
            # mark this customer as invalid.
            if amount <= last_amounts[customer_id]:
                invalid_customers.add(customer_id)
        
        # Update the last known purchase amount for this customer
        last_amounts[customer_id] = amount

    # Count customers who are in the set of all customers but NOT in the invalid set
    increasing_count = 0
    for customer_id in all_customers:
        if customer_id not in invalid_customers:
            increasing_count += 1
            
    return increasing_count
