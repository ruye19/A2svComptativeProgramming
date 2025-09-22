class Solution:
    def fib(self, n: int) -> int:
        memo = []
        # if memo[n] in memo:
        #     return memo
        if n == 0:
            return 0
        if n == 1:
            return 1

        # memo[n] = fib(n - 1) + fib(n - 2)        
        return self.fib(n - 1) + self.fib(n - 2)        
        