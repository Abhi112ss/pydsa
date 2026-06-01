METADATA = {
    "id": 2861,
    "name": "Maximum Number of Alloys",
    "slug": "maximum-number-of-alloys",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine the maximum number of target alloy units that can be produced given initial amounts and recipe requirements.",
}

def solve(initial_amounts: list[int], recipes: list[list[int]]) -> int:
    """
    Calculates the maximum number of target alloy units that can be produced.

    The problem asks for the maximum number of units of a specific target alloy.
    Since the recipes are structured such that each recipe produces exactly one 
    unit of a new alloy using a combination of existing ones, and we want to 
    maximize the target, we can use a greedy approach. However, the problem 
    constraints and structure imply that we are looking for the maximum 
    possible production. Given the nature of the problem (often seen in 
    resource conversion), the maximum amount is limited by the bottleneck 
    resource in the recipe that produces the target.

    Args:
        initial_amounts: A list of integers representing the initial quantity 
            of each alloy.
        recipes: A list of lists, where each sub-list represents a recipe. 
            A recipe is defined as [target_alloy_index, ingredient_1_index, 
            quantity_1, ingredient_2_index, quantity_2, ...].

    Returns:
        The maximum number of units of the target alloy that can be produced.

    Examples:
        >>> solve([10, 10], [[0, 1, 2]])
        5
        >>> solve([1, 1, 1], [[0, 1, 1, 2, 1]])
        1
    """
    # The problem description for 2861 in standard LeetCode contexts 
    # usually involves finding the maximum production of a specific target.
    # Based on the prompt's hint: "Use a greedy approach to always mix 
    # the alloy that provides the highest yield".
    
    # Note: In a real competitive programming environment, the target alloy 
    # index is usually specified. Assuming the target is the first alloy 
    # mentioned in the recipes or a specific index provided.
    # For the sake of this implementation, we assume the target is index 0.
    
    target_alloy = 0
    
    # To find the maximum possible production, we look at the recipes 
    # that produce the target alloy.
    # For each recipe: target = recipe[0], ingredients = (recipe[2], recipe[3]), etc.
    
    max_production = 0
    
    # We iterate through recipes to find those that produce our target.
    # Since we want the maximum number of alloys, we check which recipe 
    # allows for the most production based on current resources.
    for recipe in recipes:
        if recipe[0] == target_alloy:
            # Calculate how many times this specific recipe can be applied
            # based on the available initial amounts of its ingredients.
            current_recipe_yield = float('inf')
            
            # Ingredients are stored in pairs: [index, quantity, index, quantity...]
            # starting from index 1 of the recipe list.
            for i in range(1, len(recipe), 2):
                ingredient_idx = recipe[i]
                required_qty = recipe[i + 1]
                
                # The number of times we can use this ingredient is 
                # floor(available / required)
                possible_uses = initial_amounts[ingredient_idx] // required_qty
                current_recipe_yield = min(current_recipe_yield, possible_uses)
            
            # We take the maximum yield among all recipes that produce the target
            max_production = max(max_production, int(current_recipe_yield))
            
    return max_production
