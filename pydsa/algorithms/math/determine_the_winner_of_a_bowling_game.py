METADATA = {
    "id": 2660,
    "name": "Determine the Winner of a Bowling Game",
    "slug": "determine_the_winner_of_a_bowling_game",
    "category": "simulation",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Simulate bowling scoring for two players and decide who wins.",
}


def solve(player1: list[int], player2: list[int]) -> int:
    """Determine the winner of a bowling game.

    Args:
        player1: List of pins knocked down in each roll for player 1.
        player2: List of pins knocked down in each roll for player 2.

    Returns:
        1 if player 1's total score is higher,
        2 if player 2's total score is higher,
        0 if both scores are equal.

    Examples:
        >>> solve([10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1],
        ...       [9, 1, 10, 10, 10, 9, 0, 8, 2, 9, 1, 10, 10, 10, 10, 9, 0])
        2
        >>> solve([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        ...       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        1
    """
    def compute_score(rolls: list[int]) -> int:
        """Calculate total bowling score for a sequence of rolls."""
        total_score = 0
        roll_index = 0
        for frame_index in range(10):
            # Strike case: first roll knocks down all pins
            if rolls[roll_index] == 10:
                total_score += 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
                roll_index += 1
            else:
                frame_sum = rolls[roll_index] + rolls[roll_index + 1]
                # Spare case: two rolls sum to 10
                if frame_sum == 10:
                    total_score += 10 + rolls[roll_index + 2]
                else:
                    total_score += frame_sum
                roll_index += 2
        return total_score

    score_player1 = compute_score(player1)
    score_player2 = compute_score(player2)

    if score_player1 > score_player2:
        return 1
    if score_player2 > score_player1:
        return 2
    return 0