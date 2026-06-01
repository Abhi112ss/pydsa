METADATA = {
    "id": 726,
    "name": "Number of Atoms",
    "slug": "number-of-atoms",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "hash_map", "parsing"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Given a chemical formula string, return the count of each atom in the formula in a specific format.",
}

def solve(formula: str) -> str:
    """
    Parses a chemical formula string and returns the count of each atom.

    Args:
        formula: A string representing the chemical formula.

    Returns:
        A string representing the counts of atoms in alphabetical order.

    Examples:
        >>> solve("H2O")
        'H2O'
        >>> solve("Mg(OH)2")
        'H2MgO2'
        >>> solve("K4(ON(SO3)2)2")
        'K4N2O14S4'
    """
    stack: list[dict[str, int]] = [{}]
    n = len(formula)
    i = 0

    while i < n:
        if formula[i] == '(':
            # Start a new nesting level
            stack.append({})
            i += 1
        elif formula[i] == ')':
            # End nesting level and find the multiplier
            i += 1
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            
            multiplier = int(formula[start:i] or 1)
            top_map = stack.pop()
            current_map = stack[-1]
            
            # Multiply all atoms in the closed group and merge into the parent level
            for atom, count in top_map.items():
                current_map[atom] = current_map.get(atom, 0) + count * multiplier
        else:
            # Parse Atom Name (Uppercase followed by lowercase letters)
            start = i
            i += 1
            while i < n and formula[i].islower():
                i += 1
            atom = formula[start:i]
            
            # Parse Atom Count
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            count = int(formula[start:i] or 1)
            
            # Add atom to the current nesting level
            current_map = stack[-1]
            current_map[atom] = current_map.get(atom, 0) + count

    # The final result is in the first dictionary of the stack
    final_counts = stack[0]
    sorted_atoms = sorted(final_counts.keys())
    
    result_parts = []
    for atom in sorted_atoms:
        count = final_counts[atom]
        result_parts.append(atom)
        if count > 1:
            result_parts.append(str(count))
            
    return "".join(result_parts)
