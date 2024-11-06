class Solution:
    def prime_factors(self, n: int) -> set:
        factors = set()
        n = abs(n)
        while n % 2 == 0:
            factors.add(2)
            n //= 2

        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i

        if n > 2:
            factors.add(n)

        return set(factors)

    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True

        if max(self.prime_factors(n)) > 5:
            return False

        return True
        

test = Solution()
print(test.prime_factors(-2147483648))
print(test.isUgly(-2147483648))
