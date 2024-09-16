class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []

        for time in timePoints:
            arr.append(int(time[:2])*60 + int(time[3:]))
        
        arr.sort()
        minDif = 24 * 60 - (arr[-1] - arr[0])

        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < minDif:
                minDif = arr[i+1] - arr[i]

        return minDif