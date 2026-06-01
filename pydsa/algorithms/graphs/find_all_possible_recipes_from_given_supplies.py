METADATA = {
    "id": 2115,
    "name": "Find All Possible Recipes from Given Supplies",
    "slug": "find-all-possible-recipes-from-given-supplies",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "topological_sort", "hash_map", "breadth_first_search"],
    "difficulty": "medium",
    "time_complexity": "O(N + E)",
    "space_complexity": "O(N + E)",
    "description": "Determine all recipes that can be made given a set of initial supplies and a list of recipes with ingredient dependencies using topological sort.",
}

def solve(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    """
    Finds all recipes that can be prepared given the initial supplies.

    Args:
        recipes: A list of recipe names.
        ingredients: A list of lists, where ingredients[i] contains the ingredients for recipes[i].
        supplies: A list of available initial supplies.

    Returns:
        A list of recipe names that can be successfully prepared.

    Examples:
        >>> solve(["bread", "sandwich"], [["flour", "water", "yeast"], ["bread", "ham"]], ["flour", "water", "yeast", "ham"])
        ['bread', 'sandwich']
        >>> solve(["bread", "sandwich"], [["flour", "water", "yeast"], ["bread", "ham"]], ["flour", "water", "yeast"])
        ['bread']
    """
    from collections import deque, defaultdict

    # adjacency_list maps an ingredient to the recipes that depend on it
    adjacency_list = defaultdict(list)
    # in_degree tracks how many ingredients are still needed for a specific recipe
    in_degree = {}
    
    # All unique items (recipes and supplies) to build the graph
    # We only care about dependencies where an ingredient is a recipe
    all_recipes = set(recipes)
    
    for i, recipe in enumerate(recipes):
        recipe_ingredients = ingredients[i]
        # Count how many ingredients in this recipe are NOT in the initial supplies
        # and are not yet "available" via other recipes.
        # However, for Kahn's, we only care about dependencies that are recipes.
        needed_count = 0
        for ing in recipe_ingredients:
            if ing in all_recipes:
                adjacency_list[ing].append(recipe)
                needed_count += 1
            elif ing not in supplies:
                # If an ingredient is neither a recipe nor a supply, 
                # this recipe can never be made. We represent this by a high in_degree.
                needed_count = float('inf')
                break
        
        in_degree[recipe] = needed_count

    # Initialize queue with recipes that have 0 dependencies (all ingredients are in supplies)
    # Note: If a recipe's ingredients are all in 'supplies', its in_degree will be 0.
    queue = deque()
    for recipe in recipes:
        if in_degree.get(recipe) == 0:
            queue.append(recipe)

    possible_recipes = []

    while queue:
        current_ingredient = queue.popleft()
        possible_recipes.append(current_ingredient)

        # For every recipe that depends on the ingredient we just "produced"
        for dependent_recipe in adjacency_list[current_ingredient]:
            in_degree[dependent_recipe] -= 1
            # If all dependencies for the dependent recipe are met, add to queue
            if in_degree[dependent_recipe] == 0:
                queue.append(dependent_recipe)

    return possible_recipes
