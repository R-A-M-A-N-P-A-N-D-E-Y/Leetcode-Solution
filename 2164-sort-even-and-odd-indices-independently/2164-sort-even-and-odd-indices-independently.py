class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for i in range(0, len(nums), 2):
            even.append(nums[i])
        
        for i in range(1, len(nums), 2):
            odd.append(nums[i])

        even.sort()
        odd.sort(reverse=True)
        j = 0

        for i in range(0, len(nums), 2):
            nums[i] = even[j]
            j += 1
        
        j = 0
        for i in range(1, len(nums), 2):
            nums[i] = odd[j]
            j += 1
        
        return nums