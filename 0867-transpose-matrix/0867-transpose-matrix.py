class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ds = ls = []
        for i in range(len(matrix[0])):
            ls = []
            for j in range(len(matrix)):
                ls.append(matrix[j][i])
            ds.append(ls)

        return ds