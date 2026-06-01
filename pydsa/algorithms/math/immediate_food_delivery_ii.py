METADATA = {
    "id": 1174,
    "name": "Immediate Food Delivery II",
    "slug": "immediate-food-delivery-ii",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "group_by"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the percentage of immediate orders among the first orders of all customers.",
}

def solve(delivery_table: list[dict]) -> float:
    """
    Calculates the percentage of immediate orders among the first orders of all customers.
    
    An order is 'immediate' if the order_date is the same as the customer_pref_delivery_date.
    The 'first order' is the order with the earliest order_date for each customer.

    Args:
        delivery_table: A list of dictionaries where each dictionary represents a delivery.
            Each dict contains:
            - 'customer_id' (int)
            - 'order_date' (str, format 'YYYY-MM-DD')
            - 'customer_pref_delivery_date' (str, format 'YYYY-MM-DD')

    Returns:
        float: The percentage of immediate first orders rounded to two decimal places.

    Examples:
        >>> table = [
        ...     {"customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"},
        ...     {"customer_id": 2, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"},
        ...     {"customer_id": 1, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-11"}
        ... ]
        >>> solve(table)
        50.0
    """
    if not delivery_table:
        return 0.0

    # Map to store the earliest order date for each customer
    # customer_id -> earliest_order_date
    first_order_dates: dict[int, str] = {}

    for row in delivery_table:
        cust_id = row["customer_id"]
        order_date = row["order_date"]
        
        # Update the map if this is the first time seeing the customer 
        # or if we found an earlier order date
        if cust_id not in first_order_dates or order_date < first_order_dates[cust_id]:
            first_order_dates[cust_id] = order_date

    immediate_first_orders_count = 0
    total_customers = len(first_order_dates)

    # Iterate through the table again to identify which of the first orders were immediate
    # We use a set of (customer_id, order_date) to ensure we only count each customer's first order once
    # even if they had multiple orders on that same earliest date.
    processed_customers = set()

    for row in delivery_table:
        cust_id = row["customer_id"]
        order_date = row["order_date"]
        pref_date = row["customer_pref_delivery_date"]

        # Check if this row is the identified first order for this customer
        if cust_id not in processed_customers and order_date == first_order_dates[cust_id]:
            # If the order date matches the preferred delivery date, it is immediate
            if order_date == pref_date:
                immediate_first_orders_count += 1
            
            # Mark customer as processed so we don't count multiple orders on the same first day
            processed_customers.add(cust_id)

    # Calculate percentage and round to 2 decimal places
    percentage = (immediate_first_orders_count / total_customers) * 100
    return round(percentage, 2)
