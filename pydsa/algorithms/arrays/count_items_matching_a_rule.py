METADATA = {
    "id": 1773,
    "name": "Count Items Matching a Rule",
    "slug": "count_items_matching_a_rule",
    "category": "array",
    "aliases": [],
    "tags": ["array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Counts how many items satisfy a given rule based on type, color, or name.",
}

def solve() -> None:
    """Read input, count items matching the rule, and print the result.

    Input format:
        n
        type1 color1 name1
        type2 color2 name2
        ...
        ruleKey ruleValue

    Args:
        None (reads from standard input).

    Returns:
        None (prints the count to standard output).

    Example:
        Input:
            3
            phone blue pixel
            computer silver lenovo
            phone gold iphone
            type phone
        Output:
            2
    """
    import sys

    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    # Number of items
    n = int(data[0].strip())
    items: list[list[str]] = []
    for i in range(1, n + 1):
        # Each item consists of three strings: type, color, name
        items.append(data[i].strip().split())

    # Rule key and value
    rule_parts = data[n + 1].strip().split()
    rule_key = rule_parts[0]
    rule_value = rule_parts[1]

    # Map rule key to its position in each item list
    key_to_index = {"type": 0, "color": 1, "name": 2}
    target_index = key_to_index[rule_key]

    match_count = 0
    for item in items:
        # Increment count when the item's attribute matches the rule value
        if item[target_index] == rule_value:
            match_count += 1

    print(match_count)