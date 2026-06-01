METADATA = {
    "id": 3709,
    "name": "Design Exam Scores Tracker",
    "slug": "design_exam_scores_tracker",
    "category": "Design",
    "aliases": [],
    "tags": ["heap", "hash_map", "design"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Design a system to track exam scores for students and retrieve the top k scores efficiently.",
}

import heapq

class ExamScoresTracker:
    """
    A system to track student exam scores and retrieve top scores.
    
    Uses a max-heap to store scores and a hash map to track the current 
    valid score for each student to handle updates via lazy deletion.
    """

    def __init__(self):
        """Initializes the tracker with empty data structures."""
        # Maps student_id -> current_score
        self.student_scores: dict[int, int] = {}
        # Max-heap storing (-score, student_id) to simulate max-heap using heapq
        self.score_heap: list[tuple[int, int]] = []

    def update_score(self, student_id: int, score: int) -> None:
        """
        Updates or sets the score for a given student.

        Args:
            student_id: The unique identifier for the student.
            score: The new score to assign to the student.
        """
        self.student_scores[student_id] = score
        # Push the new score into the heap. 
        # We use negative score because heapq is a min-heap.
        heapq.heappush(self.score_heap, (-score, student_id))

    def get_top_k_scores(self, k: int) -> list[int]:
        """
        Retrieves the top k highest scores currently in the system.

        Args:
            k: The number of top scores to retrieve.

        Returns:
            A list of the top k scores in descending order.
        """
        top_scores: list[int] = []
        temp_storage: list[tuple[int, int]] = []

        # Extract elements from the heap until we find k valid scores
        while len(top_scores) < k and self.score_heap:
            neg_score, student_id = heapq.heappop(self.score_heap)
            current_score = -neg_score

            # Lazy Deletion: Check if this score is still the current score for the student
            if student_id in self.student_scores and self.student_scores[student_id] == current_score:
                top_scores.append(current_score)
                # Keep track of valid scores we popped to put them back later
                temp_storage.append((neg_score, student_id))
            else:
                # This is a stale score (an old update), simply discard it
                continue

        # Re-insert the valid scores we extracted back into the heap
        for item in temp_storage:
            heapq.heappush(self.score_heap, item)

        return top_scores

def solve():
    """
    Example usage of the ExamScoresTracker.
    """
    tracker = ExamScoresTracker()
    tracker.update_score(1, 85)
    tracker.update_score(2, 95)
    tracker.update_score(3, 70)
    tracker.update_score(1, 90)  # Update student 1 from 85 to 90
    
    # Expected: [95, 90]
    print(tracker.get_top_k_scores(2))
    
    tracker.update_score(3, 100) # Update student 3 from 70 to 100
    # Expected: [100, 95]
    print(tracker.get_top_k_scores(2))
