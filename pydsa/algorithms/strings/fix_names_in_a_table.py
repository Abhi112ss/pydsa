METADATA = {
    "id": 1667,
    "name": "Fix Names in a Table",
    "slug": "fix-names-in-a-table",
    "category": "String Manipulation",
    "aliases": [],
    "tags": ["string", "sql-logic"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Format names such that the first character is uppercase and the rest are lowercase.",
}

def solve(names: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Fixes the formatting of names in a list of dictionaries.
    
    Each name is transformed so that the first character is capitalized 
    and all subsequent characters are lowercase.

    Args:
        names: A list of dictionaries where each dictionary contains 
               at least a 'name' key.

    Returns:
        A list of dictionaries with the 'name' values correctly formatted.

    Examples:
        >>> solve([{"user_id": 1, "name": "aLice"}, {"user_id": 2, "name": "Bob"}])
        [{'user_id': 1, 'name': 'Alice'}, {'user_id': 2, 'name': 'Bob'}]
        >>> solve([{"user_id": 3, "name": "mArY"}])
        [{'user_id': 3, 'name': 'Mary'}]
    """
    fixed_names = []
    
    for entry in names:
        # Create a shallow copy to avoid mutating the original input list
        new_entry = entry.copy()
        original_name = new_entry["name"]
        
        if not original_name:
            fixed_names.append(new_entry)
            continue
            
        # Capitalize the first letter and lowercase the rest
        # Python's .capitalize() does exactly this: 
        # "aLICE" -> "Alice", "BOB" -> "Bob"
        formatted_name = original_name.capitalize()
        
        new_entry["name"] = formatted_name
        fixed_names.append(new_entry)
        
    return fixed_names
