class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count = Counter(nums)
        good_pairs = 0
        for i, n in count.items():
            good_pairs += int((n*(n-1))/2)
        
        return good_pairs