class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9 + 7)

        # the number of possible even indices.
        even = (n+1) // 2
        # the number of possible odd indices.
        odd = n // 2

        def backtrack(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = backtrack(x, n//2)
            return (res * res)%mod if n % 2 == 0 else (res * res * x)%mod
        
        # for one even position, there are 5 even numbers possible. [0,2,4,6,8]
        # so how many even numbers possible for n+1 // 2 positions?
        evennumbers = backtrack(5, even)
        # for one odd position, there are 4 prime numbers possible. [2,3,5,7]
        # so how many prime numbers possible for n // 2 positions?
        primenumbers = backtrack(4, odd)

        return (evennumbers * primenumbers) % mod