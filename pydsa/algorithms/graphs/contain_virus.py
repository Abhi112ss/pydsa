METADATA = {
    "id": 749,
    "name": "Contain Virus",
    "slug": "contain-virus",
    "category": "Simulation",
    "aliases": [],
    "tags": ["bfs", "simulation", "matrix", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(R * C * (R + C))",
    "space_complexity": "O(R * C)",
    "description": "Identify the largest infected region and wall it off to minimize the spread of the virus.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Args:
        grid: A 2D integer array representing the infection status.

    Returns:
        The minimum number of cells to wall off to minimize the total number of infected cells.
    """
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def get_region_info(start_r: int, start_c: int) -> tuple[set[tuple[int, int]], set[tuple[int, int]], int]:
        region_cells = set()
        boundary_cells = set()
        queue = [(start_r, start_c)]
        visited[start_r][start_c] = True
        head = 0
        
        while head < len(queue):
            r, c = queue[head]
            head += 1
            region_cells.add((r, c))
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        if not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                    else:
                        boundary_cells.add((nr, nc))
                else:
                    pass
        
        return region_cells, boundary_cells, len(region_cells)

    all_regions = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                all_regions.append(get_region_info(r, c))

    if not all_regions:
        return 0

    best_reduction = -float('inf')
    
    for i in range(len(all_regions)):
        current_region_cells, current_boundary, current_size = all_regions[i]
        
        walls_needed = len(current_boundary)
        
        potential_growth = 0
        for br, bc in current_boundary:
            potential_growth += 1
            
        for j in range(len(all_regions)):
            if i == j:
                continue
            other_region_cells, _, other_size = all_regions[j]
            
            growth_from_other = 0
            for br, bc in current_boundary:
                if (br, bc) in other_region_cells:
                    growth_from_other += 1
            
            potential_growth += growth_from_other

        total_infected_after = 0
        for j in range(len(all_regions)):
            if i == j:
                total_infected_after += current_size
            else:
                other_region_cells, other_boundary, other_size = all_regions[j]
                growth = 0
                for br, bc in other_boundary:
                    if (br, bc) in current_region_cells:
                        growth += 1
                total_infected_after += (other_size + growth)
        
        total_infected_before = sum(reg[2] for reg in all_regions)
        
        current_reduction = total_infected_before - total_infected_after
        
        if current_reduction > best_reduction:
            best_reduction = current_reduction
        elif current_reduction == best_reduction:
            if walls_needed < (best_reduction_walls if 'best_reduction_walls' in locals() else float('inf')):
                pass

    total_infected_before = sum(reg[2] for reg in all_regions)
    
    max_reduction = -1
    min_walls = float('inf')
    
    for i in range(len(all_regions)):
        region_cells, boundary, size = all_regions[i]
        
        walls = len(boundary)
        
        growth_to_others = 0
        for br, bc in boundary:
            if grid[br][bc] == 0:
                growth_to_others += 1
        
        for j in range(len(all_regions)):
            if i == j:
                continue
            other_cells, other_boundary, other_size = all_regions[j]
            
            growth_to_other_region = 0
            for br, bc in boundary:
                if (br, bc) in other_cells:
                    growth_to_other_region += 1
            
            growth_to_others += growth_to_other_region

        current_total_infected = 0
        for j in range(len(all_regions)):
            if i == j:
                current_total_infected += size
            else:
                other_cells, other_boundary, other_size = all_regions[j]
                growth_to_this_region = 0
                for br, bc in other_boundary:
                    if (br, bc) in region_cells:
                        growth_to_this_region += 1
                current_total_infected += (other_size + growth_to_this_region)
        
        reduction = total_infected_before - current_total_infected
        
        if reduction > max_reduction:
            max_reduction = reduction
            min_walls = walls
        elif reduction == max_reduction:
            if walls < min_walls:
                min_walls = walls
                
    return total_infected_before - max_reduction if max_reduction != -1 else 0

def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    all_regions = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                region_cells = set()
                boundary_cells = set()
                queue = [(r, c)]
                visited[r][c] = True
                idx = 0
                while idx < len(queue):
                    curr_r, curr_c = queue[idx]
                    idx += 1
                    region_cells.add((curr_r, curr_c))
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == 1:
                                if not visited[nr][nc]:
                                    visited[nr][nc] = True
                                    queue.append((nr, nc))
                            else:
                                boundary_cells.add((nr, nc))
                all_regions.append({
                    "cells": region_cells,
                    "boundary": boundary_cells,
                    "size": len(region_cells)
                })

    if not all_regions:
        return 0

    total_initial_infected = sum(reg["size"] for reg in all_regions)
    best_final_count = float('inf')
    min_walls_for_best = float('inf')

    for i in range(len(all_regions)):
        target_region = all_regions[i]
        walls = len(target_region["boundary"])
        
        current_total = 0
        for j in range(len(all_regions)):
            if i == j:
                current_total += target_region["size"]
            else:
                other_region = all_regions[j]
                growth = 0
                for br, bc in other_region["boundary"]:
                    if (br, bc) in target_region["cells"]:
                        growth += 1
                current_total += (other_region["size"] + growth)
        
        if current_total < best_final_count:
            best_final_count = current_total
            min_walls_for_best = walls
        elif current_total == best_final_count:
            if walls < min_walls_for_best:
                min_walls_for_best = walls
                
    return best_final_count