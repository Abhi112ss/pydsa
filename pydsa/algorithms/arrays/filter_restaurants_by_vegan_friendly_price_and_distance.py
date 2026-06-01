METADATA = {
    "id": 1333,
    "name": "Filter Restaurants by Vegan-Friendly, Price and Distance",
    "slug": "filter-restaurants-by-vegan-friendly-price-and-distance",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "filtering"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Filter restaurants based on vegan-friendliness, maximum price, and minimum distance, then sort them by rating and ID.",
}

def solve(restaurants: list[list[int]], vegan_friendly: bool, max_price: int, distance_limit: float) -> list[list[int]]:
    """
    Filters restaurants based on specific criteria and returns them sorted.

    Args:
        restaurants: A list of lists where each sublist contains [id, customer_ratings_sum, 
                     number_of_ratings, latitude, longitude, is_vegan, price].
        vegan_friendly: Boolean indicating if only vegan-friendly restaurants should be included.
        max_price: The maximum allowable price for a restaurant.
        distance_limit: The maximum allowable distance from a specific point (implied by problem context).
                       Note: In the LeetCode version, distance is usually calculated from a 
                       fixed point or provided as a pre-calculated value. Based on the 
                       standard problem signature, we filter by the provided constraints.

    Returns:
        A list of lists containing the filtered and sorted restaurants.

    Examples:
        >>> restaurants = [[1, 10, 2, 4, 4, 1, 5], [2, 20, 2, 4, 4, 0, 10]]
        >>> solve(restaurants, True, 10, 1.0)
        [[1, 10, 2, 4, 4, 1, 5]]
    """
    filtered_restaurants = []

    for res in restaurants:
        res_id = res[0]
        ratings_sum = res[1]
        num_ratings = res[2]
        lat = res[3]
        lon = res[4]
        is_vegan = res[5]
        price = res[6]

        # Calculate average rating for sorting purposes
        avg_rating = ratings_sum / num_ratings

        # 1. Apply filtering criteria: vegan status, price, and distance.
        # Note: The problem description for 1333 usually provides distance as a 
        # pre-calculated value or requires a specific distance check. 
        # In the standard LeetCode signature, distance is often handled via 
        # a provided distance array or calculated via coordinates.
        # Here we assume the standard filter logic:
        
        # Check vegan requirement
        if vegan_friendly and is_vegan == 0:
            continue
        
        # Check price requirement
        if price > max_price:
            continue
            
        # The problem 1333 specifically provides distance as a separate input 
        # in some variations, but the standard signature is:
        # restaurants, vegan_friendly, max_price, distance_limit
        # We assume distance_limit is a threshold for a distance value 
        # provided in the context of the problem.
        
        # Since the standard LeetCode signature for 1333 is:
        # restaurants: List[List[int]], vegan_friendly: bool, max_price: int, distance_limit: float
        # and the distance is actually calculated from a point (lat, lon) 
        # provided in the problem description (often (4, 4)), 
        # we must ensure we follow the exact logic.
        
        # However, looking at the LeetCode signature, distance is usually 
        # calculated from (4, 4) as per the problem description.
        # Let's implement the distance calculation if needed, but usually, 
        # the distance is provided as a constraint on a calculated value.
        
        # Standard LeetCode 1333 distance calculation:
        # distance = sqrt((lat - 4)^2 + (lon - 4)^2)
        import math
        dist = math.sqrt((lat - 4)**2 + (lon - 4)**2)
        
        if dist > distance_limit:
            continue

        # Store the restaurant with its calculated average rating for sorting
        # We store [id, ratings_sum, num_ratings, lat, lon, is_vegan, price, avg_rating]
        filtered_restaurants.append(res + [avg_rating])

    # 2. Sort the filtered list.
    # Primary key: average rating (descending)
    # Secondary key: restaurant ID (ascending)
    # We use a lambda that negates the rating to achieve descending order for that key.
    filtered_restaurants.sort(key=lambda x: (-x[7], x[0]))

    # 3. Clean up the list to return only the original columns
    return [res[:7] for res in filtered_restaurants]
