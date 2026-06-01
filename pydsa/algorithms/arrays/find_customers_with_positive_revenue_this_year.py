METADATA = {
    "id": 1821,
    "name": "Find Customers With Positive Revenue This Year",
    "slug": "find_customers_with_positive_revenue_this_year",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "filtering"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return customer IDs with positive total revenue for the current year.",
}


def solve() -> None:
    """Read customer records and output IDs with positive revenue this year.

    The input format is:
        n
        customer_id_1 revenue_1 year_1
        ...
        customer_id_n revenue_n year_n

    The function prints the distinct customer IDs (sorted ascending) whose total
    revenue for the current year (2023) is greater than zero.

    Returns:
        None. The result is printed to standard output.

    Example:
        Input:
            5
            1 100 2023
            2 -50 2023
            1 -30 2023
            3 200 2022
            2 70 2023
        Output:
            1 2
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    iterator = iter(data)
    record_count = int(next(iterator))
    revenue_by_customer: dict[int, int] = {}

    for _ in range(record_count):
        customer_id = int(next(iterator))
        revenue = int(next(iterator))
        year = int(next(iterator))

        # consider only records from the current year (2023)
        if year == 2023:
            # aggregate revenue per customer
            revenue_by_customer[customer_id] = revenue_by_customer.get(customer_id, 0) + revenue

    # filter customers with positive total revenue
    positive_customers = [cid for cid, total in revenue_by_customer.items() if total > 0]
    positive_customers.sort()

    # output result
    print(" ".join(map(str, positive_customers)))