class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total = 0
        for ele in customers:
            if ele == 'Y':
                total += 1
        
        ans = 0
        mini = total

        for i in range(len(customers)):
            if customers[i] == 'Y':
                total -= 1
            if customers[i] == 'N':
                total += 1
            if total < mini:
                mini = total
                ans = i + 1
        
        return ans
