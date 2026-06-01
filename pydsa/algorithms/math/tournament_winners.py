METADATA = {
    "id": 1194,
    "name": "Tournament Winners",
    "slug": "tournament-winners",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "ranking", "aggregation"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total score for each player in each tournament and rank them within their respective tournaments.",
}

from dataclasses import dataclass
from typing import List, Dict


@dataclass(frozen=True)
class Match:
    tournament_id: int
    player_id: int
    score: int


def solve(matches: List[Match]) -> List[Dict[str, int]]:
    """
    Calculates the total score for each player per tournament and ranks them.
    
    The ranking is determined by the total score in descending order. 
    If scores are tied, the player with the lower player_id is ranked higher.
    
    Args:
        matches: A list of Match objects containing tournament_id, player_id, and score.
        
    Returns:
        A list of dictionaries where each dictionary contains 'tournament_id', 
        'player_id', 'total_score', and 'rank'.
        
    Examples:
        >>> matches = [
        ...     Match(1, 1, 10), Match(1, 2, 10), Match(1, 3, 5),
        ...     Match(2, 1, 5), Match(2, 2, 15)
        ... ]
        >>> solve(matches)
        [{'tournament_id': 1, 'player_id': 1, 'total_score': 10, 'rank': 1}, ...]
    """
    # Step 1: Aggregate scores per (tournament_id, player_id)
    # Using a dictionary to simulate SQL GROUP BY tournament_id, player_id
    score_map: Dict[tuple[int, int], int] = {}
    for match in matches:
        key = (match.tournament_id, match.player_id)
        score_map[key] = score_map.get(key, 0) + match.score

    # Step 2: Flatten the aggregated data into a list of records
    # Each record represents a player's performance in a specific tournament
    records = []
    for (tournament_id, player_id), total_score in score_map.items():
        records.append({
            "tournament_id": tournament_id,
            "player_id": player_id,
            "total_score": total_score
        })

    # Step 3: Sort records to simulate Window Function (RANK() OVER ...)
    # Primary sort: tournament_id (to group players together)
    # Secondary sort: total_score DESC (highest score first)
    # Tertiary sort: player_id ASC (tie-breaker for ranking)
    records.sort(key=lambda x: (x["tournament_id"], -x["total_score"], x["player_id"]))

    # Step 4: Assign ranks within each tournament group
    # We iterate through the sorted list and increment rank only when 
    # the tournament_id changes or the score/tie-breaker criteria changes.
    # Note: Standard SQL RANK() gives same rank to ties. 
    # However, the problem logic usually implies a specific tie-breaking rule.
    # Here we implement a dense-like rank based on the sorted order.
    
    results: List[Dict[str, int]] = []
    if not records:
        return results

    current_rank = 1
    for i in range(len(records)):
        # If it's not the first element and the tournament changed, reset rank
        if i > 0 and records[i]["tournament_id"] != records[i-1]["tournament_id"]:
            current_rank = 1
        
        # If it's not the first element and the score/tie-breaker is different 
        # within the same tournament, the rank increments.
        # To mimic SQL RANK() exactly: if scores are equal, they get the same rank.
        # But the problem specifies player_id as a tie-breaker, making every 
        # entry in our sorted list unique in its rank position.
        
        # Check if current record has the same score as previous in same tournament
        if i > 0 and records[i]["tournament_id"] == records[i-1]["tournament_id"]:
            if records[i]["total_score"] == records[i-1]["total_score"]:
                # In standard SQL RANK(), ties get the same rank.
                # But since we use player_id as a tie-breaker in sorting, 
                # we follow the sorted order.
                pass 
            else:
                # If score is different, we calculate rank based on position
                # To strictly follow SQL RANK() behavior:
                # We need to count how many people had higher scores.
                pass

        # Re-calculating rank based on the sorted order to handle the "tie-breaker" requirement
        # Since the sort includes player_id, every player is effectively unique.
        # We calculate rank by checking how many players in the same tournament 
        # have a strictly better score.
        
        # Optimization: Since we already sorted by (tournament, -score, player_id),
        # the rank is simply the count of players in the same tournament 
        # who have a strictly higher score than the current player.
        
        # However, the prompt asks for the optimal algorithm. 
        # Let's use the sorted property:
        if i > 0 and records[i]["tournament_id"] == records[i-1]["tournament_id"]:
            if records[i]["total_score"] == records[i-1]["total_score"]:
                # If scores are tied, they get the same rank (SQL RANK behavior)
                # But the problem says "use player_id as tie-breaker". 
                # This usually means the tie-breaker is part of the ORDER BY, 
                # not the RANK() equality condition.
                # If the tie-breaker is in ORDER BY, the rank is effectively 1, 2, 3...
                # Let's assume standard SQL RANK() where ties in score get same rank.
                # But the prompt implies the tie-breaker makes the rank unique.
                # We will treat the sorted position as the rank.
                current_rank = i - (i - current_rank) # This is a placeholder
        
        # Correct approach for "Rank with tie-breaker in ORDER BY":
        # The rank is the position in the sorted list within the group.
        # Let's find the start of the current tournament group.
        
        # Finding the rank:
        # We'll use a simple counter that resets per tournament.
        # Because the sort is (tournament, -score, player_id), 
        # the rank is simply the index within the tournament group + 1.
        
        # Let's find the start index of the current tournament
        # (In a production environment, we'd track this in the loop)
        pass

    # Refined Step 4:
    final_results = []
    group_start_idx = 0
    for i in range(len(records)):
        if i > 0 and records[i]["tournament_id"] != records[i-1]["tournament_id"]:
            group_start_idx = i
        
        # The rank is the position relative to the start of the tournament group
        # This satisfies the requirement of using player_id as a tie-breaker.
        rank = i - group_start_idx + 1
        
        record = records[i].copy()
        record["rank"] = rank
        final_results.append(record)

    return final_results
