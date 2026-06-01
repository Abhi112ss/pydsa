METADATA = {
    "id": 1744,
    "name": "Can You Eat Your Favorite Candy on Your Favorite Day?",
    "slug": "can-you-eat-your-favorite-candy-on-your-favorite-day",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "modulo"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if it is possible to eat a specific favorite candy on a specific favorite day given a sequence of candy amounts.",
}

def solve(candy: list[int], favorite_candy: int, favorite_day: int) -> bool:
    """
    Determines if the favorite candy can be eaten on the favorite day.

    The candies are eaten in cycles. If the total number of candies is N, 
    the candy eaten on day 'd' is determined by the cumulative sum of 
    candies modulo N.

    Args:
        candy: A list of integers representing the number of candies of each type.
        favorite_candy: The ID of the favorite candy.
        favorite_day: The zero-indexed day the user wants to eat the favorite candy.

    Returns:
        True if the favorite candy can be eaten on the favorite day, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2, 2)
        True
        >>> solve([1, 2, 3, 4, 5], 2, 3)
        False
    """
    total_candies = sum(candy)
    
    # The favorite day is zero-indexed. If the favorite day is greater than 
    # or equal to the total number of candies, it's impossible.
    if favorite_day >= total_candies:
        return False

    # We need to find the range of candy IDs that are eaten on 'favorite_day'.
    # Since candies are eaten in cycles, the candy eaten on 'favorite_day' 
    # is the candy at index (favorite_day % total_candies) in the 
    # flattened sequence of all candies.
    
    # However, the problem asks if the 'favorite_candy' ID is eaten on that day.
    # The candy ID eaten on 'favorite_day' is actually determined by the 
    # cumulative sum of candies.
    
    # Let's find the range of candy IDs that are eaten on the 'favorite_day'.
    # Because we are looking for a specific candy ID, we can check if the 
    # favorite_candy falls within the range of IDs covered by the 
    # cumulative sum at the specific day.
    
    # A more direct way: The candy eaten on 'favorite_day' is the candy 
    # whose cumulative count covers the index 'favorite_day'.
    # But the problem defines candy IDs by their position in the list.
    # Wait, the candy IDs are 1-indexed based on the list position.
    
    # Let's re-evaluate: The total number of candies is 'total_candies'.
    # The candy eaten on 'favorite_day' is the candy at index (favorite_day % total_candies)
    # in the sequence of all candies.
    # But the candy IDs are 1, 2, ..., len(candy).
    # The problem states: "the i-th candy is candy[i]". 
    # Actually, the candy IDs are 1, 2, ..., len(candy).
    # The candy eaten on day 'd' is the candy at index (d % total_candies) 
    # in the sequence of all candies.
    
    # Let's find the cumulative sum to see which candy ID corresponds to 'favorite_day'.
    # Since we need to check if 'favorite_candy' is eaten on 'favorite_day',
    # we check if the 'favorite_day' falls within the range of indices 
    # occupied by 'favorite_candy'.
    
    # The range of indices for 'favorite_candy' (1-indexed) is:
    # start_index = sum(candy[0 : favorite_candy-1])
    # end_index = sum(candy[0 : favorite_candy]) - 1
    
    # Because of the cycle, the candy eaten on 'favorite_day' is the one 
    # where (favorite_day % total_candies) falls into the range 
    # [start_index, end_index] (relative to the total sequence).
    
    # However, the cycle repeats the entire sequence.
    # The candy eaten on 'favorite_day' is the candy at index (favorite_day % total_candies)
    # in the sequence of all candies.
    # We need to find which candy ID is at that position.
    
    # Let's find the cumulative sum of all candies.
    # The candy ID at index 'i' (0 <= i < total_candies) is the smallest 'k' 
    # such that prefix_sum[k] > i.
    
    # Instead of iterating, we can find the range of indices for 'favorite_candy'.
    # Let's calculate the prefix sums.
    current_sum = 0
    start_idx = 0
    end_idx = 0
    
    # Find the range of indices [start_idx, end_idx] that 'favorite_candy' covers.
    # favorite_candy is 1-indexed.
    for i in range(len(candy)):
        if i == favorite_candy - 1:
            start_idx = current_sum
            current_sum += candy[i]
            end_idx = current_sum - 1
            break
        current_sum += candy[i]
    
    # The candy eaten on 'favorite_day' is the one at index (favorite_day % total_candies).
    # We need to check if (favorite_day % total_candies) is within [start_idx, end_idx].
    # But wait, the favorite_day might be larger than total_candies, 
    # but the problem says we eat candies in cycles.
    # The sequence of candies is: candy[0] (repeated candy[0] times), candy[1]...
    # The total length of one cycle is total_candies.
    # The index in the cycle is favorite_day % total_candies.
    
    # We need to check if the candy at (favorite_day % total_candies) is favorite_candy.
    # This is true if start_idx <= (favorite_day % total_candies) <= end_idx.
    
    # Wait, the favorite_day is the day we want to eat the candy.
    # The candy eaten on day 'd' is the candy at index 'd % total_candies' 
    # in the sequence of all candies.
    # We need to find if the candy at index 'favorite_day % total_candies' is 'favorite_candy'.
    
    # Let's re-calculate start_idx and end_idx correctly.
    prefix_sum = 0
    start_idx = -1
    end_idx = -1
    
    for i, count in enumerate(candy):
        if i == favorite_candy - 1:
            start_idx = prefix_sum
            prefix_sum += count
            end_idx = prefix_sum - 1
            break
        prefix_sum += count
        
    # The index in the cycle is:
    target_idx = favorite_day % total_candies
    
    # Check if target_idx falls within the range of the favorite candy.
    return start_idx <= target_idx <= end_idx
