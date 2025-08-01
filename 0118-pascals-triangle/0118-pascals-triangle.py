class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            output = [[1], [1,1]]
            for i in range(2, numRows):
                temp = [1]
                for j in range(len(output[-1]) - 1):
                    temp.append(output[-1][j] + output[-1][j+1])
                temp.append(1)
                output.append(temp)
        
        return output