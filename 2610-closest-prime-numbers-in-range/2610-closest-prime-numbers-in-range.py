class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left == 1:
            left = 2
        primes = SieveOfEratosthenes(left, right)

        m = 10 ** 6
        a = 0
        b = 0
        print(primes)
        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < m:
                m = primes[i] - primes[i - 1]
                a = primes[i-1]
                b = primes[i]

        return [a, b] if len(primes) > 1 else [-1, -1]

def SieveOfEratosthenes(left: int, num: int) -> List[int]:
    prime = [True for i in range(num+1)]
    p = 2

    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    
    res = []
    for p in range(left, num+1):
        if prime[p]:
            res.append(p)

    return res