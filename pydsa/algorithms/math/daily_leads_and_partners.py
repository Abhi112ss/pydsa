METADATA = {
    "id": 1693,
    "name": "Daily Leads and Partners",
    "slug": "daily-leads-and-partners",
    "category": "Database",
    "aliases": [],
    "tags": ["sql"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Calculate the number of unique leads and unique partners for each date.",
}

def solve(leads_and_partners_table: list[dict]) -> list[dict]:
    """
    Simulates the SQL query to find daily unique leads and unique partners.

    Args:
        leads_and_partners_table: A list of dictionaries where each dictionary 
            represents a row in the table with keys 'date', 'lead_id', and 'partner_id'.

    Returns:
        A list of dictionaries containing 'day', 'unique_leads', and 'unique_partners',
        sorted by 'day' in ascending order.

    Examples:
        >>> table = [
        ...     {"date": "2020-12-08", "lead_id": 1, "partner_id": 2},
        ...     {"date": "2020-12-08", "lead_id": 1, "partner_id": 3},
        ...     {"date": "2020-12-07", "lead_id": 1, "partner_id": 2}
        ... ]
        >>> solve(table)
        [{'day': '2020-12-07', 'unique_leads': 1, 'unique_partners': 1}, 
         {'day': '2020-12-08', 'unique_leads': 1, 'unique_partners': 2}]
    """
    # Dictionary to store sets of unique IDs per date
    # Structure: { date: {"leads": {id1, id2}, "partners": {id1, id2}} }
    daily_stats: dict[str, dict[str, set[int]]] = {}

    for row in leads_and_partners_table:
        date = row["date"]
        lead_id = row["lead_id"]
        partner_id = row["partner_id"]

        if date not in daily_stats:
            daily_stats[date] = {"leads": set(), "partners": set()}
        
        # Add IDs to sets to automatically handle uniqueness (COUNT DISTINCT)
        daily_stats[date]["leads"].add(lead_id)
        daily_stats[date]["partners"].add(partner_id)

    # Transform the aggregated sets into the required output format
    result = []
    for date in sorted(daily_stats.keys()):
        result.append({
            "day": date,
            "unique_leads": len(daily_stats[date]["leads"]),
            "unique_partners": len(daily_stats[date]["partners"])
        })

    return result
