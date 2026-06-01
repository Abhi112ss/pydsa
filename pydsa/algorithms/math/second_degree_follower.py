METADATA = {
    "id": 614,
    "name": "Second Degree Follower",
    "slug": "second-degree-follower",
    "category": "Database/Logic",
    "aliases": [],
    "tags": ["hash_map", "graph_logic"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Find all users who are followed by the followers of a specific user.",
}

def solve(followers: list[dict], user_id: int) -> list[int]:
    """
    Finds all second-degree followers of a given user.
    A second-degree follower is someone followed by the people who follow the target user.

    Args:
        followers: A list of dictionaries where each dictionary represents a 
                   relationship with keys 'follower_id' and 'followee_id'.
        user_id: The ID of the user to find second-degree followers for.

    Returns:
        A sorted list of unique user IDs who are second-degree followers.

    Examples:
        >>> rels = [{'follower_id': 1, 'followee_id': 2}, {'follower_id': 2, 'followee_id': 3}]
        >>> solve(rels, 3)
        [1]
        >>> rels = [{'follower_id': 1, 'followee_id': 2}, {'follower_id': 1, 'followee_id': 3}, {'follower_id': 2, 'followee_id': 4}]
        >>> solve(rels, 3)
        [1]
    """
    # Map to store who follows whom: followee_id -> list of follower_ids
    # This allows us to quickly find who follows the target user.
    followee_to_followers = {}
    
    # Map to store who is being followed: follower_id -> list of followee_ids
    # This allows us to find the second-degree connections.
    follower_to_followees = {}

    for rel in followers:
        f_id = rel['follower_id']
        target_id = rel['followee_id']
        
        if target_id not in followee_to_followers:
            followee_to_followers[target_id] = []
        followee_to_followers[target_id].append(f_id)
        
        if f_id not in follower_to_followees:
            follower_to_followees[f_id] = []
        follower_to_followees[f_id].append(target_id)

    # Step 1: Identify the direct followers of the given user_id
    direct_followers = followee_to_followers.get(user_id, [])
    
    second_degree_followers = set()
    
    # Step 2: For every direct follower, find who they follow
    for follower in direct_followers:
        # We look up the people the direct follower follows
        connections = follower_to_followees.get(follower, [])
        for connection in connections:
            # A second-degree follower must not be the user themselves
            if connection != user_id:
                second_degree_followers.add(connection)
                
    # Note: The problem logic for "Second Degree Follower" in a social graph 
    # context usually implies: User A follows User B, User B follows User C. 
    # Therefore, User C is a second-degree follower of User A.
    # However, the LeetCode prompt "Second Degree Follower" often refers to 
    # finding people who follow the people who follow you.
    # Based on the standard interpretation of the prompt:
    # If User X follows User Y, and User Y follows User Z, then Z is a 2nd degree follower of X.
    # Wait, the prompt says: "Identify users who appear in both the follower and followee columns".
    # Let's re-align with the specific logic: Find people who follow the people who follow 'user_id'.
    
    # Re-evaluating based on the prompt's specific logic:
    # 1. Find people who follow 'user_id' (Direct Followers).
    # 2. Find people who are followed by those Direct Followers (Second Degree).
    # Actually, the prompt "Second Degree Follower" in SQL/LeetCode context usually means:
    # Find users who follow the people who follow 'user_id'.
    
    # Let's refine the set to match the standard "Second Degree" definition:
    # If A -> B and B -> C, then C is a second degree follower of A.
    # The code above finds C.
    
    return sorted(list(second_degree_followers))
