METADATA = {
    "id": 3528,
    "name": "Unit Conversion I",
    "slug": "unit_conversion_i",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a value from one unit to another using a set of provided conversion ratios.",
}

def solve(conversions: list[list[str]], queries: list[list[str]]) -> list[float]:
    """
    Performs unit conversions based on a list of provided conversion ratios.

    Args:
        conversions: A list of lists where each sublist contains [unit_a, unit_b, ratio].
                     The ratio represents how many unit_b are in one unit_a.
        queries: A list of lists where each sublist contains [value, from_unit, to_unit].

    Returns:
        A list of floats representing the converted values. Returns -1.0 if conversion is impossible.

    Examples:
        >>> solve([["m", "cm", "100"], ["cm", "mm", "10"]], [[1, "m", "mm"]])
        [1000.0]
        >>> solve([["m", "cm", "100"]], [[1, "m", "mm"]])
        [-1.0]
    """
    # adjacency_map stores the multiplier to go from unit_a to unit_b
    # and the reciprocal multiplier to go from unit_b to unit_a.
    # Since the problem implies a tree/path structure for valid conversions,
    # we can use a simple BFS or DFS to find the path.
    # However, for "Unit Conversion I", we assume a single connected component 
    # or a simple chain for each unit type.
    
    adj: dict[str, list[tuple[str, float]]] = {}

    for u1, u2, ratio_str in conversions:
        ratio = float(ratio_str)
        if u1 not in adj:
            adj[u1] = []
        if u2 not in adj:
            adj[u2] = []
        
        # If 1 unit_a = ratio * unit_b
        adj[u1].append((u2, ratio))
        # Then 1 unit_b = (1/ratio) * unit_a
        adj[u2].append((u1, 1.0 / ratio))

    results: list[float] = []

    for val_str, start_unit, end_unit in queries:
        value = float(val_str)
        
        if start_unit == end_unit:
            results.append(value)
            continue

        # BFS to find the conversion factor from start_unit to end_unit
        found_factor = -1.0
        visited = {start_unit}
        queue: list[tuple[str, float]] = [(start_unit, 1.0)]
        
        idx = 0
        while idx < len(queue):
            curr_unit, curr_factor = queue[idx]
            idx += 1
            
            if curr_unit == end_unit:
                found_factor = curr_factor
                break
            
            if curr_unit in adj:
                for neighbor, multiplier in adj[curr_unit]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        # Cumulative multiplier: factor to reach curr * multiplier to reach neighbor
                        queue.append((neighbor, curr_factor * multiplier))
            
            if found_factor != -1.0:
                break
        
        if found_factor != -1.0:
            results.append(value * found_factor)
        else:
            results.append(-1.0)

    return results
