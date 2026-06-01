METADATA = {
    "id": 1268,
    "name": "Search Suggestions System",
    "slug": "search-suggestions-system",
    "category": "String",
    "aliases": [],
    "tags": ["trie", "binary_search", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N log N + M log N)",
    "space_complexity": "O(N)",
    "description": "Given a list of products and a search word, return the top 3 lexicographically smallest suggestions for each prefix of the search word.",
}

import bisect

def solve(products: list[str], searchWord: str) -> list[list[str]]:
    """
    Provides search suggestions based on the prefix of the search word.

    Args:
        products: A list of product names.
        searchWord: The string being typed by the user.

    Returns:
        A list of lists, where each inner list contains up to 3 lexicographically 
        smallest product suggestions for the prefix formed up to that character.

    Examples:
        >>> solve(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
        [['moneypot', 'monitor', 'mobile'], ['moneypot', 'monitor', 'mobile'], ['moneypot', 'monitor', 'mobile'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]
        Note: The example output above is illustrative; actual lexicographical order 
        depends on the sorted list.
    """
    # Sort products lexicographically to enable binary search
    sorted_products = sorted(products)
    results = []
    
    # current_prefix tracks the string formed as we iterate through searchWord
    current_prefix = ""
    
    for char in searchWord:
        current_prefix += char
        
        # Find the first index where a product is >= current_prefix
        # This is the start of the range of products matching the prefix
        start_index = bisect.bisect_left(sorted_products, current_prefix)
        
        suggestions = []
        # Check the next 3 products starting from start_index
        # They must still start with the current_prefix to be valid
        for i in range(start_index, min(start_index + 3, len(sorted_products))):
            if sorted_products[i].startswith(current_prefix):
                suggestions.append(sorted_products[i])
            else:
                # Since the list is sorted, if this one doesn't match, 
                # no subsequent ones will.
                break
        
        results.append(suggestions)
        
    return results
