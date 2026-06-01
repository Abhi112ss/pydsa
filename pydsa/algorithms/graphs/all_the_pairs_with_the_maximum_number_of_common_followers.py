METADATA = {
    "id": 1951,
    "name": "All the Pairs With the Maximum Number of Common Followers",
    "slug": "all_the_pairs_with_the_maximum_number_of_common_followers",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "bit_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(n^2 / 64)",
    "space_complexity": "O(n)",
    "description": "Find all pairs of users that share the maximum number of common followers using bitsets for efficient intersection.",
}

def solve(n: int, connections: list[list[int]]) -> list[list[int]]:
    """
    Finds all pairs of users that share the maximum number of common followers.

    Args:
        n: The number of users (labeled 1 to n).
        connections: A list of pairs [a, b] where a is a follower of b.

    Returns:
        A list of pairs [u, v] (where u < v) that have the maximum number of common followers,
        sorted in ascending order.

    Examples:
        >>> solve(4, [[1, 2], [2, 3], [1, 3], [1, 4]])
        [[1, 3]]
        >>> solve(3, [[1, 2], [2, 3], [1, 3]])
        [[1, 2], [1, 3], [2, 3]]
    """
    # Represent followers of each user as a bitset (Python's large integers act as bitsets)
    # followers[i] will have the j-th bit set if user j follows user i.
    followers = [0] * (n + 1)
    for follower, followed in connections:
        followers[followed] |= (1 << follower)

    max_common = 0
    result = []

    # Iterate through all unique pairs (i, j)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # The intersection of two bitsets gives the common followers.
            # bit_count() is highly optimized in Python 3.10+
            common_count = (followers[i] & followers[j]).bit_count()

            if common_count > 0:
                if common_count > max_common:
                    # Found a new maximum, reset the result list
                    max_common = common_count
                    result = [[i, j]]
                elif common_count == max_common:
                    # Found another pair matching the current maximum
                    result.append([i, j])
            elif max_common == 0:
                # If we haven't found any common followers yet, 
                # we don't add pairs with 0 common followers to the result
                # unless the problem implies 0 is a valid maximum (not the case here).
                pass

    # If no pairs have common followers, the problem implies returning an empty list
    # or handling the case where max_common remains 0.
    # Based on LeetCode constraints, if max_common is 0, result should be empty.
    if max_common == 0:
        return []

    return result
