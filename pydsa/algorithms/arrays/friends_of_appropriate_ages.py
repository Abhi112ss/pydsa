METADATA = {
    "id": 825,
    "name": "Friends Of Appropriate Ages",
    "slug": "friends_of_appropriate_ages",
    "category": "Array",
    "aliases": [],
    "tags": ["counting", "two_pointer", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n + max_age)",
    "space_complexity": "O(max_age)",
    "description": "Count the number of pairs of people who can be friends based on specific age constraints.",
}

def solve(friends: list[list[int]]) -> int:
    """
    Calculates the number of pairs of people who can be friends.
    
    A pair (x, y) is appropriate if:
    1. x + 7 <= y
    2. x + 1 <= y - 7
    3. x < y
    
    These simplify to: y >= x + 8.

    Args:
        friends: A list of lists where each sub-list contains [age, count] 
                 representing the age of a person and how many people have that age.

    Returns:
        The total number of appropriate friend pairs.

    Examples:
        >>> solve([[1, 1], [7, 1], [10, 1]])
        1
        >>> solve([[1, 1], [7, 1], [10, 1], [11, 1]])
        3
    """
    # The maximum age is 100 according to problem constraints
    MAX_AGE = 100
    age_counts = [0] * (MAX_AGE + 1)
    
    # Populate the frequency array
    for age, count in friends:
        age_counts[age] = count
        
    # Create a prefix sum array to allow O(1) range sum queries
    # prefix_sums[i] stores the total number of people with age <= i
    prefix_sums = [0] * (MAX_AGE + 1)
    current_sum = 0
    for i in range(MAX_AGE + 1):
        current_sum += age_counts[i]
        prefix_sums[i] = current_sum
        
    total_pairs = 0
    
    # Iterate through each age group to find valid friends
    for age in range(MAX_AGE + 1):
        if age_counts[age] == 0:
            continue
            
        # The condition y >= x + 8 means for a person of age 'age',
        # any person with age >= age + 8 is a valid friend.
        min_friend_age = age + 8
        
        if min_friend_age <= MAX_AGE:
            # Calculate number of people in the range [min_friend_age, MAX_AGE]
            # using the prefix sum: total_people_up_to_max - total_people_up_to_min_friend_age - 1
            # Actually, it's prefix_sums[MAX_AGE] - prefix_sums[min_friend_age - 1]
            count_of_valid_friends = prefix_sums[MAX_AGE] - prefix_sums[min_friend_age - 1]
            
            # Multiply the number of people at current age by the number of valid friends
            total_pairs += age_counts[age] * count_of_valid_friends
            
    return total_pairs
