METADATA = {
    "id": 2051,
    "name": "The Category of Each Member in the Store",
    "slug": "the_category_of_each_member_in_the_store",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return each member's most frequently purchased product category.",
}


def solve(
    members: list[list[int | str]],
    orders: list[list[int]],
    products: list[list[int | str]],
) -> list[list[int, str]]:
    """Determine the most frequently purchased product category for each member.

    Args:
        members: A list where each element is [member_id, member_name].
        orders: A list where each element is [order_id, member_id, product_id].
        products: A list where each element is [product_id, category].

    Returns:
        A list of [member_id, category] pairs sorted by member_id. The category
        is the one the member bought most often; if there is a tie, the
        lexicographically smallest category is chosen.

    Examples:
        >>> members = [[1, "Alice"], [2, "Bob"]]
        >>> orders = [[101, 1, 1001], [102, 1, 1002], [103, 2, 1001]]
        >>> products = [[1001, "Electronics"], [1002, "Books"]]
        >>> solve(members, orders, products)
        [[1, "Books"], [2, "Electronics"]]
    """
    # Map product_id to its category for O(1) look‑ups.
    product_to_category: dict[int, str] = {}
    for product_id, category in products:
        product_to_category[int(product_id)] = str(category)

    # Count categories per member.
    member_category_counts: dict[int, dict[str, int]] = {}
    for _, member_id, product_id in orders:
        member_key = int(member_id)
        category = product_to_category[int(product_id)]
        if member_key not in member_category_counts:
            member_category_counts[member_key] = {}
        category_counter = member_category_counts[member_key]
        category_counter[category] = category_counter.get(category, 0) + 1

    # Determine the most frequent category for each member.
    result: list[list[int, str]] = []
    for member_id, _ in members:
        member_key = int(member_id)
        category_counter = member_category_counts.get(member_key, {})
        if not category_counter:
            # If the member has no orders, we can skip or assign an empty string.
            continue
        # Find max count; on ties choose smallest category lexicographically.
        max_count = max(category_counter.values())
        candidate_categories = [
            cat for cat, cnt in category_counter.items() if cnt == max_count
        ]
        chosen_category = min(candidate_categories)
        result.append([member_key, chosen_category])

    # Return results ordered by member_id.
    result.sort(key=lambda pair: pair[0])
    return result