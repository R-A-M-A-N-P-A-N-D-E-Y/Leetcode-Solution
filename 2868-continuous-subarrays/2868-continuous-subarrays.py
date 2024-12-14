from collections import deque


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        count = 0
        left = 0
        max_deque = deque()  # Monotonic decreasing deque for max values
        min_deque = deque()  # Monotonic increasing deque for min values

        for right in range(len(nums)):
            # Update the deques for the current element
            while max_deque and nums[right] > nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)

            while min_deque and nums[right] < nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)

            # Shrink the window if the condition is not met
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                # Remove indices out of the current window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Add all valid subarrays ending at `right`
            count += right - left + 1

        return count