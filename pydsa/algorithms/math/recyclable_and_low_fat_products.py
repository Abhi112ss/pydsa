METADATA = {
    "id": 1757,
    "name": "Recyclable and Low Fat Products",
    "slug": "recyclable-and-low-fat-products",
    "category": "Database",
    "aliases": [],
    "tags": ["sql"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the IDs of products that are both low fat and recyclable.",
}

from typing import List, Dict, Any


def solve(products: List[Dict[str, Any]]) -> List[int]:
    """
    Filters a list of product dictionaries to find IDs of products that are 
    both low fat and recyclable.

    Args:
        products: A list of dictionaries where each dictionary represents a product.
            Each dictionary contains 'product_id' (int), 'low_fats' (str 'Y'/'N'),
            and 'recyclable' (str 'Y'/'N').

    Returns:
        A list of integers representing the product_ids that satisfy the criteria.

    Examples:
        >>> products = [
        ...     {"product_id": 0, "low_fats": "Y", "recyclable": "N"},
        ...     {"product_id": 1, "low_fats": "Y", "recyclable": "Y"},
        ...     {"product_id": 2, "low_fats": "N", "recyclable": "Y"},
        ...     {"product_id": 3, "low_fats": "Y", "recyclable": "Y"},
        ...     {"product_id": 4, "low_fats": "N", "recyclable": "N"}
        ... ]
        >>> solve(products)
        [1, 3]
    """
    result_ids: List[int] = []

    for product in products:
        # Check if both 'low_fats' and 'recyclable' attributes are 'Y'
        # This mimics the SQL WHERE low_fats = 'Y' AND recyclable = 'Y' clause
        is_low_fat = product.get("low_fats") == "Y"
        is_recyclable = product.get("recyclable") == "Y"

        if is_low_fat and is_recyclable:
            result_ids.append(product["product_id"])

    return result_ids
