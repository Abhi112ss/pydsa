METADATA = {
    "id": 1487,
    "name": "Making File Names Unique",
    "slug": "making-file-names-unique",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(N * L) where N is number of files and L is max length of a name",
    "space_complexity": "O(N * L) to store the names in the hash map",
    "description": "Given an array of file names, return an array where each file name is unique by appending a suffix if a collision occurs.",
}

def solve(files: list[str]) -> list[str]:
    """
    Processes a list of file names to ensure each name is unique.
    
    If a name already exists, a suffix in the format '(k)' is appended, 
    where k is the smallest positive integer that makes the name unique.
    
    Args:
        files: A list of strings representing the initial file names.
        
    Returns:
        A list of strings containing the unique file names.
        
    Examples:
        >>> solve(["pes", "fifa", "gta", "pes(1)"])
        ['pes', 'fifa', 'gta', 'pes(1)']
        >>> solve(["a", "b", "a", "a", "b"])
        ['a', 'b', 'a(1)', 'a(2)', 'b(1)']
        >>> solve(["x", "x", "x", "x(1)", "x(2)", "x(1)"])
        ['x', 'x(1)', 'x(2)', 'x(1)(1)', 'x(2)(1)', 'x(1)(1)(1)']
    """
    # name_counts maps a base name to the next integer suffix to try
    # This prevents O(N^2) behavior by not restarting the search from 1 every time
    name_counts: dict[str, int] = {}
    result: list[str] = []

    for name in files:
        if name not in name_counts:
            # Case 1: The name is brand new
            result.append(name)
            name_counts[name] = 1
        else:
            # Case 2: Collision detected. Find the next available (k)
            k = name_counts[name]
            new_name = f"{name}({k})"
            
            # Increment k until we find a name that hasn't been used yet
            while new_name in name_counts:
                k += 1
                new_name = f"{name}({k})"
            
            # Update the original name's counter to skip checked values next time
            name_counts[name] = k + 1
            
            # Add the new unique name to the map and result
            result.append(new_name)
            name_counts[new_name] = 1
            
    return result
