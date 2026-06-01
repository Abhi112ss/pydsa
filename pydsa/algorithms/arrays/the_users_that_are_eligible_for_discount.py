METADATA = {
    "id": 2230,
    "name": "The Users That Are Eligible for Discount",
    "slug": "the-users-that-are-eligible-for-discount",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "filtering"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify users within a specific age range who have made a purchase of a specific amount.",
}

def solve(users: list[list[int]], age_limit: int, purchase_amount: int) -> list[int]:
    """
    Finds the IDs of users who are within the age limit and have made a purchase 
    of at least the specified purchase amount.

    Args:
        users: A list of lists where each sublist contains [user_id, age, purchase_amount].
        age_limit: The maximum age (inclusive) for a user to be eligible.
        purchase_amount: The minimum purchase amount (inclusive) required for eligibility.

    Returns:
        A list of user IDs that meet both the age and purchase amount criteria, 
        sorted in ascending order.

    Examples:
        >>> solve([[1, 20, 100], [2, 25, 50], [3, 15, 150]], 20, 100)
        [1]
        >>> solve([[1, 20, 100], [2, 25, 50], [3, 15, 150]], 30, 50)
        [1, 2, 3]
    """
    eligible_user_ids = []

    for user_data in users:
        user_id, age, amount = user_data
        
        # Check if the user meets both the age and the purchase amount criteria
        if age <= age_limit and amount >= purchase_amount:
            eligible_user_ids.append(user_id)

    # The problem typically expects the IDs to be returned in ascending order
    eligible_user_ids.sort()
    
    return eligible_user_ids
