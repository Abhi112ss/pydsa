METADATA = {
    "id": 352,
    "name": "Data Stream as Disjoint Intervals",
    "slug": "data-stream-as-disjoint-intervals",
    "category": "Design",
    "aliases": [],
    "tags": ["binary_search_tree", "design", "intervals"],
    "difficulty": "hard",
    "time_complexity": "O(log N)",
    "space_complexity": "O(N)",
    "description": "Design a data structure that receives a stream of integers and returns a list of disjoint intervals.",
}

import bisect

class SummaryRanges:
    """
    A data structure that maintains a set of disjoint intervals from a stream of integers.
    
    Uses a sorted list of interval boundaries to simulate a balanced BST behavior,
    allowing for O(log N) search and O(N) worst-case insertion (due to list shifts),
    though amortized performance for interval management is highly efficient.
    """

    def __init__(self) -> None:
        """Initializes the data structure with an empty list of intervals."""
        # intervals is a list of [start, end] pairs, kept sorted by start.
        self.intervals: list[list[int]] = []

    def addNum(self, value: int) -> None:
        """
        Adds a new integer to the data structure and merges overlapping intervals.

        Args:
            value: The integer to add to the stream.
        """
        # Find the insertion point using binary search to maintain sorted order.
        # We look for where this value would fit relative to existing interval starts.
        idx = bisect.bisect_left(self.intervals, [value, value])
        
        # Check if the value is already contained within an existing interval.
        # Case 1: The value is inside the interval at idx-1.
        if idx > 0 and self.intervals[idx - 1][1] >= value:
            return
        
        # Case 2: The value is inside the interval at idx (if idx < len).
        # This is actually covered by the logic below, but we check for exact containment.
        if idx < len(self.intervals) and self.intervals[idx][0] <= value <= self.intervals[idx][1]:
            return

        # Determine the range of intervals that will be merged.
        # We check the interval before (idx-1) and the interval at (idx).
        merge_start = value
        merge_end = value
        
        # Check if the new value can merge with the preceding interval.
        if idx > 0 and self.intervals[idx - 1][1] + 1 == value:
            merge_start = self.intervals[idx - 1][0]
            idx -= 1 # Move index back to start of the merge range
            
        # Check if the new value can merge with the succeeding interval(s).
        # We use a while loop to consume all intervals that become contiguous.
        while idx < len(self.intervals) and self.intervals[idx][0] == merge_end + 1:
            merge_end = self.intervals[idx][1]
            idx += 1
            
        # If the value was adjacent to the previous interval, we replace the previous one.
        # Otherwise, we insert a new interval.
        # The slice replacement handles both single insertion and multi-interval merging.
        # We calculate the actual start index for the slice based on whether we merged backwards.
        
        # Re-calculating the slice range:
        # If we merged with idx-1, the slice starts at idx-1.
        # If we didn't, the slice starts at the current idx.
        
        # Let's refine the logic: 
        # 1. Find if value is already covered.
        # 2. Find the range of intervals to remove.
        # 3. Insert the new merged interval.
        
        # Re-implementing the merge logic for clarity and correctness:
        # Find the first interval that could potentially merge with 'value'
        # (i.e., interval.end >= value - 1)
        # and the last interval that could merge (i.e., interval.start <= value + 1)
        
        # Find index of first interval where interval.end >= value - 1
        # Since intervals are disjoint and sorted, we can use binary search on ends.
        # However, for simplicity in this implementation, we use the idx found via bisect.
        
        # Let's use a more robust approach:
        # 1. Find where 'value' would be inserted.
        # 2. Check neighbors.
        
        # Resetting logic for a clean implementation:
        pass

    def addNum(self, value: int) -> None:
        """
        Adds a new integer to the data structure and merges overlapping intervals.
        """
        # Find the position where this value would be inserted to keep intervals sorted.
        # We search based on the start of the intervals.
        idx = bisect.bisect_left(self.intervals, [value, value])
        
        # 1. Check if 'value' is already contained in the interval at idx-1.
        if idx > 0 and self.intervals[idx - 1][1] >= value:
            return
        
        # 2. Check if 'value' is already contained in the interval at idx.
        if idx < len(self.intervals) and self.intervals[idx][0] <= value:
            # This case is actually handled by the 'already contained' check above
            # if the interval at idx-1 was the one containing it.
            # If idx is the first interval and it contains value, idx-1 doesn't exist.
            # But if idx < len and intervals[idx][0] <= value, and we know 
            # intervals[idx-1][1] < value, then value must be inside intervals[idx].
            # However, since intervals are disjoint, if intervals[idx][0] <= value,
            # and we know value is not in idx-1, then value must be in idx.
            # But wait, if intervals[idx][0] == value, it's not "contained" in the sense 
            # of being strictly inside, but it's a duplicate.
            if self.intervals[idx][0] <= value <= self.intervals[idx][1]:
                return

        # 3. Identify the range of intervals to merge.
        # The new interval will start at min(value, intervals[idx-1].start) 
        # if intervals[idx-1].end + 1 == value.
        # The new interval will end at max(value, intervals[idx].end)
        # if intervals[idx].start - 1 == value.
        
        new_start = value
        new_end = value
        
        # Check left neighbor
        if idx > 0 and self.intervals[idx - 1][1] + 1 == value:
            new_start = self.intervals[idx - 1][0]
            idx -= 1 # We will replace the interval at idx-1
            
        # Check right neighbor(s)
        # We might merge multiple intervals if they are all contiguous.
        # e.g., value=5, intervals=[[1,2], [4,4], [6,6], [8,8]] -> [4,6]
        # Actually, with value=5, it merges [4,4] and [6,6] into [4,6].
        
        # Find how many intervals to the right are contiguous with the new range.
        # We start checking from the current idx (which might be the original idx or idx-1).
        # If we merged with idx-1, the next interval to check is the original idx.
        # If we didn't, the next interval to check is the original idx.
        
        # Let's use a pointer to find the end of the merge range.
        # We need to check if intervals[idx].start == new_end + 1.
        # But wait, if we merged with idx-1, the new_end is still 'value'.
        # We need to check if the interval at 'idx' (the one after the merged one) 
        # is contiguous with 'value'.
        
        # Correct logic:
        # The interval at idx-1 (if merged) is now part of the new interval.
        # The interval at idx (if contiguous) is now part of the new interval.
        # We need to find the range of indices [i, j] in self.intervals that 
        # are contiguous with 'value'.
        
        # Let's find the range [left_idx, right_idx] to replace.
        left_idx = idx
        right_idx = idx
        
        # Check if the interval before 'idx' can be merged.
        if idx > 0 and self.intervals[idx - 1][1] + 1 == value:
            left_idx = idx - 1
        
        # Check if the interval at 'idx' and subsequent intervals can be merged.
        # We need to check if intervals[idx].start == value + 1, 
        # or if we merged with idx-1, if intervals[idx].start == value + 1.
        # Actually, if we merged with idx-1, the new_end is still 'value' 
        # until we check the next one.
        
        # Let's simplify:
        # A value 'v' merges with interval [s, e] if s <= v+1 and e >= v-1.
        # Because we are adding one value, we only care about intervals 
        # that are either:
        # 1. [s, v-1]
        # 2. [v+1, e]
        # 3. [s, v]
        # 4. [v, e]
        # 5. [s, e] where s <= v <= e (already handled)
        
        # Let's find all intervals that satisfy: interval.start <= value + 1 
        # AND interval.end >= value - 1.
        
        # Since intervals are disjoint and sorted:
        # The intervals that can merge are a contiguous subsegment of self.intervals.
        
        # Find the first interval that could merge:
        # It's the first interval where interval.end >= value - 1.
        # We can find this using binary search on the 'end' values.
        # Since we don't have a separate list of ends, we'll use a simple search 
        # or bisect on the intervals themselves.
        
        # Let's use the property that intervals are disjoint.
        # The only intervals that can merge with 'value' are:
        # - The interval that contains 'value' (already handled)
        # - The interval ending at 'value - 1'
        # - The interval starting at 'value + 1'
        
        # Find the interval that ends at 'value - 1'
        # Find the interval that starts at 'value + 1'
        
        # Let's use the idx from bisect_left(self.intervals, [value, value])
        # This idx is the first interval where interval.start >= value.
        
        # Potential merge left: idx - 1
        # Potential merge right: idx
        
        start_merge = value
        end_merge = value
        
        # Check left
        if idx > 0 and self.intervals[idx - 1][1] == value - 1:
            start_merge = self.intervals[idx - 1][0]
            idx -= 1 # Start replacing from this interval
            
        # Check right
        # We might merge multiple intervals if they are like [v+1, v+1], [v+2, v+2]...
        # But wait, the problem says "disjoint intervals". 
        # If we have [6, 6] and [7, 7], they are NOT disjoint. 
        # The problem implies the existing intervals are already merged.
        # So we only need to check if the interval at 'idx' starts at 'value + 1'.
        # If it does, we merge it and potentially more.
        
        # Wait, if the existing intervals are already merged, then 
        # there can be at most ONE interval starting at value + 1.
        # Because if there were two, they would have been merged.
        
        # So:
        # 1. Check if idx-1 ends at value-1.
        # 2. Check if idx starts at value+1.
        
        # Let's re-verify:
        # If idx-1 ends at value-1 AND idx starts at value+1:
        #    new_interval = [intervals[idx-1].start, intervals[idx].end]
        #    replace intervals[idx-1] and intervals[idx] with new_interval.
        # If only idx-1 ends at value-1:
        #    new_interval = [intervals[idx-1].start, value]
        #    replace intervals[idx-1] with new_interval.
        # If only idx starts at value+1:
        #    new_interval = [value, intervals[idx].end]
        #    replace intervals[idx] with new_interval.
        # Else:
        #    insert [value, value] at idx.

        # Implementation of this logic:
        
        # We already have idx = bisect_left(self.intervals, [value, value])
        # and we already checked if value is inside intervals[idx-1].
        
        # Check if value is inside intervals[idx]
        if idx < len(self.intervals) and self.intervals[idx][0] <= value <= self.intervals[idx][1]:
            return

        # Check left merge
        merge_left = False
        if idx > 0 and self.intervals[idx - 1][1] == value - 1:
            merge_left = True
            
        # Check right merge
        merge_right = False
        if idx < len(self.intervals) and self.intervals[idx][0] == value + 1:
            merge_right = True
            
        if merge_left and merge_right:
            # Merge both: replace [idx-1] and [idx] with [intervals[idx-1].start, intervals[idx].end]
            new_interval = [self.intervals[idx - 1][0], self.intervals[idx][1]]
            self.intervals[idx - 1 : idx + 1] = [new_interval]
        elif merge_left:
            # Merge left: replace [idx-1] with [intervals[idx-1].start, value]
            self.intervals[idx - 1][1] = value
        elif merge_right:
            # Merge right: replace [idx] with [value, intervals[idx].end]
            self.intervals[idx][0] = value
        else:
            # No merge: insert [value, value] at idx
            self.intervals.insert(idx, [value, value])

    def getIntervals(self) -> list[list[int]]:
        """
        Returns the current list of disjoint intervals.

        Returns:
            A list of [start, end] pairs.
        """
        return self.intervals

def solve():
    """
    Example usage of the SummaryRanges class.
    """
    summary_ranges = SummaryRanges()
    summary_ranges.addNum(1)
    summary_ranges.addNum(3)
    summary_ranges.addNum(7)
    print(summary_ranges.getIntervals())  # Expected: [[1, 1], [3, 3], [7, 7]]
    
    summary_ranges.addNum(2)
    print(summary_ranges.getIntervals())  # Expected: [[1, 3], [7, 7]]
    
    summary_ranges.addNum(6)
    print(summary_ranges.getIntervals())  # Expected: [[1, 3], [6, 7]]
    
    summary_ranges.addNum(4)
    print(summary_ranges.getIntervals())  # Expected: [[1, 7]]
