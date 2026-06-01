METADATA = {
    "id": 585,
    "name": "Investments in 2016",
    "slug": "investments-in-2016",
    "category": "Database/Logic",
    "aliases": [],
    "tags": ["logic", "hash_map", "frequency_counts"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify unique Ticker-Fraction pairs that have a unique Ticker-Year-Fraction combination.",
}

from collections import Counter

def solve(investments: list[dict]) -> list[dict]:
    """
    Finds unique Ticker-Fraction pairs that have a unique Ticker-Year-Fraction combination.
    
    In the context of the SQL problem, we are looking for (Ticker, Fraction) pairs 
    where the combination of (Ticker, Year, Fraction) appears exactly once in the dataset.

    Args:
        investments: A list of dictionaries, where each dictionary represents an investment.
            Example: {"ticker": "ABC", "fraction": 0.5, "year": 2016, "amount": 100}

    Returns:
        A list of dictionaries containing the unique 'ticker' and 'fraction' pairs.

    Examples:
        >>> data = [
        ...     {"ticker": "ABC", "fraction": 0.5, "year": 2016, "amount": 100},
        ...     {"ticker": "ABC", "fraction": 0.5, "year": 2017, "amount": 200},
        ...     {"ticker": "XYZ", "fraction": 0.1, "year": 2016, "amount": 50},
        ...     {"ticker": "XYZ", "fraction": 0.1, "year": 2016, "amount": 50},
        ... ]
        >>> solve(data)
        [{'ticker': 'ABC', 'fraction': 0.5}]
    """
    # Count occurrences of the (Ticker, Year, Fraction) triplet to find unique entries
    # This mimics the SQL: GROUP BY Ticker, Year, Fraction HAVING COUNT(*) = 1
    triplet_counts = Counter()
    for inv in investments:
        triplet = (inv["ticker"], inv["year"], inv["fraction"])
        triplet_counts[triplet] += 1

    # Identify the unique (Ticker, Fraction) pairs that satisfy the condition
    # We use a set to ensure the final output contains unique (Ticker, Fraction) pairs
    # even if multiple unique triplets share the same Ticker-Fraction (though the 
    # problem logic implies we are filtering the rows themselves).
    unique_results = []
    seen_pairs = set()

    for inv in investments:
        triplet = (inv["ticker"], inv["year"], inv["fraction"])
        
        # Check if this specific Ticker-Year-Fraction combination is unique
        if triplet_counts[triplet] == 1:
            pair = (inv["ticker"], inv["fraction"])
            
            # The problem asks for the unique Ticker-Fraction pairs.
            # If multiple unique triplets result in the same pair, we return the pair once.
            if pair not in seen_pairs:
                unique_results.append({
                    "ticker": inv["ticker"],
                    "fraction": inv["fraction"]
                })
                seen_pairs.add(pair)

    return unique_results
