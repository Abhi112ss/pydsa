METADATA = {
    "id": 339,
    "name": "Nested List Weight Sum",
    "slug": "nested_list_weight_sum",
    "category": "tree",
    "aliases": [],
    "tags": ["depth_first_search", "breadth_first_search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(d)",
    "description": "Compute the sum of integers in a nested list weighted by their depth.",
}

from typing import Union, List

NestedElement = Union[int, List["NestedElement"]]

def solve(nested_list: List[NestedElement]) -> int:
    """Calculate the weighted sum of a nested list of integers.

    Args:
        nested_list: A list where each element is either an integer or another
            nested list of the same structure.

    Returns:
        The sum of each integer multiplied by its depth (root depth = 1).

    Examples:
        >>> solve([1, [4, [6]]])
        27
        >>> solve([[1,1],2,[1,1]])
        10
    """
    def dfs(elements: List[NestedElement], depth: int) -> int:
        total = 0
        for element in elements:
            if isinstance(element, int):
                total += element * depth  # weight integer by current depth
            else:
                total += dfs(element, depth + 1)  # recurse into sublist
        return total

    return dfs(nested_list, 1)