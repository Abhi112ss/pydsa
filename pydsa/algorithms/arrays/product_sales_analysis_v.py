METADATA = {
    "id": 2329,
    "name": "Product Sales Analysis V",
    "slug": "product_sales_analysis_v",
    "category": "SQL Logic Simulation",
    "aliases": [],
    "tags": ["sql_logic", "date_filtering"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Filter sales records to find products sold within a specific 30-day window relative to a given date.",
}

from datetime import datetime, timedelta

def solve(sales_data: list[dict], current_date_str: str) -> list[dict]:
    """
    Filters the sales dataset for records where the sale date is within 
    the 30-day window relative to the provided current date.

    Args:
        sales_data: A list of dictionaries, where each dictionary represents 
            a sale with keys 'product_id', 'sale_date' (YYYY-MM-DD), and 'amount'.
        current_date_str: A string representing the reference date in 'YYYY-MM-DD' format.

    Returns:
        A list of dictionaries containing only the sales that occurred 
        within the 30-day window (inclusive of the current date and 30 days prior).

    Examples:
        >>> sales = [
        ...     {"product_id": 1, "sale_date": "2023-01-01", "amount": 100},
        ...     {"product_id": 2, "sale_date": "2023-01-15", "amount": 200},
        ...     {"product_id": 3, "sale_date": "2023-02-15", "amount": 300}
        ... ]
        >>> solve(sales, "2023-01-20")
        [{'product_id': 1, 'sale_date': '2023-01-01', 'amount': 100}, 
         {'product_id': 2, 'sale_date': '2023-01-15', 'amount': 200}]
    """
    # Parse the reference date
    reference_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    
    # Define the window: [reference_date - 30 days, reference_date]
    # Note: In SQL logic, "within 30 days" usually implies the range 
    # [current_date - 30, current_date]
    start_window = reference_date - timedelta(days=30)
    
    filtered_sales = []
    
    for sale in sales_data:
        # Convert sale date string to datetime object for comparison
        sale_date = datetime.strptime(sale["sale_date"], "%Y-%m-%d")
        
        # Check if the sale date falls within the inclusive 30-day window
        if start_window <= sale_date <= reference_date:
            filtered_sales.append(sale)
            
    return filtered_sales
