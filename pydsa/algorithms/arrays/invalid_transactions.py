METADATA = {
    "id": 1169,
    "name": "Invalid Transactions",
    "slug": "invalid-transactions",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sorting", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Identify transactions that occur at the same time but in different cities, or involve the same name but different cities at the same time.",
}

def solve(transactions: list[str]) -> list[str]:
    """
    Identifies invalid transactions based on name, amount, time, and city conflicts.
    
    A transaction is invalid if:
    1. It has the same name and time as another transaction but a different city.
    2. It has the same name and time as another transaction but a different amount (implied by city conflict logic).
    
    Actually, the rule is: A transaction is invalid if there is another transaction 
    with the same name, but a different city, at the same time.

    Args:
        transactions: A list of strings where each string is formatted as "name,amount,time,city".

    Returns:
        A list of strings containing all invalid transactions.

    Examples:
        >>> solve(["alice,20,10,new york", "bob,12,20,malibu", "alice,30,10,los angeles"])
        ['alice,20,10,new york', 'alice,30,10,los angeles']
    """
    # Parse the raw strings into structured data for easier comparison
    parsed_transactions = []
    for trans in transactions:
        name, amount, time, city = trans.split(',')
        parsed_transactions.append({
            "raw": trans,
            "name": name,
            "amount": int(amount),
            "time": int(time),
            "city": city
        })

    n = len(parsed_transactions)
    is_invalid = [False] * n

    # Compare every pair of transactions to find conflicts
    # A conflict exists if name and time match, but city does not.
    for i in range(n):
        for j in range(i + 1, n):
            t1 = parsed_transactions[i]
            t2 = parsed_transactions[j]

            if t1["name"] == t2["name"] and t1["time"] == t2["time"]:
                if t1["city"] != t2["city"]:
                    # Both transactions involved in the conflict are marked invalid
                    is_invalid[i] = True
                    is_invalid[j] = True

    # Collect all transactions marked as invalid
    result = []
    for idx in range(n):
        if is_invalid[idx]:
            result.append(parsed_transactions[idx]["raw"])

    return result
