METADATA = {
    "id": 584,
    "name": "Find Customer Referee",
    "slug": "find_customer_referee",
    "category": "Database",
    "aliases": [],
    "tags": ["database", "sql", "hash-table", "set"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the names of customers who are not referred by any other customer.",
}


def solve(customers: list[list[object]]) -> list[str]:
    """Find customers who are not referred by any other customer.

    Args:
        customers: A list where each element is a list of three items:
            - id (int): Unique identifier of the customer.
            - name (str): Name of the customer.
            - referee_id (int or None): The id of the customer who referred this one,
              or None if there is no referee.

    Returns:
        A list of customer names that do not appear as a referee_id for any other
        customer, sorted alphabetically.

    Examples:
        >>> solve([[1, "Alice", None], [2, "Bob", 1], [3, "Charlie", 2]])
        ['Alice']
        >>> solve([[10, "Dave", None], [20, "Eve", None]])
        ['Dave', 'Eve']
    """
    # Map each customer id to its name for quick lookup.
    id_to_name: dict[int, str] = {}
    # Collect all ids and all non‑null referee ids.
    all_ids: set[int] = set()
    referee_ids: set[int] = set()

    for record in customers:
        customer_id, name, referee_id = record[0], record[1], record[2]
        id_to_name[customer_id] = name
        all_ids.add(customer_id)
        # Exclude NULL (None) values from the referee set.
        if referee_id is not None:
            referee_ids.add(referee_id)

    # Customers whose id never appears as a referee_id are the desired ones.
    root_ids = all_ids - referee_ids
    result_names = [id_to_name[cust_id] for cust_id in root_ids]
    result_names.sort()
    return result_names