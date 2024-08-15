class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = [0, 0, 0]
            
        for ele in bills:
            if ele == 5:
                count[0] += 1
            elif ele == 10:
                count[1] += 1
                if count[0] > 0:
                    count[0] -= 1
                else:
                    return False
            else:
                count[2] += 1
                if count[1] > 0 and count[0] > 0:
                    count[1] -= 1
                    count[0] -= 1
                elif count[0] >= 3:
                    count[0] -= 3
                else:
                    return False
        
        return True
