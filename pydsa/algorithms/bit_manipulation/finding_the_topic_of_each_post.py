METADATA = {
    "id": 2199,
    "name": "Finding the Topic of Each Post",
    "slug": "finding-the-topic-of-each-post",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["bit_manipulation", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n * num_topics)",
    "space_complexity": "O(n)",
    "description": "Find the most frequent topic for each post by identifying common topics shared with other posts using bitmasks.",
}

def solve(topics: list[list[int]], posts: list[list[int]]) -> list[int]:
    """
    Finds the most frequent topic for each post.

    A topic is considered 'frequent' for a post if it appears in the most 
    number of other posts that share at least one topic with the current post.

    Args:
        topics: A list of lists where topics[i] contains the topic IDs for post i.
        posts: A list of lists where posts[j] contains the post IDs that cover topic j.

    Returns:
        A list of integers where the i-th element is the most frequent topic for post i.
        If there is a tie, the smallest topic ID is returned.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 4]], [[0, 1], [0, 2], [1, 2]])
        [1, 2, 3]
    """
    num_posts = len(topics)
    num_topics = len(posts)
    
    # Step 1: Convert each post's topics into a bitmask for efficient comparison.
    # Since num_topics can be up to 100, we use Python's arbitrary-precision integers.
    post_masks = [0] * num_posts
    for post_idx in range(num_posts):
        mask = 0
        for topic_id in topics[post_idx]:
            mask |= (1 << topic_id)
        post_masks[post_idx] = mask

    # Step 2: Pre-calculate which posts share at least one topic.
    # We can optimize this by iterating through each topic and seeing which posts it belongs to.
    # topic_to_posts[t] = list of post indices that contain topic t.
    topic_to_posts = [[] for _ in range(num_topics)]
    for topic_id in range(num_topics):
        for post_id in posts[topic_id]:
            topic_to_posts[topic_id].append(post_id)

    results = []
    for i in range(num_posts):
        current_post_mask = post_masks[i]
        topic_counts = {}
        
        # Step 3: Find all posts that share at least one topic with post i.
        # We iterate through all topics of post i, then all posts containing those topics.
        # We use a set to ensure we don't count the same 'other' post multiple times.
        shared_posts = set()
        for topic_id in topics[i]:
            for other_post_id in topic_to_posts[topic_id]:
                if other_post_id != i:
                    shared_posts.add(other_post_id)
        
        # Step 4: For each shared post, count how many topics they have in common with post i.
        # However, the problem asks for the most frequent topic *among the shared posts*.
        # Re-reading: "the topic that appears in the most number of posts that share at least one topic with post i".
        # This means we count how many 'shared_posts' contain each topic of post i.
        for topic_id in topics[i]:
            count = 0
            for other_post_id in shared_posts:
                # Check if the shared post contains this specific topic
                if (post_masks[other_post_id] >> topic_id) & 1:
                    count += 1
            topic_counts[topic_id] = count

        # Step 5: Determine the best topic based on frequency and then ID.
        best_topic = -1
        max_freq = -1
        
        # Sort topics to handle the "smallest topic ID" tie-break rule naturally
        # or just iterate and compare.
        for topic_id in sorted(topics[i]):
            freq = topic_counts.get(topic_id, 0)
            if freq > max_freq:
                max_freq = freq
                best_topic = topic_id
        
        results.append(best_topic)

    return results

# Note: The logic above is slightly inefficient for large constraints. 
# Let's refine the counting logic to meet O(N * num_topics) or similar.

def solve(topics: list[list[int]], posts: list[list[int]]) -> list[int]:
    """
    Optimized version of the topic finder.
    """
    num_posts = len(topics)
    num_topics = len(posts)
    
    # post_masks[i] is the bitmask of topics in post i
    post_masks = [0] * num_posts
    for i in range(num_posts):
        for t in topics[i]:
            post_masks[i] |= (1 << t)
            
    # topic_to_posts[t] is the list of posts containing topic t
    topic_to_posts = [[] for _ in range(num_topics)]
    for t in range(num_topics):
        for p in posts[t]:
            topic_to_posts[t].append(p)
            
    ans = []
    for i in range(num_posts):
        # Find all posts that share at least one topic with post i
        shared_posts_mask = 0
        for t in topics[i]:
            for p_idx in topic_to_posts[t]:
                shared_posts_mask |= (1 << p_idx)
        
        # Remove the current post from the shared set
        shared_posts_mask &= ~(1 << i)
        
        best_topic = -1
        max_count = -1
        
        # For each topic in the current post, count how many shared posts contain it
        # We sort topics[i] to handle tie-breaking (smallest ID)
        for t in sorted(topics[i]):
            count = 0
            # Instead of iterating all shared posts, we check how many posts in 
            # topic_to_posts[t] are also in the shared_posts_mask.
            for p_idx in topic_to_posts[t]:
                if (shared_posts_mask >> p_idx) & 1:
                    count += 1
            
            if count > max_count:
                max_count = count
                best_topic = t
        
        ans.append(best_topic)
        
    return ans