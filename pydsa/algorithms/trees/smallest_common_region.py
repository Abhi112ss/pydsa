METADATA = {
    "id": 1257,
    "name": "Smallest Common Region",
    "slug": "smallest-common-region",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "hash_map", "lca"],
    "difficulty": "hard",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Find the smallest common region of two given regions in a tree structure.",
}

def solve(regions: list[list[int]], region_to_parent: list[int], region_to_name: list[str], region1: int, region2: int) -> str:
    """
    Finds the smallest common region of two given regions in a tree structure.
    
    The problem is equivalent to finding the Lowest Common Ancestor (LCA) in a tree
    where each region points to its parent.

    Args:
        regions: A list of lists, where each sublist contains the IDs of regions 
                 belonging to a specific area. (Not strictly needed for the LCA logic).
        region_to_parent: A list where region_to_parent[i] is the parent of region i.
        region_to_name: A list where region_to_name[i] is the name of region i.
        region1: The ID of the first region.
        region2: The ID of the second region.

    Returns:
        The name of the smallest common region.

    Examples:
        >>> regions = [[1, 2], [3, 4], [5, 6]]
        >>> region_to_parent = [-1, 0, 0, 1, 1, 2]
        >>> region_to_name = ["root", "a", "b", "c", "d", "e"]
        >>> solve(regions, region_to_parent, region_to_name, 3, 4)
        'a'
    """
    
    # Use a set to track the path from region1 to the root
    visited_regions = set()
    
    # Traverse up from region1 to the root, marking all ancestors
    current_region = region1
    while current_region != -1:
        visited_regions.add(current_region)
        current_region = region_to_parent[current_region]
        
    # Traverse up from region2; the first region encountered that is in 
    # the visited_regions set is the Lowest Common Ancestor (LCA)
    current_region = region2
    while current_region != -1:
        if current_region in visited_regions:
            return region_to_name[current_region]
        current_region = region_to_parent[current_region]
        
    # This part should theoretically not be reached given the problem constraints
    return ""
