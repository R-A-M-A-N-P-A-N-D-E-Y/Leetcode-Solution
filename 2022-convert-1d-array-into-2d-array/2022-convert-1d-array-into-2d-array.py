class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        res = []
        ele = 0
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(original[ele])
                ele += 1
            res.append(temp)
        
        return res