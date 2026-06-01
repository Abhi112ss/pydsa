METADATA = {
    "id": 1654,
    "name": "Minimum Jumps to Reach Home",
    "slug": "minimum_jumps_to_reach_home",
    "category": "graph",
    "aliases": [],
    "tags": ["bfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of jumps to reach a target position while avoiding forbidden spots and not making two backward jumps consecutively.",
}


from collections import deque
from typing import List, Set, Tuple


def solve(forbidden: List[int], a: int, b: int, x: int) -> int:
    """Find the minimum number of jumps required to reach position ``x`` starting from ``0``.

    The jumper can move forward by ``a`` units or backward by ``b`` units.
    Landing on any position listed in ``forbidden`` is prohibited.
    Two consecutive backward jumps are not allowed.

    Args:
        forbidden: List of positions that cannot be landed on.
        a: Length of a forward jump.
        b: Length of a backward jump.
        x: Target position to reach.

    Returns:
        The minimum number of jumps needed to reach ``x``.
        Returns ``-1`` if the target is unreachable.

    Examples:
        >>> solve([14, 4, 18, 1, 15], 3, 15, 9)
        3
        >>> solve([8, 3, 16, 6, 12, 20], 15, 13, 11)
        -1
    """
    forbidden_set: Set[int] = set(forbidden)

    # Upper bound for search: far enough to cover any optimal path.
    max_limit: int = max(forbidden + [x]) + a + b

    # Each state is (position, last_move_was_backward)
    visited: Set[Tuple[int, bool]] = set()
    queue: deque[Tuple[int, bool, int]] = deque()

    start_state: Tuple[int, bool, int] = (0, False, 0)
    queue.append(start_state)
    visited.add((0, False))

    while queue:
        current_position, last_was_backward, steps = queue.popleft()

        if current_position == x:
            return steps

        # Try a forward jump.
        forward_position = current_position + a
        forward_state = (forward_position, False)
        if (
            forward_position <= max_limit
            and forward_position not in forbidden_set
            and forward_state not in visited
        ):
            visited.add(forward_state)
            queue.append((forward_position, False, steps + 1))

        # Try a backward jump only if the previous move was not backward.
        if not last_was_backward:
            backward_position = current_position - b
            backward_state = (backward_position, True)
            if (
                backward_position >= 0
                and backward_position not in forbidden_set
                and backward_state not in visited
            ):
                visited.add(backward_state)
                queue.append((backward_position, True, steps + 1))

    return -1