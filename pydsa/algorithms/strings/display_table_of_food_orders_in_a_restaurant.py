METADATA = {
    "id": 1418,
    "name": "Display Table of Food Orders in a Restaurant",
    "slug": "display-table-of-food-orders-in-a-restaurant",
    "category": "Database/Simulation",
    "aliases": [],
    "tags": ["sorting", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Construct a formatted table of food orders sorted by customer and item name.",
}

def solve(customers: list[list[str]], orders: list[list[str]]) -> list[list[str]]:
    """
    Constructs a table of food orders based on customer and order data.

    The table includes a header row of unique food items sorted alphabetically,
    followed by rows for each customer (sorted by ID) containing the quantity
    of each food item ordered.

    Args:
        customers: A list of lists where customers[i] = [customer_id, customer_name].
        orders: A list of lists where orders[i] = [order_id, customer_id, customer_name, food_item, quantity].

    Returns:
        A list of lists of strings representing the formatted table.

    Examples:
        >>> customers = [["1", "David"], ["2", "Corina"]]
        >>> orders = [["1", "1", "David", "Steak", "5"], ["2", "1", "David", "Salad", "3"]]
        >>> solve(customers, orders)
        [['food', 'Steak', 'Salad'], ['David', '5', '3']]
    """
    # Map customer_id to customer_name for quick lookup
    customer_map: dict[str, str] = {}
    for cust_id, cust_name in customers:
        customer_map[cust_id] = cust_name

    # Nested map: table_data[customer_name][food_item] = quantity
    # We use customer_name as the primary key to group orders by person
    table_data: dict[str, dict[str, str]] = {}
    # Set to keep track of all unique food items for the header
    unique_foods: set[str] = set()

    for _, cust_id, _, food_item, quantity in orders:
        cust_name = customer_map[cust_id]
        
        if cust_name not in table_data:
            table_data[cust_name] = {}
        
        # Store quantity as string to match expected output format
        table_data[cust_name][food_item] = quantity
        unique_foods.add(food_item)

    # Sort food items alphabetically for the header row
    sorted_foods = sorted(list(unique_foods))
    header = ["food"] + sorted_foods

    # Sort customers by their ID (numerically) to determine row order
    # Note: The problem implies sorting by customer ID, but the table 
    # rows are identified by name. We must sort the names based on the 
    # numeric value of the IDs associated with them.
    
    # First, create a list of (customer_id, customer_name) to sort correctly
    sorted_customer_info = sorted(customer_map.items(), key=lambda x: int(x[0]))
    
    result: list[list[str]] = [header]

    # Build each customer's row
    for cust_id, cust_name in sorted_customer_info:
        # Only include customers who actually placed an order
        if cust_name in table_data:
            row = [cust_name]
            customer_orders = table_data[cust_name]
            
            # For every food item in the header, check if the customer ordered it
            for food in sorted_foods:
                row.append(customer_orders.get(food, "0"))
            
            result.append(row)

    return result
