METADATA = {
    "id": 1241,
    "name": "Number of Comments per Post",
    "slug": "number_of_comments_per_post",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "group_by"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Counts distinct comments per post from a list of comment records.",
}


def solve(comments: list[tuple[int, int, int | None]]) -> list[tuple[int, int]]:
    """Counts distinct comments for each post.

    Args:
        comments: A list of tuples where each tuple represents a comment record
            in the form (post_id, comment_id, parent_comment_id). The
            parent_comment_id can be None for top‑level comments.

    Returns:
        A list of (post_id, comment_count) tuples sorted by post_id in ascending
        order. Each comment is counted at most once per post, even if duplicate
        rows appear in the input.

    Examples:
        >>> data = [
        ...     (1, 101, None),
        ...     (1, 102, 101),
        ...     (2, 201, None),
        ...     (1, 101, None),  # duplicate row
        ... ]
        >>> solve(data)
        [(1, 2), (2, 1)]
    """
    # Set to keep track of unique (parent_comment_id, comment_id) pairs
    seen_pairs: set[tuple[int | None, int]] = set()
    # Mapping from post_id to its distinct comment count
    post_comment_counts: dict[int, int] = {}

    for post_id, comment_id, parent_comment_id in comments:
        pair = (parent_comment_id, comment_id)
        if pair in seen_pairs:
            continue  # duplicate comment, skip counting
        seen_pairs.add(pair)

        # Increment the comment count for the associated post
        if post_id in post_comment_counts:
            post_comment_counts[post_id] += 1
        else:
            post_comment_counts[post_id] = 1

    # Produce sorted result list
    result = sorted(post_comment_counts.items(), key=lambda item: item[0])
    return result