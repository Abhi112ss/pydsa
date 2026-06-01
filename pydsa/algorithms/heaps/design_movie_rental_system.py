METADATA = {
    "id": 1912,
    "name": "Design Movie Rental System",
    "slug": "design-movie-rental-system",
    "category": "Design",
    "aliases": [],
    "tags": ["heap", "hash_map", "sorted_set", "design"],
    "difficulty": "hard",
    "time_complexity": "O(log N) per operation",
    "space_complexity": "O(N)",
    "description": "Design a system to rent and return movies with efficient searching for the cheapest available movies.",
}

import heapq
from collections import defaultdict

class SortedList:
    """
    A simplified SortedList implementation using a min-heap and a lazy-removal 
    mechanism to simulate a balanced BST/SortedSet behavior.
    """
    def __init__(self):
        self.heap = []
        self.deleted = defaultdict(int)

    def add(self, val: tuple[int, int]):
        heapq.heappush(self.heap, val)

    def remove(self, val: tuple[int, int]):
        self.deleted[val] += 1

    def pop_min(self) -> tuple[int, int]:
        # Clean up the top of the heap if the element was marked as deleted
        while self.heap and self.deleted[self.heap[0]] > 0:
            val = heapq.heappop(self.heap)
            self.deleted[val] -= 1
        return heapq.heappop(self.heap)

    def peek_min(self) -> tuple[int, int]:
        while self.heap and self.deleted[self.heap[0]] > 0:
            val = heapq.heappop(self.heap)
            self.deleted[val] -= 1
        return self.heap[0]

    def is_empty(self) -> bool:
        while self.heap and self.deleted[self.heap[0]] > 0:
            val = heapq.heappop(self.heap)
            self.deleted[val] -= 1
        return len(self.heap) == 0

class MovieRentalSystem:
    def __init__(self, movies: list[list[int]], shops: list[list[int]]):
        """
        Initializes the rental system.
        
        Args:
            movies: List of [shop, movie]
            shops: List of [shop, movie, price]
        """
        # movie_to_shops[movie][shop] = price
        self.movie_to_shops = defaultdict(dict)
        # available_movies stores (price, shop, movie) for all unrented movies
        self.available_movies = SortedList()
        # rented_movies stores (price, shop, movie) for all currently rented movies
        self.rented_movies = SortedList()
        # movie_shop_price[shop][movie] = price
        self.movie_shop_price = defaultdict(dict)
        # rented_set tracks which (shop, movie) pairs are currently rented
        self.rented_set = set()

        # Process shops input: shops[i] = [shop, movie, price]
        for shop, movie, price in shops:
            self.movie_to_shops[movie][shop] = price
            self.movie_shop_price[shop][movie] = price
            self.available_movies.add((price, shop, movie))

    def search(self, movie: int) -> list[int]:
        """
        Finds the cheapest 5 unrented copies of a movie.

        Args:
            movie: The movie ID.

        Returns:
            A list of up to 5 [shop, movie] pairs, sorted by price, then shop.
        """
        # Note: Since we can't easily iterate a heap for specific movie IDs, 
        # we must maintain a separate SortedList per movie for O(log N) search.
        # However, to keep the complexity optimal within the constraints, 
        # we'll use a dictionary of SortedLists for each movie.
        # Let's refine the implementation below.
        pass

class MovieRentalSystemOptimized:
    """
    Refined implementation using per-movie SortedLists to ensure O(log N) search.
    """
    def __init__(self, movies: list[list[int]], shops: list[list[int]]):
        # movie_to_shops[movie][shop] = price
        self.movie_to_shops = defaultdict(dict)
        # available_per_movie[movie] = SortedList of (price, shop)
        self.available_per_movie = defaultdict(SortedList)
        # rented_movies = SortedList of (price, shop, movie)
        self.rented_movies = SortedList()
        # shop_movie_price[shop][movie] = price
        self.shop_movie_price = defaultdict(dict)
        # rented_set tracks (shop, movie)
        self.rented_set = set()

        for shop, movie, price in shops:
            self.movie_to_shops[movie][shop] = price
            self.shop_movie_price[shop][movie] = price
            self.available_per_movie[movie].add((price, shop))

    def search(self, movie: int) -> list[list[int]]:
        """
        Finds the cheapest 5 unrented copies of a movie.
        """
        res = []
        sl = self.available_per_movie[movie]
        
        # We need to peek at the top 5 elements. 
        # Since SortedList is a heap, we must temporarily pop and re-add 
        # or use a more complex structure. For LeetCode, we can use a 
        # temporary list to collect and then restore.
        temp_storage = []
        while len(res) < 5 and not sl.is_empty():
            val = sl.pop_min()
            temp_storage.append(val)
            res.append([val[1], movie])
        
        # Restore the elements back to the SortedList
        for item in temp_storage:
            sl.add(item)
            
        return res

    def rent(self, shop: int, movie: int) -> None:
        """
        Rents a movie from a shop.
        """
        price = self.shop_movie_price[shop][movie]
        # Remove from available
        self.available_per_movie[movie].remove((price, shop))
        # Add to rented
        self.rented_movies.add((price, shop, movie))
        self.rented_set.add((shop, movie))

    def derent(self, shop: int, movie: int) -> None:
        """
        Returns a rented movie to a shop.
        """
        price = self.shop_movie_price[shop][movie]
        # Remove from rented
        self.rented_movies.remove((price, shop, movie))
        self.rented_set.remove((shop, movie))
        # Add back to available
        self.available_per_movie[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        """
        Returns the cheapest 5 rented movies.
        """
        res = []
        temp_storage = []
        # Collect top 5 from the global rented heap
        while len(res) < 5 and not self.rented_movies.is_empty():
            val = self.rented_movies.pop_min()
            temp_storage.append(val)
            res.append([val[1], val[2]])
        
        # Restore the elements
        for item in temp_storage:
            self.rented_movies.add(item)
            
        return res

# The actual class required by LeetCode structure
class MovieRentalSystemFinal(MovieRentalSystemOptimized):
    pass

# Re-mapping for the final solution to match the expected interface
def solve():
    """
    This is a placeholder to satisfy the requirement of a single file.
    The actual logic is contained in MovieRentalSystemOptimized.
    """
    pass

# Since the prompt asks for the solver file, I will provide the 
# implementation of MovieRentalSystem as the primary class.

class MovieRentalSystem:
    def __init__(self, movies: list[list[int]], shops: list[list[int]]):
        # movie_to_shops[movie][shop] = price
        self.movie_to_shops = defaultdict(dict)
        # available_per_movie[movie] = SortedList of (price, shop)
        self.available_per_movie = defaultdict(SortedList)
        # rented_movies = SortedList of (price, shop, movie)
        self.rented_movies = SortedList()
        # shop_movie_price[shop][movie] = price
        self.shop_movie_price = defaultdict(dict)
        # rented_set tracks (shop, movie)
        self.rented_set = set()

        for shop, movie, price in shops:
            self.movie_to_shops[movie][shop] = price
            self.shop_movie_price[shop][movie] = price
            self.available_per_movie[movie].add((price, shop))

    def search(self, movie: int) -> list[list[int]]:
        res = []
        sl = self.available_per_movie[movie]
        temp_storage = []
        # Extract up to 5 cheapest available copies
        while len(res) < 5 and not sl.is_empty():
            val = sl.pop_min()
            temp_storage.append(val)
            res.append([val[1], movie])
        # Restore extracted elements to the heap
        for item in temp_storage:
            sl.add(item)
        return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_price[shop][movie]
        # Move from available per movie to global rented list
        self.available_per_movie[movie].remove((price, shop))
        self.rented_movies.add((price, shop, movie))
        self.rented_set.add((shop, movie))

    def derent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_price[shop][movie]
        # Move from global rented list back to available per movie
        self.rented_movies.remove((price, shop, movie))
        self.rented_set.remove((shop, movie))
        self.available_per_movie[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        res = []
        temp_storage = []
        # Extract up to 5 cheapest rented movies
        while len(res) < 5 and not self.rented_movies.is_empty():
            val = self.rented_movies.pop_min()
            temp_storage.append(val)
            res.append([val[1], val[2]])
        # Restore extracted elements to the heap
        for item in temp_storage:
            self.rented_movies.add(item)
        return res