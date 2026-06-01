METADATA = {
    "id": 3093,
    "name": "Longest Common Suffix Queries",
    "slug": "longest_common_suffix_queries",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "trie", "binary_search", "suffix_array"],
    "difficulty": "hard",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Find the length of the longest common suffix for given pairs of strings using efficient string matching techniques.",
}

class SuffixArraySolver:
    """
    A solver class that uses a Suffix Array and LCP (Longest Common Prefix) array
    to answer Longest Common Suffix queries by reversing the strings.
    """

    def __init__(self, strings: list[str]):
        # Reverse all strings to turn suffix queries into prefix queries
        self.reversed_strings = [s[::-1] for s in strings]
        # Concatenate all reversed strings with unique separators to build a single large string
        # Using a single large string allows us to use Suffix Array techniques
        self.combined_string = ""
        self.string_offsets = []
        
        for s in self.reversed_strings:
            self.string_offsets.append(len(self.combined_string))
            self.combined_string += s + "$"  # $ is a separator
            
        self.n = len(self.combined_string)
        self.sa = self._build_suffix_array()
        self.lcp = self._build_lcp()
        self.rank = [0] * self.n
        for i in range(self.n):
            self.rank[self.sa[i]] = i
        self.sparse_table = self._build_sparse_table()

    def _build_suffix_array(self) -> list[int]:
        """Builds the suffix array in O(N log N) time."""
        n = self.n
        sa = list(range(n))
        rank = [ord(self.combined_string[i]) for i in range(n)]
        k = 1
        while k < n:
            # Sort by (rank[i], rank[i+k] if exists else -1)
            key = lambda x: (rank[x], rank[x + k] if x + k < n else -1)
            sa.sort(key=key)
            
            new_rank = [0] * n
            for i in range(1, n):
                new_rank[sa[i]] = new_rank[sa[i - 1]] + (1 if key(sa[i]) > key(sa[i - 1]) else 0)
            rank = new_rank
            if rank[sa[n - 1]] == n - 1:
                break
            k *= 2
        return sa

    def _build_lcp(self) -> list[int]:
        """Builds the LCP array using Kasai's algorithm in O(N)."""
        n = self.n
        lcp = [0] * n
        rank = [0] * n
        for i in range(n):
            rank[self.sa[i]] = i
        
        h = 0
        for i in range(n):
            if rank[i] > 0:
                j = self.sa[rank[i] - 1]
                while i + h < n and j + h < n and self.combined_string[i + h] == self.combined_string[j + h]:
                    h += 1
                lcp[rank[i]] = h
                if h > 0:
                    h -= 1
        return lcp

    def _build_sparse_table(self) -> list[list[int]]:
        """Builds a sparse table for Range Minimum Query (RMQ) on the LCP array."""
        n = self.n
        max_log = n.bit_length()
        st = [[0] * max_log for _ in range(n)]
        for i in range(n):
            st[i][0] = self.lcp[i]
        
        for j in range(1, max_log):
            for i in range(n - (1 << j) + 1):
                st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
        return st

    def query_lcp(self, idx1: int, idx2: int) -> int:
        """Returns the LCP of two suffixes starting at idx1 and idx2 in the combined string."""
        if idx1 == idx2:
            return self.n - idx1
        
        r1, r2 = self.rank[idx1], self.rank[idx2]
        if r1 > r2:
            r1, r2 = r2, r1
        
        # LCP(i, j) is the minimum in the LCP array between rank[i]+1 and rank[j]
        r1 += 1
        length = r2 - r1 + 1
        k = length.bit_length() - 1
        return min(self.sparse_table[r1][k], self.sparse_table[r2 - (1 << k) + 1][k])

def solve(strings: list[str], queries: list[list[int]]) -> list[int]:
    """
    Solves the Longest Common Suffix queries.

    Args:
        strings: A list of strings to query suffixes from.
        queries: A list of queries where each query is [i, j] representing indices of strings.

    Returns:
        A list of integers representing the length of the longest common suffix for each query.

    Examples:
        >>> solve(["abcde", "fbcde", "abc"], [[0, 1], [0, 2]])
        [3, 2]
    """
    if not strings:
        return []

    # We use a Suffix Array approach on reversed strings.
    # To handle multiple strings, we concatenate them with unique separators.
    # However, for large N, unique separators are hard. 
    # A simpler way for this specific problem is to use the reversed strings 
    # and find the LCP of the starting positions of the reversed strings.
    
    # Step 1: Reverse strings
    rev_strings = [s[::-1] for s in strings]
    
    # Step 2: Build a single combined string with a separator that won't match any char
    # Since we only care about LCP within the bounds of the original strings,
    # we can use a single separator '#' and carefully bound the LCP result.
    combined = []
    offsets = []
    lengths = []
    for s in rev_strings:
        offsets.append(len(combined))
        lengths.append(len(s))
        combined.append(s)
        combined.append("#") # Separator
    
    full_str = "".join(combined)
    n = len(full_str)
    
    # Step 3: Build Suffix Array and LCP
    # Using a standard O(N log N) or O(N log^2 N) construction
    sa = list(range(n))
    rank = [ord(c) for c in full_str]
    k = 1
    while k < n:
        # Sort by current rank and rank at offset k
        key = lambda x: (rank[x], rank[x + k] if x + k < n else -1)
        sa.sort(key=key)
        new_rank = [0] * n
        for i in range(1, n):
            new_rank[sa[i]] = new_rank[sa[i-1]] + (1 if key(sa[i]) > key(sa[i-1]) else 0)
        rank = new_rank
        if rank[sa[n-1]] == n - 1: break
        k *= 2
        
    # Step 4: Build LCP array (Kasai's)
    lcp = [0] * n
    inv_sa = [0] * n
    for i in range(n):
        inv_sa[sa[i]] = i
    
    h = 0
    for i in range(n):
        if inv_sa[i] > 0:
            j = sa[inv_sa[i] - 1]
            while i + h < n and j + h < n and full_str[i + h] == full_str[j + h] and full_str[i+h] != '#':
                h += 1
            lcp[inv_sa[i]] = h
            if h > 0: h -= 1
            
    # Step 5: Sparse Table for RMQ
    max_log = n.bit_length()
    st = [[0] * max_log for _ in range(n)]
    for i in range(n):
        st[i][0] = lcp[i]
    for j in range(1, max_log):
        for i in range(n - (1 << j) + 1):
            st[i][j] = min(st[i][j-1], st[i + (1 << (j-1))][j-1])
            
    def get_lcp(idx1: int, idx2: int) -> int:
        r1, r2 = inv_sa[idx1], inv_sa[idx2]
        if r1 > r2: r1, r2 = r2, r1
        r1 += 1
        length = r2 - r1 + 1
        if length <= 0: return 0
        k_val = length.bit_length() - 1
        return min(st[r1][k_val], st[r2 - (1 << k_val) + 1][k_val])

    # Step 6: Process queries
    results = []
    for i, j in queries:
        # The suffix of the reversed string starts at offsets[i]
        # The common prefix of reversed strings is the common suffix of original strings
        res = get_lcp(offsets[i], offsets[j])
        # The LCP cannot exceed the length of either string
        res = min(res, lengths[i], lengths[j])
        results.append(res)
        
    return results
