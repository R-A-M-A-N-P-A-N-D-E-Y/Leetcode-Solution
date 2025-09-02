class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda p: (p[0], -p[1]))
        count = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0]:
                    if points[i][-1] > points[j][-1]:
                        brk = False
                        for a in range(i + 1, j):
                            if points[i][0] == points[a][0]:
                                if points[i][-1] >= points[a][-1] and points[a][-1] >= points[j][-1]:
                                    brk = True
                                    break
                        if not brk:
                            count += 1
                elif points[i][-1] == points[j][-1]:
                    if points[i][0] < points[j][0]:
                        brk = False
                        for a in range(i + 1, j):
                            if points[i][-1] == points[a][-1]:
                                if points[i][0] <= points[a][0] and points[a][0] <= points[j][0]:
                                    brk = True
                                    break
                        if not brk:
                            count += 1
                elif points[i][0] < points[j][0]:
                    if points[i][-1] > points[j][-1]:
                        brk = False
                        for a in range(i + 1, j):
                            if points[i][0] <= points[a][0] and points[a][0] <= points[j][0]:
                                if points[i][-1] >= points[a][-1] and points[a][-1] >= points[j][-1]:
                                    brk = True
                                    break
                        if not brk:
                            count += 1
            
        return count

