METADATA = {
    "id": 2353,
    "name": "Design a Food Rating System",
    "slug": "design-a-food-rating-system",
    "category": "Design",
    "aliases": [],
    "tags": ["heap", "hash_map", "priority_queue", "design"],
    "difficulty": "medium",
    "time_complexity": "O(log N) for all operations",
    "space_complexity": "O(N)",
    "description": "Design a system to store food items with their cuisine and rating, allowing updates and retrieval of the highest-rated food per cuisine.",
}

import heapq

class FoodRatingSystem:
    """
    A system to manage food ratings categorized by cuisine.
    
    Uses a combination of hash maps for O(1) access and max-heaps for 
    O(log N) retrieval of the highest-rated food per cuisine.
    """

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        """
        Initializes the FoodRatingSystem.

        Args:
            foods: A list of food names.
            cuisines: A list of cuisines corresponding to each food.
            ratings: A list of ratings corresponding to each food.
        """
        # food_to_data maps food_name -> (rating, cuisine)
        self.food_to_data: dict[str, tuple[int, str]] = {}
        
        # cuisine_to_heap maps cuisine -> max-heap of (-rating, food_name)
        # We use negative rating to simulate a max-heap using Python's min-heap
        self.cuisine_to_heap: dict[str, list[tuple[int, str]]] = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_data[food] = (rating, cuisine)
            if cuisine not in self.cuisine_to_heap:
                self.cuisine_to_heap[cuisine] = []
            # Push (-rating, food_name) to handle max rating and lexicographical order
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        """
        Updates the rating of an existing food item.

        Args:
            food: The name of the food to update.
            newRating: The new rating to assign.
        """
        rating, cuisine = self.food_to_data[food]
        # Update the primary source of truth
        self.food_to_data[food] = (newRating, cuisine)
        # Lazy removal: push the new rating into the heap. 
        # The old rating remains in the heap but will be ignored by highestRated()
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        """
        Retrieves the name of the highest rated food in the given cuisine.
        If there is a tie, returns the lexicographically smaller name.

        Args:
            cuisine: The cuisine to query.

        Returns:
            The name of the highest rated food.
        """
        heap = self.cuisine_to_heap[cuisine]
        
        # Lazy removal: check if the top of the heap matches the current 
        # actual rating stored in food_to_data.
        while heap:
            neg_rating, food = heap[0]
            actual_rating, actual_cuisine = self.food_to_data[food]
            
            # If the rating in the heap is outdated, discard it
            if -neg_rating != actual_rating:
                heapq.heappop(heap)
            else:
                return food
        
        return ""

def solve():
    """
    Example usage of the FoodRatingSystem.
    """
    foods = ["sushi", "curry", "miso", "ramen", "miso"]
    cuisines = ["japanese", "indian", "japanese", "japanese", "japanese"]
    ratings = [13, 15, 11, 14, 12]
    
    frs = FoodRatingSystem(foods, cuisines, ratings)
    print(frs.highestRated("japanese"))  # Expected: "ramen"
    frs.changeRating("miso", 15)
    print(frs.highestRated("japanese"))  # Expected: "miso"
    print(frs.highestRated("indian"))    # Expected: "curry"
