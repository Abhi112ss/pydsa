METADATA = {
    "id": 1795,
    "name": "Rearrange Products Table",
    "slug": "rearrange-products-table",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "pivot", "transformation"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Transform a table from a long format to a wide format by pivoting product names into columns.",
}

def solve(products: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Transforms the products table from long format to wide format.
    
    The input is a list of dictionaries where each dictionary represents a row 
    in the original table with keys 'product_id', 'store_id', and 'product'.
    The output is a list of dictionaries where each dictionary represents a row 
    grouped by 'store_id', containing 'store_id' and the product names as keys.

    Args:
        products: A list of dictionaries representing the input table.
            Example: [{"product_id": "0", "store_id": "1", "product": "headphone"}, ...]

    Returns:
        A list of dictionaries representing the pivoted table.
        Example: [{"store_id": "1", "headphone": "0", "laptop": "1"}, ...]

    Examples:
        >>> products = [
        ...     {"product_id": "0", "store_id": "1", "product": "headphone"},
        ...     {"product_id": "1", "store_id": "1", "product": "laptop"},
        ...     {"product_id": "2", "store_id": "2", "product": "headphone"}
        ... ]
        >>> solve(products)
        [{'store_id': '1', 'headphone': '0', 'laptop': '1'}, {'store_id': '2', 'headphone': '2'}]
    """
    # Dictionary to group product information by store_id
    # Key: store_id, Value: dict of {product_name: product_id}
    pivoted_data: dict[str, dict[str, str]] = {}

    for row in products:
        store_id = row["store_id"]
        product_name = row["product"]
        product_id = row["product_id"]

        # Initialize the store entry if it doesn't exist
        if store_id not in pivoted_data:
            pivoted_data[store_id] = {"store_id": store_id}
        
        # Map the product name to its corresponding product_id for this store
        pivoted_data[store_id][product_name] = product_id

    # Convert the dictionary of stores into a list of dictionaries
    # We sort by store_id to ensure deterministic output, though not strictly required by logic
    result = []
    sorted_store_ids = sorted(pivoted_data.keys())
    
    for store_id in sorted_store_ids:
        result.append(pivoted_data[store_id])

    return result
