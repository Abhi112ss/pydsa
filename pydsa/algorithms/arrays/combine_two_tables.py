METADATA = {
    "id": 175,
    "name": "Combine Two Tables",
    "slug": "combine_two_tables",
    "category": "database",
    "aliases": ["Combine Two Tables SQL"],
    "tags": ["logic", "sql"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Perform a left outer join between Person and Address tables based on the personId.",
}


def solve(person_table: list[dict], address_table: list[dict]) -> list[dict]:
    """
    Combines Person and Address tables using a left outer join on personId.

    Args:
        person_table: A list of dictionaries containing 'personId', 'lastName', 'firstName'.
        address_table: A list of dictionaries containing 'addressId', 'personId', 'city', 'state'.

    Returns:
        A list of dictionaries containing 'firstName', 'lastName', 'city', 'state'.
        If the address of a personId is not present, city and state are None.

    Examples:
        >>> person = [{'personId': 1, 'lastName': 'Wang', 'firstName': 'Allen'}]
        >>> address = [{'addressId': 1, 'personId': 1, 'city': 'NYC', 'state': 'NY'}]
        >>> solve(person, address)
        [{'firstName': 'Allen', 'lastName': 'Wang', 'city': 'NYC', 'state': 'NY'}]
    """
    # Create a lookup dictionary for addresses keyed by personId for O(1) access
    address_lookup = {}
    for entry in address_table:
        # We assume personId is unique in the Address table per problem context
        address_lookup[entry["personId"]] = {
            "city": entry.get("city"),
            "state": entry.get("state"),
        }

    result = []
    # Iterate through each person to perform the left join
    for person in person_table:
        person_id = person["personId"]
        # Retrieve address info if it exists, otherwise default to None values
        address_info = address_lookup.get(person_id, {"city": None, "state": None})

        result.append(
            {
                "firstName": person["firstName"],
                "lastName": person["lastName"],
                "city": address_info["city"],
                "state": address_info["state"],
            }
        )

    return result
