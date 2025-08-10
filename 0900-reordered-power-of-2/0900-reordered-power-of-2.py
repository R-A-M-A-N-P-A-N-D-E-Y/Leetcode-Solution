class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        def get_sign(num):
            sign = 1
            while num > 0:
                sign *= prime[num % 10]
                num //= 10
            return sign

        target_sign = get_sign(n)
        for i in range(31):
            if get_sign(1 << i) == target_sign:
                return True
        return False
