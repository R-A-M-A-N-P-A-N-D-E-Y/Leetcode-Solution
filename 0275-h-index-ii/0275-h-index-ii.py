class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        j = n - 1
        i = 0

        while i <= j:
            mid = (j + i) // 2

            if citations[mid] == n - mid:
                return n - mid
    
            elif citations[mid] < n - mid:
                i = mid + 1
    
            else:
                j = mid - 1
    
        return n - i