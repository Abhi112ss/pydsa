METADATA = {
    "id": 433,
    "name": "Minimum Genetic Mutation",
    "slug": "minimum-genetic-mutation",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "shortest_path", "string"],
    "difficulty": "medium",
    "time_complexity": "O(B * N * L)",
    "space_complexity": "O(B)",
    "description": "Find the minimum number of mutations to transform a start gene into an end gene using a bank of valid mutations.",
}

from collections import deque

def solve(start_gene: str, end_gene: str, bank: list[str]) -> int:
    """
    Finds the minimum number of mutations required to transform start_gene to end_gene.
    
    Each mutation must result in a gene present in the bank. A mutation consists 
    of changing exactly one character in the gene string.

    Args:
        start_gene: The initial genetic sequence.
        end_gene: The target genetic sequence.
        bank: A list of valid genetic sequences allowed for mutations.

    Returns:
        The minimum number of mutations required, or -1 if no such mutation sequence exists.

    Examples:
        >>> solve("AACCGGT", "AACCGGC", ["AACCGGC"])
        1
        >>> solve("AACCGGT", "AACCGGC", [])
        -1
        >>> solve("ACGTTGC", "AACCGGC", ["AACCGGC", "AACCGGT", "AACCGGT", "ACGTTGC"])
        3
    """
    # Convert bank to a set for O(1) lookup time
    valid_genes = set(bank)
    
    # If the target gene is not in the bank, it's impossible to reach
    if end_gene not in valid_genes:
        return -1

    # BFS queue stores tuples of (current_gene, current_mutation_count)
    queue = deque([(start_gene, 0)])
    
    # Keep track of visited genes to prevent infinite loops and redundant work
    visited = {start_gene}
    
    while queue:
        current_gene, distance = queue.popleft()
        
        # If we reached the target, return the distance traveled
        if current_gene == end_gene:
            return distance
        
        # Try mutating each of the 7 positions in the gene
        for i in range(len(current_gene)):
            original_char = current_gene[i]
            
            # Try all possible nucleotide mutations: A, C, G, T
            for nucleotide in "ACGT":
                if nucleotide == original_char:
                    continue
                
                # Construct the new gene string
                mutated_gene = (
                    current_gene[:i] + 
                    nucleotide + 
                    current_gene[i+1:]
                )
                
                # If the mutation is valid and hasn't been visited, add to queue
                if mutated_gene in valid_genes and mutated_gene not in visited:
                    visited.add(mutated_gene)
                    queue.append((mutated_gene, distance + 1))
                    
    return -1
