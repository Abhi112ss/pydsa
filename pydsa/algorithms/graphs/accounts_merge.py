METADATA = {
    "id": 721,
    "name": "Accounts Merge",
    "slug": "accounts-merge",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "dfs", "hash_map", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(A log A)",
    "space_complexity": "O(A)",
    "description": "Merge accounts that share common email addresses using a Disjoint Set Union approach.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    
    def __init__(self, elements: list[str]) -> None:
        self.parent = {element: element for element in elements}
        self.rank = {element: 0 for element in elements}

    def find(self, i: str) -> str:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: str, j: str) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1

def solve(accounts: list[list[str]]) -> list[list[str]]:
    """
    Merges accounts that share common email addresses.

    Args:
        accounts: A list of lists where each sublist contains a name followed by emails.

    Returns:
        A list of merged accounts, where each account starts with the name followed by sorted emails.

    Examples:
        >>> solve([["John","a@m.com","b@m.com"],["John","c@m.com"],["John","a@m.com","c@m.com"]])
        [['John', 'a@m.com', 'b@m.com', 'c@m.com']]
    """
    dsu = UnionFind([]) # Placeholder, will be populated via email collection
    email_to_name = {}
    all_emails = []

    # Step 1: Map every email to its owner and collect all unique emails
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            email_to_name[email] = name
            all_emails.append(email)
    
    # Re-initialize DSU with all unique emails found
    dsu = UnionFind(list(set(all_emails)))

    # Step 2: Union emails that appear in the same account
    for account in accounts:
        first_email = account[1]
        for subsequent_email in account[2:]:
            dsu.union(first_email, subsequent_email)

    # Step 3: Group emails by their representative (root) in DSU
    merged_groups: dict[str, list[str]] = {}
    for email in email_to_name:
        root = dsu.find(email)
        if root not in merged_groups:
            merged_groups[root] = []
        merged_groups[root].append(email)

    # Step 4: Format the output: [Name, sorted_emails...]
    result = []
    for root, emails in merged_groups.items():
        name = email_to_name[root]
        result.append([name] + sorted(emails))

    return result
