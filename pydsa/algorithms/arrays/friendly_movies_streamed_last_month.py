METADATA = {
    "id": 1495,
    "name": "Friendly Movies Streamed Last Month",
    "slug": "friendly-movies-streamed-last-month",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of movies that can be watched such that no two movies are consecutive in the original list.",
}

def solve(movies: list[int], friends: list[list[int]]) -> int:
    """
    Calculates the maximum number of movies that can be watched such that 
    no two movies are consecutive in the original list and each movie 
    is watched by at least one friend.

    Args:
        movies: A list of movie IDs.
        friends: A list of lists, where each sublist contains movie IDs 
                 that a specific friend likes.

    Returns:
        The maximum number of movies that can be watched.

    Examples:
        >>> solve([1, 2, 3], [[1, 2], [2, 3]])
        2
        >>> solve([1, 2, 3, 4], [[1, 2], [3, 4]])
        2
    """
    n = len(movies)
    if n == 0:
        return 0

    # Map movie ID to its index in the original list for O(1) lookup
    movie_to_idx = {movie_id: i for i, movie_id in enumerate(movies)}
    
    # Track which movies are "covered" (liked by at least one friend)
    # and which movies are "available" (can be picked without violating adjacency)
    is_covered = [False] * n
    for friend_movies in friends:
        for m_id in friend_movies:
            if m_id in movie_to_idx:
                is_covered[movie_to_idx[m_id]] = True

    # We want to pick as many movies as possible.
    # A movie can be picked if:
    # 1. It is covered by a friend.
    # 2. It is not adjacent to a movie already picked.
    
    # To maximize the count, we use a greedy approach.
    # However, the constraint is "no two movies are consecutive".
    # This is equivalent to finding the maximum independent set on a path graph
    # restricted to the subset of 'covered' nodes.
    
    # Since the graph is a simple path (1-2-3-4...), we can use dynamic programming
    # or a greedy approach. For a path graph, greedy works: 
    # iterate through and pick a node if it's covered and its neighbors aren't picked.
    
    # But wait, the problem asks for the maximum number of movies such that 
    # NO TWO movies are consecutive. This is exactly the Maximum Independent Set 
    # on the subgraph induced by the 'covered' nodes.
    
    # Let's refine: We can only pick movies that are in the 'is_covered' set.
    # If we have a contiguous block of covered movies of length K, 
    # the maximum number of non-adjacent movies we can pick from that block is ceil(K/2).
    
    total_max_movies = 0
    current_block_length = 0
    
    for i in range(n):
        if is_covered[i]:
            current_block_length += 1
        else:
            # End of a contiguous block of covered movies
            if current_block_length > 0:
                # For a block of length K, we can pick (K + 1) // 2 movies
                total_max_movies += (current_block_length + 1) // 2
                current_block_length = 0
                
    # Handle the last block if the loop ends while in a block
    if current_block_length > 0:
        total_max_movies += (current_block_length + 1) // 2
        
    return total_max_movies
