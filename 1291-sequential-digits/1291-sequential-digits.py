class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        start , end = len(str(low)), len(str(high))
        firstnum = low//(10**(start-1))
        res = []
        num = []
        
        num = [0]*start
        num[0] = firstnum
        for j in range(1, start):
            num[j] = num[j-1] + 1
        no = int(''.join(map(str, num)))
        if no < low:
                for j in range(start):
                    num[j] = num[j] + 1
                no = int(''.join(map(str, num)))
        
        for i in range(start+1, end+2):  
            while no <= high and all((num[i] == num[i - 1] + 1 and num[i] <= 9) for i in range(1, i-1)):
                res.append(no)
                for j in range(i-1):
                    num[j] = num[j] + 1
                no = int(''.join(map(str, num)))
            
            num = [0]*i
            num[0] = 1
            for j in range(1, i):
                num[j] = num[j-1] + 1
            no = int(''.join(map(str, num)))
                
        return res