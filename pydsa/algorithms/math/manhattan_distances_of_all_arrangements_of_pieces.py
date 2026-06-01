METADATA = {
    "id": 3426,
    "name": "Manhattan Distances of All Arrangements of Pieces",
    "slug": "manhattan-distances-of-all-arrangements-of-pieces",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of Manhattan distances between all possible arrangements of pieces on a grid using combinatorial contribution analysis.",
}

def solve(n: int, m: int, pieces: list[list[int]]) -> int:
    """
    Calculates the sum of Manhattan distances of all possible arrangements of pieces.
    
    The problem asks for the sum of Manhattan distances between all possible 
    permutations of piece placements. Since Manhattan distance is |x1 - x2| + |y1 - y2|,
    we can solve for X and Y dimensions independently.
    
    For a single dimension (e.g., X), if we have N positions and K pieces, 
    the total sum is the sum of |xi - xj| over all pairs of pieces across all 
    possible valid arrangements.
    
    Args:
        n: Number of rows in the grid.
        m: Number of columns in the grid.
        pieces: A list of [r, c] coordinates representing the pieces.
        
    Returns:
        The total sum of Manhattan distances modulo 10^9 + 7.
        
    Examples:
        >>> solve(2, 2, [[0, 0], [1, 1]])
        2
    """
    MOD = 10**9 + 7

    def calculate_dimension_sum(coords: list[int], limit: int, num_pieces: int) -> int:
        """
        Calculates the sum of distances for a single dimension.
        
        Args:
            coords: The coordinates of the pieces in this dimension.
            limit: The size of the dimension (n or m).
            num_pieces: Total number of pieces.
            
        Returns:
            The sum of distances for this dimension.
        """
        # Sort coordinates to use the prefix sum approach for |a - b|
        coords.sort()
        
        # Total ways to arrange the remaining (num_pieces - 2) pieces 
        # in the remaining (limit - 2) spots is not quite right because 
        # the pieces are distinct and the spots are distinct.
        # Actually, the problem is simpler: we want the sum of |p_i - p_j| 
        # over all pairs (i, j) and all valid permutations.
        
        # Let's use the contribution of each pair of pieces (i, j).
        # For a fixed pair of pieces at positions x_i and x_j, 
        # there are (limit - 2)! ways to place the other pieces if we 
        # were just placing them in a line. But we are on a grid.
        
        # Correct approach:
        # Total sum = Sum_{i < j} [ (Sum over all arrangements of |x_i - x_j|) ]
        # For a fixed pair of pieces i and j, and fixed positions x_i and x_j:
        # The number of ways to place the other (K-2) pieces in the remaining 
        # (N*M - 2) cells is P(N*M - 2, K - 2).
        
        # However, the problem implies we are arranging the *given* pieces 
        # into the grid. If the pieces are distinct, we choose K cells out of N*M.
        # Total arrangements = (N*M) * (N*M - 1) * ... * (N*M - K + 1)
        
        # Let's simplify: The sum of |x_i - x_j| over all pairs (i, j) 
        # and all possible placements.
        # For any two cells (r1, c1) and (r2, c2), how many arrangements 
        # have piece 1 at (r1, c1) and piece 2 at (r2, c2)?
        # Answer: P(N*M - 2, K - 2).
        
        # Total Sum = P(N*M - 2, K - 2) * Sum_{all pairs of cells (u, v)} dist(u, v)
        # where dist(u, v) is the distance in one dimension.
        
        # Wait, the problem asks for the sum of Manhattan distances of ALL arrangements.
        # This means we sum the Manhattan distance of the configuration for every permutation.
        # Total Sum = Sum_{permutations} Sum_{i < j} (|r_i - r_j| + |c_i - c_j|)
        # Total Sum = Sum_{i < j} Sum_{permutations} (|r_i - r_j| + |c_i - c_j|)
        
        # By symmetry, Sum_{permutations} |r_i - r_j| is the same for all i, j.
        # There are K(K-1)/2 pairs of pieces.
        # For a fixed pair (i, j), the sum of |r_i - r_j| over all permutations is:
        # (Number of ways to place i and j in cells (r1, c1) and (r2, c2)) * |r1 - r2|
        # Sum_{all cell pairs (u, v)} |r_u - r_v| * P(N*M - 2, K - 2)
        
        # Let S = Sum_{all cell pairs (u, v)} |r_u - r_v|
        # Total Sum = [K(K-1)/2] * [S / (N*M * (N*M - 1) / 2)] * [P(N*M, K)] ... No.
        
        # Let's use the contribution of each pair of cells (u, v).
        # A pair of cells (u, v) contributes |r_u - r_v| to the total sum 
        # if piece i is at u and piece j is at v (or vice versa).
        # There are K(K-1) ordered pairs of pieces (i, j).
        # For each ordered pair, there are P(N*M - 2, K - 2) ways to place the rest.
        # Total Sum = Sum_{u != v} |r_u - r_v| * P(N*M - 2, K - 2) * (K * (K-1) / 2) ... No.
        
        # Let's re-evaluate:
        # Total Sum = Sum_{i < j} Sum_{all arrangements} (|r_i - r_j| + |c_i - c_j|)
        # For a fixed i, j, the sum of |r_i - r_j| over all arrangements is:
        # Sum_{u, v in Grid, u != v} |r_u - r_v| * P(N*M - 2, K - 2)
        # Note: u and v are cells.
        
        # Let's calculate S_dim = Sum_{u, v in Grid, u != v} |coord_u - coord_v|
        # For a 1D dimension of size L, there are M cells for each coordinate.
        # So for each coordinate x in [0, L-1], there are M cells.
        # S_dim = Sum_{x1=0}^{L-1} Sum_{x2=0}^{L-1} (M * M) * |x1 - x2|
        # (Note: u != v is handled because |x1 - x2| = 0 when x1 = x2)
        
        # Total Sum = [K(K-1)/2] * [Sum_{u, v in Grid, u != v} (|r_u - r_v| + |c_u - c_v|)] * P(N*M - 2, K - 2) / (N*M * (N*M - 1) / 2) ... No.
        
        # Let's use the simplest logic:
        # Total Sum = (Number of ways to choose 2 pieces) * (Sum of |r_u - r_v| over all pairs of cells u, v) * (Ways to place remaining K-2 pieces)
        # Total Sum = [K(K-1)/2] * [Sum_{u < v in Grid} (|r_u - r_v| + |c_u - c_v|)] * P(N*M - 2, K - 2)
        
        # Let's calculate Sum_{u < v in Grid} |r_u - r_v|:
        # This is Sum_{x1=0}^{L-1} Sum_{x2=x1+1}^{L-1} (M * M) * (x2 - x1)
        # where M is the size of the OTHER dimension.
        
        # Let's refine:
        # Let K = number of pieces.
        # Let TotalCells = N * M.
        # Total Sum = [K(K-1)/2] * [Sum_{u < v in Grid} (|r_u - r_v| + |c_u - c_v|)] * P(TotalCells - 2, K - 2)
        
        # Sum_{u < v in Grid} |r_u - r_v|:
        # Each pair of rows (i, j) with i < j has M * M pairs of cells.
        # Sum_{0 <= i < j < L} (M * M) * (j - i)
        
        # Sum_{0 <= i < j < L} (j - i) = Sum_{d=1}^{L-1} d * (L - d)
        # This is a standard sum: (L^3 - L) / 6.
        
        # So, Sum_{u < v in Grid} |r_u - r_v| = M^2 * (L^3 - L) / 6
        # And Sum_{u < v in Grid} |c_u - c_v| = N^2 * (W^3 - W) / 6
        
        # Wait, the pieces are given as coordinates. Does the problem mean 
        # we only rearrange the *given* pieces? Yes.
        # Does it mean the pieces are distinct? Usually, in these problems, 
        # "arrangements of pieces" implies the pieces are distinct.
        # If pieces are distinct, the formula above is correct.
        
        # Let's re-read: "Manhattan Distances of All Arrangements of Pieces".
        # If the pieces are at specific coordinates, we are just permuting them.
        # But the problem says "arrangements of pieces", which usually means 
        # we pick K cells out of N*M and place the K pieces there.
        
        # Let's re-verify the formula:
        # Total Sum = [K(K-1)/2] * [Sum_{u < v in Grid} (|r_u - r_v| + |c_u - c_v|)] * P(TotalCells - 2, K - 2)
        # Let's test with N=2, M=2, K=2.
        # TotalCells = 4. K(K-1)/2 = 1. P(4-2, 2-2) = P(2, 0) = 1.
        # Sum_{u < v} |r_u - r_v|:
        # Rows: 0, 0, 1, 1. Pairs: (0,0), (0,1), (0,1), (0,1), (0,1), (1,1).
        # |r_u - r_v|: 0, 1, 1, 1, 1, 0. Sum = 4.
        # Using formula: M^2 * (L^3 - L) / 6 = 2^2 * (2^3 - 2) / 6 = 4 * 6 / 6 = 4. Correct.
        # Sum_{u < v} |c_u - c_v|: N^2 * (W^3 - W) / 6 = 2^2 * (2^3 - 2) / 6 = 4.
        # Total Sum = 1 * (4 + 4) * 1 = 8.
        
        # Wait, the example says N=2, M=2, pieces=[[0,0], [1,1]] -> 2.
        # My formula gives 8. Why?
        # Ah, the example might mean we only permute the *given* pieces 
        # among the *given* coordinates.
        # If we only permute the pieces among the K given coordinates:
        # Total Sum = Sum_{permutations sigma} Sum_{i < j} dist(piece_i_at_pos_sigma(i), piece_j_at_pos_sigma(j))
        # If we only use the K given coordinates, the problem is:
        # Sum_{sigma} Sum_{i < j} dist(coord_{sigma(i)}, coord_{sigma(j)})
        # Since we sum over all permutations, every pair of coordinates (u, v) 
        # from the K given coordinates will be occupied by (piece_i, piece_j) 
        # exactly (K-2)! * 2 times (for i,j and j,i).
        # Wait, for a fixed pair of indices i < j, and a fixed pair of coordinates u, v:
        # There are (K-2)! permutations where piece i is at u and piece j is at v.
        # There are (K-2)! permutations where piece i is at v and piece j is at u.
        # Total Sum = Sum_{i < j} Sum_{u < v in K_coords} [ (K-2)! * dist(u, v) + (K-2)! * dist(v, u) ]
        # Total Sum = [K(K-1)/2] * [2 * (K-2)! * Sum_{u < v in K_coords} dist(u, v)]
        # Total Sum = (K!) * Sum_{u < v in K_coords} dist(u, v) / (K(K-1)/2) ... No.
        
        # Let's re-calculate:
        # For each pair of indices i < j, we sum dist(pos_i, pos_j) over all K! permutations.
        # In K! permutations, the pair (pos_i, pos_j) takes all possible ordered 
        # pairs of coordinates (u, v) from the K given coordinates exactly (K-2)! times.
        # Total Sum = Sum_{i < j} [ Sum_{u != v in K_coords} (K-2)! * dist(u, v) ]
        # Total Sum = [K(K-1)/2] * (K-2)! * Sum_{u != v in K_coords} dist(u, v)
        # Total Sum = [K! / 2] * Sum_{u != v in K_coords} dist(u, v)
        # Total Sum = K! * Sum_{u < v in K_coords} dist(u, v)
        
        # Let's test N=2, M=2, K=2, coords=[(0,0), (1,1)]:
        # K! = 2. Sum_{u < v} dist(u, v) = dist((0,0), (1,1)) = |0-1| + |0-1| = 2.
        # Total Sum = 2 * 2 = 4? Still not 2.
        # Wait, if the pieces are NOT distinct, then we divide by K!.
        # If the pieces are identical, there is only 1 arrangement for each set of cells.
        # But the problem says "arrangements of pieces". If pieces are identical, 
        # there's only one arrangement for a fixed set of cells.
        # If the pieces are at [0,0] and [1,1], and they are identical, 
        # there is only 1 arrangement: piece at (0,0) and piece at (1,1).
        # The distance is 2.
        # If the example output is 2, it means the pieces are identical 
        # and we only consider the set of coordinates they occupy.
        # But "all arrangements" usually means we permute the pieces.
        # If the pieces are identical, there is only 1 arrangement.
        # If the pieces are distinct, there are K! arrangements.
        # If the example output is 2, and the distance is 2, it means 
        # the sum is 2. This happens if K! = 1 (identical pieces) 
        # or if we are looking for the AVERAGE distance.
        # Let's re-read: "Sum of Manhattan distances of all arrangements".
        # If K=2 and the only arrangement is {(0,0), (1,1)}, the sum is 2.
        # This implies the pieces are identical and we are just 
        # choosing K cells from the N*M grid? No, that would be many more.
        # It must mean we are only permuting the pieces among the K given coordinates.
        # And if the pieces are identical