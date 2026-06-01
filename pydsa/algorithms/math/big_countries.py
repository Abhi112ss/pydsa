METADATA = {
    "id": 595,
    "name": "Big Countries",
    "slug": "big_countries",
    "category": "Database",
    "aliases": ["big_countries"],
    "tags": ["logic"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Filter countries that are big by area or population using a simple logical OR condition.",
}

def solve(world: list[dict]) -> list[dict]:
    """Filter countries that are big based on area or population criteria.

    A country is considered big if it has an area of at least 3,000,000 km²
    or a population of at least 25,000,000.

    Args:
        world: A list of dictionaries, each representing a country with keys:
               'name', 'continent', 'area', 'population', 'gdp'.

    Returns:
        A list of dictionaries representing big countries that meet the criteria.

    Examples:
        >>> data = [
        ...     {"name": "Afghanistan", "continent": "Asia", "area": 652230, "population": 25500000, "gdp": 20000000000},
        ...     {"name": "Albania", "continent": "Europe", "area": 28748, "population": 2831741, "gdp": 12960000000},
        ...     {"name": "Algeria", "continent": "Africa", "area": 2381741, "population": 39200000, "gdp": 22000000000},
        ...     {"name": "Andorra", "continent": "Europe", "area": 468, "population": 76177, "gdp": 3660000000},
        ...     {"name": "Angola", "continent": "Africa", "area": 1246700, "population": 29310273, "gdp": 10099000000}
        ... ]
        >>> result = solve(data)
        >>> len(result)
        3
        >>> result[0]["name"]
        'Afghanistan'
        >>> result[1]["name"]
        'Algeria'
        >>> result[2]["name"]
        'Angola'
    """
    # Define the thresholds for a country to be considered big
    MIN_AREA = 3_000_000
    MIN_POPULATION = 25_000_000

    # Filter countries that meet either the area or population threshold
    big_countries = [
        country for country in world
        if country["area"] >= MIN_AREA or country["population"] >= MIN_POPULATION
    ]

    return big_countries