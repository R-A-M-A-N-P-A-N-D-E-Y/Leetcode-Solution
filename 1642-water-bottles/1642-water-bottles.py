class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # ans = numBottles
        # rem = 0

        # while (numBottles + rem) // numExchange > 0:
        #     numBottles = (numBottles + rem) // numExchange
        #     ans += numBottles
        #     rem = (numBottles % numExchange) + (numBottles // numExchange)
        
        return numBottles + ((numBottles - 1) // (numExchange - 1))