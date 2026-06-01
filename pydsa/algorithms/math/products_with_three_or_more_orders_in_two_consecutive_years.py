METADATA = {
    "id": 2292,
    "name": "Products With Three or More Orders in Two Consecutive Years",
    "slug": "products-with-three-or-more-orders-in-two-consecutive-years",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sql"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find products that had at least three orders in two consecutive years.",
}

from collections import defaultdict

def solve(orders: list[dict[str, int]]) -> list[dict[str, int]]:
    """
    Identifies products that had three or more orders in two consecutive years.

    Args:
        orders: A list of dictionaries, where each dictionary represents an order
                containing 'product_id' and 'order_date' (represented as year).
                Example: [{'product_id': 1, 'year': 2019}, {'product_id': 1, 'year': 2019}, ...]

    Returns:
        A list of dictionaries containing the 'product_id' of qualifying products,
        sorted by product_id in ascending order.

    Examples:
        >>> orders = [
        ...     {'product_id': 1, 'year': 2019}, {'product_id': 1, 'year': 2019}, {'product_id': 1, 'year': 2019},
        ...     {'product_id': 1, 'year': 2020}, {'product_id': 1, 'year': 2020}, {'product_id': 1, 'year': 2020},
        ...     {'product_id': 2, 'year': 2019}, {'product_id': 2, 'year': 2019}, {'product_id': 2, 'year': 2019}
        ... ]
        >>> solve(orders)
        [{'product_id': 1}]
    """
    # Map product_id -> {year: count_of_orders}
    product_year_counts = defaultdict(lambda: defaultdict(int))

    # Step 1: Aggregate order counts per product per year
    for order in orders:
        product_id = order['product_id']
        year = order['year']
        product_year_counts[product_id][year] += 1

    result_product_ids = set()

    # Step 2: Check each product for consecutive years with >= 3 orders
    for product_id, years_dict in product_year_counts.items():
        # Get sorted list of years for this specific product
        sorted_years = sorted(years_dict.keys())
        
        for i in range(len(sorted_years) - 1):
            current_year = sorted_years[i]
            next_year = sorted_years[i + 1]
            
            # Check if years are consecutive and both meet the threshold
            if next_year == current_year + 1:
                if years_dict[current_year] >= 3 and years_dict[next_year] >= 3:
                    result_product_ids.add(product_id)
                    break  # Found a match for this product, move to next product

    # Step 3: Format output as list of dicts sorted by product_id
    sorted_results = sorted(list(result_product_ids))
    return [{"product_id": pid} for pid in sorted_results]
