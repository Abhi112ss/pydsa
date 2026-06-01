METADATA = {
    "id": 1902,
    "name": "Depth of BST Given Insertion Order",
    "slug": "depth_of_bst_given_insertion_order",
    "category": "Trees",
    "aliases": [],
    "tags": ["binary_search_tree", "simulation", "monotonic_stack", "segment_tree"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum depth of a Binary Search Tree given the sequence of elements inserted.",
}

import bisect

def solve(insertion_order: list[int]) -> int:
    """
    Calculates the maximum depth of a BST formed by inserting elements in a given order.
    
    The algorithm uses the property that when an element is inserted into a BST, 
    its parent is either its predecessor or its successor in the sorted set of 
    already inserted elements, specifically the one that was inserted most recently.
    
    Args:
        insertion_order: A list of integers representing the order of insertion.
        
    Returns:
        The maximum depth of the resulting BST.
        
    Examples:
        >>> solve([1, 2, 3, 4, 5])
        5
        >>> solve([5, 1, 2, 3, 4])
        2
        >>> solve([3, 1, 4, 2, 5])
        3
    """
    if not insertion_order:
        return 0

    n = len(insertion_order)
    # depths[i] will store the depth of the element at insertion_order[i]
    depths = [0] * n
    # sorted_elements maintains the elements currently in the BST to find neighbors
    sorted_elements = []
    # element_to_index maps the value to its original index in insertion_order
    # to retrieve the depth of the parent easily.
    element_to_index = {}
    
    # We use a sorted list to simulate the BST structure. 
    # For each new element, its parent is either its predecessor or successor 
    # in the current sorted set, whichever was inserted later (has a higher index).
    for i, val in enumerate(insertion_order):
        # Find the position where 'val' would be inserted to maintain order
        idx = bisect.bisect_left(sorted_elements, val)
        
        predecessor_idx = -1
        successor_idx = -1
        
        # Check predecessor (element just smaller than val)
        if idx > 0:
            pred_val = sorted_elements[idx - 1]
            predecessor_idx = element_to_index[pred_val]
            
        # Check successor (element just larger than val)
        if idx < len(sorted_elements):
            succ_val = sorted_elements[idx]
            successor_idx = element_to_index[succ_val]
            
        # The parent is the one among predecessor and successor that was inserted last
        # because that element is the one that would be the immediate ancestor in a BST.
        parent_idx = -1
        if predecessor_idx != -1 and successor_idx != -1:
            parent_idx = predecessor_idx if predecessor_idx > successor_idx else successor_idx
        elif predecessor_idx != -1:
            parent_idx = predecessor_idx
        elif successor_idx != -1:
            parent_idx = successor_idx
            
        # If no parent exists, this is the root (depth 1)
        if parent_idx == -1:
            depths[i] = 1
        else:
            depths[i] = depths[parent_idx] + 1
            
        # Update tracking structures
        bisect.insort(sorted_elements, val)
        element_to_index[val] = i
        
    return max(depths)
