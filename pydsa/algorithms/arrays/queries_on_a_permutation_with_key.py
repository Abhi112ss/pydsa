METADATA = {
    "id": 1409,
    "name": "Queries on a Permutation With Key",
    "slug": "queries-on-a-permutation-with-key",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "hash table"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(n)",
    "description": "Given a permutation and a key, answer queries to find the index of a value in the modified permutation.",
}

def solve(key: list[int], queries: list[list[int]]) -> list[int]:
    """
    Processes queries on a permutation modified by a key.

    The permutation is constructed by taking the key and appending the 
    remaining numbers from 1 to n that are not present in the key.

    Args:
        key: A list of unique integers representing the initial part of the permutation.
        queries: A list of queries where each query is [query_value, query_index].

    Returns:
        A list of integers representing the index of query_value in the modified 
        permutation for each query.

    Examples:
        >>> solve([3, 1, 2, 4], [[3, 0], [1, 1]])
        [0, 1]
        >>> solve([1, 2, 3, 4], [[4, 3], [1, 0]])
        [3, 0]
    """
    n = len(key)
    # Use a set for O(1) lookup to find missing numbers
    present_in_key = set(key)
    
    # The modified permutation starts with the key
    # We then append all numbers from 1 to n that are not in the key
    # To optimize, we build the full permutation first
    full_permutation = list(key)
    for i in range(1, n + 1):
        if i not in present_in_key:
            full_permutation.append(i)
            
    # Precompute the mapping of value -> index for O(1) query time
    # This is the core optimization to avoid O(n) search per query
    value_to_index = {val: idx for idx, val in enumerate(full_permutation)}
    
    results = []
    for val, _ in queries:
        # The problem asks for the index of 'val' in the permutation
        # The second element of the query (query_index) is unused in the logic
        # but provided in the input format.
        results.append(value_to_index[val])
        
    return results
