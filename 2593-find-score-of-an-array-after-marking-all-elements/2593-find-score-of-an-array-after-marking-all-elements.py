class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        # Build a min-heap with (value, index) pairs
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)  # Convert to a min-heap

        score = 0  # Initialize score

        # Process elements in min-heap
        while min_heap:
            num, idx = heapq.heappop(min_heap)  # Get the smallest unprocessed element
            if nums[idx] != -1:  # Process only if not already marked
                score += num
                nums[idx] = -1  # Mark the current index
                if idx > 0 and nums[idx - 1] != -1:
                    nums[idx - 1] = -1  # Mark the left neighbor
                if idx < n - 1 and nums[idx + 1] != -1:
                    nums[idx + 1] = -1  # Mark the right neighbor

        return score
