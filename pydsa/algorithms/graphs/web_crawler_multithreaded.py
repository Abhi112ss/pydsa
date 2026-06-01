METADATA = {
    "id": 1242,
    "name": "Web Crawler Multithreaded",
    "slug": "web-crawler-multithreaded",
    "category": "Concurrency",
    "aliases": [],
    "tags": ["bfs", "concurrency", "hash_set", "multithreading"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Implement a multithreaded web crawler that fetches URLs from a starting URL within the same hostname.",
}

import threading
from queue import Queue
from collections import deque

class HtmlParser:
    """
    This class is provided by LeetCode.
    """
    def getUrls(self, url: str) -> list[str]:
        pass

class Solution:
    def crawl(self, htmlParser: HtmlParser, startUrl: str, maxDepth: int) -> list[str]:
        """
        Crawls URLs starting from startUrl up to maxDepth using multiple threads.

        Args:
            htmlParser: An object with a getUrls method to fetch URLs from a page.
            startUrl: The initial URL to start crawling from.
            maxDepth: The maximum depth to crawl.

        Returns:
            A list of all unique URLs found within the same hostname and maxDepth.

        Examples:
            >>> parser = MockParser(["http://news.com/a", "http://news.com/b", "http://other.com/c"])
            >>> sol = Solution()
            >>> sol.crawl(parser, "http://news.com/a", 1)
            ["http://news.com/a", "http://news.com/b"]
        """
        # Extract hostname to ensure we stay within the same domain
        hostname = startUrl.split('/')[2]
        
        # Thread-safe set to keep track of visited URLs
        visited = {startUrl}
        visited_lock = threading.Lock()
        
        # Queue for BFS: stores tuples of (url, current_depth)
        queue = Queue()
        queue.put((startUrl, 0))
        
        # Results list and a lock to protect it
        results = [startUrl]
        results_lock = threading.Lock()
        
        # Counter to track active tasks to know when to stop the worker threads
        # We use a lock to safely increment/decrement this counter
        active_tasks = 0
        tasks_lock = threading.Lock()
        
        # Condition variable to notify workers when new tasks are added or all tasks are done
        condition = threading.Condition(tasks_lock)

        def worker():
            nonlocal active_tasks
            while True:
                with condition:
                    # Wait until there is a task in the queue or no more tasks are being processed
                    while queue.empty() and active_tasks > 0:
                        condition.wait()
                    
                    # If queue is empty and no more tasks are being processed, exit thread
                    if queue.empty() and active_tasks == 0:
                        condition.notify_all()
                        return
                    
                    # If queue is empty but tasks are still active, we might need to wait
                    if queue.empty():
                        continue
                        
                    url, depth = queue.get()
                    active_tasks += 1

                # Perform the network-intensive operation outside the lock
                try:
                    if depth < maxDepth:
                        new_urls = htmlParser.getUrls(url)
                        for next_url in new_urls:
                            # Check if URL belongs to the same hostname and hasn't been visited
                            if next_url.split('/')[2] == hostname:
                                with visited_lock:
                                    if next_url not in visited:
                                        visited.add(next_url)
                                        with results_lock:
                                            results.append(next_url)
                                        
                                        # Add new URL to queue and increment active task count
                                        with condition:
                                            queue.put((next_url, depth + 1))
                                            condition.notify()
                finally:
                    # Decrement active tasks and notify others that a task is completed
                    with condition:
                        active_tasks -= 1
                        queue.task_done()
                        condition.notify_all()

        # Use a fixed number of worker threads (e.g., 10)
        num_threads = 10
        threads = []
        for _ in range(num_threads):
            t = threading.Thread(target=worker)
            t.start()
            threads.append(t)

        # Wait for all threads to finish
        for t in threads:
            t.join()

        return results
