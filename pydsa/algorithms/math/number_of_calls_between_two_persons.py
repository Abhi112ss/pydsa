METADATA = {
    "id": 1699,
    "name": "Number of Calls Between Two Persons",
    "slug": "number-of-calls-between-two-persons",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the number of calls between two specific users, considering the order of callers and receivers as interchangeable.",
}

def solve(caller_id: int, receiver_id: int, calls: list[dict[str, int]]) -> int:
    """
    Calculates the total number of calls between two specific users.
    
    The relationship is undirected, meaning a call from user A to user B 
    is the same as a call from user B to user A for the purpose of this count.

    Args:
        caller_id: The ID of the first user.
        receiver_id: The ID of the second user.
        calls: A list of dictionaries where each dictionary represents a call 
               with keys 'caller' and 'receiver'.

    Returns:
        The total count of calls between the two users.

    Examples:
        >>> calls = [{'caller': 1, 'receiver': 2}, {'caller': 2, 'receiver': 1}, {'caller': 1, 'receiver': 3}]
        >>> solve(1, 2, calls)
        2
        >>> solve(1, 3, calls)
        1
    """
    call_count = 0
    
    for call in calls:
        current_caller = call['caller']
        current_receiver = call['receiver']
        
        # Check if the current call matches (user1, user2) OR (user2, user1)
        # This simulates the SQL logic: WHERE (caller = u1 AND receiver = u2) OR (caller = u2 AND receiver = u1)
        is_match = (
            (current_caller == caller_id and current_receiver == receiver_id) or
            (current_caller == receiver_id and current_receiver == caller_id)
        )
        
        if is_match:
            call_count += 1
            
    return call_count
