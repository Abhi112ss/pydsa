METADATA = {
    "id": 1527,
    "name": "Patients With a Condition",
    "slug": "patients-with-a-condition",
    "category": "Database",
    "aliases": [],
    "tags": ["sql"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find patients whose diagnoses contain a specific condition code starting with a specific prefix.",
}

def solve(patients: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Simulates the SQL query to find patients with a specific condition.
    
    The condition must be at the start of the string or preceded by a space.
    In SQL, this is typically handled by: WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'

    Args:
        patients: A list of dictionaries where each dictionary represents a patient 
                  with 'patient_id' and 'conditions' keys.

    Returns:
        A list of dictionaries containing the 'patient_id' of patients meeting the criteria.

    Examples:
        >>> patients = [
        ...     {"patient_id": "1", "conditions": "SNORE DIAB1"},
        ...     {"patient_id": "2", "conditions": "ACNE DIAB1"},
        ...     {"patient_id": "3", "conditions": "DIAB100"},
        ...     {"patient_id": "4", "conditions": "ACNE DIAB100"}
        ... ]
        >>> solve(patients)
        [{'patient_id': '1'}, {'patient_id': '2'}, {'patient_id': '3'}]
    """
    target_prefix = "DIAB1"
    result = []

    for patient in patients:
        conditions_str = patient["conditions"]
        # Split the string into individual condition codes
        # This handles the logic of 'starts with' or 'preceded by space'
        condition_list = conditions_str.split()
        
        # Check if any condition in the list starts with the target prefix
        match_found = False
        for condition in condition_list:
            if condition.startswith(target_prefix):
                match_found = True
                break
        
        if match_found:
            result.append({"patient_id": patient["patient_id"]})

    return result
