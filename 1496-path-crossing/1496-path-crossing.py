class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        l = [[0, 0]]

        for d in path:
            if d == "N":
                x += 1
                if [x, y] in l:
                    return True 
                l.append([x, y])
            elif d == "E":
                y += 1
                if [x, y] in l:
                    return True
                l.append([x, y])
            elif d == "W":
                y -= 1
                if [x, y] in l:
                    return True 
                l.append([x, y])
            else:
                x -= 1
                if [x, y] in l:
                    return True 
                l.append([x, y])
        
        return False