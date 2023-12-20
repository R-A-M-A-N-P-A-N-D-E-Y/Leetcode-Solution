class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        m1 = min(prices)
        if m1 > money:
            return money
        else:
            prices.remove(m1)
        m2 = min(prices)

        if m1+m2 > money:
            return money
        else:
            return money-(m1+m2)