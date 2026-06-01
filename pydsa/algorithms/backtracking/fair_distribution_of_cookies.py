METADATA = {
    "id": 2305,
    "name": "Fair Distribution of Cookies",
    "slug": "fair-distribution-of-cookies",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "optimization"],
    "difficulty": "hard",
    "time_complexity": "O(children^cookies)",
    "space_complexity": "O(cookies)",
    "description": "Distribute cookies to children such that the maximum number of cookies any child receives is minimized.",
}

def solve(cookies: list[int], children: int) -> int:
    """
    Distributes cookies to children to minimize the maximum number of cookies any child gets.

    Args:
        cookies: A list of integers representing the number of cookies in each bag.
        children: The number of children available to receive cookies.

    Returns:
        The minimum possible value of the maximum number of cookies any child receives.

    Examples:
        >>> solve([8, 15, 10, 20, 8], 3)
        20
        >>> solve([1, 1, 1, 1], 2)
        2
    """
    # current_distribution stores the total cookies assigned to each child
    current_distribution = [0] * children
    # Initialize result with a large value (sum of all cookies is a safe upper bound)
    min_max_cookies = sum(cookies)

    def backtrack(cookie_index: int) -> None:
        nonlocal min_max_cookies

        # Base case: all cookie bags have been distributed
        if cookie_index == len(cookies):
            current_max = max(current_distribution)
            min_max_cookies = min(min_max_cookies, current_max)
            return

        # Pruning: if the current max already exceeds our best found, stop exploring this path
        if max(current_distribution) >= min_max_cookies:
            return

        # Try giving the current cookie bag to each child
        for child_idx in range(children):
            # Optimization: If multiple children have 0 cookies, only give to the first one
            # to avoid redundant permutations of the same distribution.
            if child_idx > 0 and current_distribution[child_idx] == 0 and current_distribution[child_idx - 1] == 0:
                continue

            # Assign the bag
            current_distribution[child_idx] += cookies[cookie_index]
            
            # Recurse to the next bag
            backtrack(cookie_index + 1)
            
            # Backtrack: remove the bag to try the next child
            current_distribution[child_idx] -= cookies[cookie_index]

    # Sort cookies in descending order to hit pruning conditions faster
    cookies.sort(reverse=True)
    backtrack(0)
    return min_max_cookies
