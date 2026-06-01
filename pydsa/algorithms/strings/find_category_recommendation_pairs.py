METADATA = {
    "id": 3554,
    "name": "Find Category Recommendation Pairs",
    "slug": "find-category-recommendation-pairs",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "two_pointer", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(N * K^2) where N is number of users and K is avg categories per user",
    "space_complexity": "O(C^2) where C is total unique categories",
    "description": "Find pairs of categories that frequently co-occur within the same user's history to provide recommendations.",
}

def solve(user_categories: list[list[int]], threshold: int) -> list[list[int]]:
    """
    Finds pairs of categories that appear together in at least 'threshold' users' histories.

    Args:
        user_categories: A list of lists, where each sublist contains the category IDs 
                         associated with a specific user.
        threshold: The minimum number of users required to recommend a pair.

    Returns:
        A list of pairs [cat_a, cat_b] where cat_a < cat_b and the pair occurs 
        at least 'threshold' times. The result is sorted lexicographically.

    Examples:
        >>> solve([[1, 2, 3], [1, 2], [1, 3]], 2)
        [[1, 2], [1, 3]]
        >>> solve([[1, 2], [2, 3], [3, 1]], 1)
        [[1, 2], [1, 3], [2, 3]]
    """
    # Dictionary to store the frequency of co-occurring category pairs
    # Key: tuple (min_cat, max_cat), Value: count
    co_occurrence_counts: dict[tuple[int, int], int] = {}

    for categories in user_categories:
        # Sort categories for each user to ensure we always process pairs in (small, large) order
        # This simplifies the key generation and avoids duplicate pairs like (1, 2) and (2, 1)
        sorted_cats = sorted(categories)
        num_categories = len(sorted_cats)
        
        # Use a set to ensure we only count a pair once per user, 
        # even if the input data has duplicate categories for a single user
        unique_user_cats = sorted(list(set(sorted_cats)))
        n = len(unique_user_cats)

        # Generate all unique combinations of 2 categories for the current user
        for i in range(n):
            for j in range(i + 1, n):
                pair = (unique_user_cats[i], unique_user_cats[j])
                co_occurrence_counts[pair] = co_occurrence_counts.get(pair, 0) + 1

    # Filter pairs that meet the minimum threshold requirement
    recommendations = []
    for (cat_a, cat_b), count in co_occurrence_counts.items():
        if count >= threshold:
            recommendations.append([cat_a, cat_b])

    # Sort the final list of pairs lexicographically: first by cat_a, then by cat_b
    recommendations.sort()
    
    return recommendations
