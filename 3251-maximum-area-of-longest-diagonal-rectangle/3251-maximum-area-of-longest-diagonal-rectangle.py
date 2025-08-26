class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dgnl = 0
        area = 0

        for i in range(len(dimensions)):
            if sqrt(dimensions[i][0]**2 + dimensions[i][1]**2) > dgnl:
                dgnl = sqrt(dimensions[i][0]**2 + dimensions[i][1]**2)
                area = dimensions[i][0] * dimensions[i][1]
            elif sqrt(dimensions[i][0]**2 + dimensions[i][1]**2) == dgnl:
                if area < dimensions[i][0] * dimensions[i][1]:
                    area = dimensions[i][0] * dimensions[i][1]
        
        return area