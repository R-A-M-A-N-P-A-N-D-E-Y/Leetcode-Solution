from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        return max(count, key=count.get)    