METADATA = {
    "id": 1251,
    "name": "Average Selling Price",
    "slug": "average_selling_price",
    "category": "Database",
    "aliases": [],
    "tags": ["math", "aggregation"],
    "difficulty": "medium",
    "time_complexity": "O((s+q) log s)",
    "space_complexity": "O(s)",
    "description": "Compute the average selling price for each query based on sales records.",
}


def solve(sales: list[list[int]], queries: list[list[int]]) -> list[float]:
    """Calculate average selling price for each query.

    Args:
        sales: A list where each element is [product_id, units_sold, price_per_unit,
            timestamp]. All values are integers.
        queries: A list where each element is [product_id, start_timestamp,
            end_timestamp]. The timestamps are inclusive.

    Returns:
        A list of floats where each float is the average selling price for the
        corresponding query. If no units were sold in the given date range,
        the result for that query is -1.0.

    Examples:
        >>> sales = [
        ...     [1, 10, 5, 100],
        ...     [1, 5, 7, 200],
        ...     [2, 3, 20, 150]
        ... ]
        >>> queries = [
        ...     [1, 50, 150],
        ...     [2, 100, 200],
        ...     [1, 300, 400]
        ... ]
        >>> solve(sales, queries)
        [5.666666666666667, 20.0, -1.0]
    """
    from bisect import bisect_left, bisect_right

    # Map each product to its sorted sales records and prefix sums.
    product_to_data: dict[int, dict[str, list[int]]] = {}

    # Organize raw records per product.
    for product_id, units, price, timestamp in sales:
        if product_id not in product_to_data:
            product_to_data[product_id] = {"timestamps": [], "cum_units": [0], "cum_revenue": [0]}
        product_to_data[product_id]["timestamps"].append(timestamp)
        product_to_data[product_id]["cum_units"].append(units)          # temporary storage
        product_to_data[product_id]["cum_revenue"].append(units * price)  # temporary storage

    # Sort records and build true prefix sums.
    for product_id, data in product_to_data.items():
        # Zip together to sort by timestamp while keeping units and revenue aligned.
        combined = list(zip(data["timestamps"], data["cum_units"][1:], data["cum_revenue"][1:]))
        combined.sort(key=lambda x: x[0])

        # Reset lists with a leading zero for easier diff calculations.
        timestamps_sorted: list[int] = [0]
        cum_units: list[int] = [0]
        cum_revenue: list[int] = [0]

        for ts, units, revenue in combined:
            timestamps_sorted.append(ts)
            cum_units.append(cum_units[-1] + units)
            cum_revenue.append(cum_revenue[-1] + revenue)

        data["timestamps"] = timestamps_sorted
        data["cum_units"] = cum_units
        data["cum_revenue"] = cum_revenue

    results: list[float] = []

    for product_id, start_ts, end_ts in queries:
        if product_id not in product_to_data:
            results.append(-1.0)
            continue

        data = product_to_data[product_id]
        timestamps = data["timestamps"]
        cum_units = data["cum_units"]
        cum_revenue = data["cum_revenue"]

        # Find rightmost index where timestamp <= end_ts (inclusive).
        right_index = bisect_right(timestamps, end_ts) - 1
        # Find leftmost index where timestamp < start_ts.
        left_index = bisect_left(timestamps, start_ts) - 1

        if right_index <= left_index:
            results.append(-1.0)
            continue

        total_units = cum_units[right_index] - cum_units[left_index]
        total_revenue = cum_revenue[right_index] - cum_revenue[left_index]

        if total_units == 0:
            results.append(-1.0)
        else:
            results.append(total_revenue / total_units)

    return results