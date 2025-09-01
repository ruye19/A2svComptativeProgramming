class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        result = pow(x , n // 2 )
        result **= 2
        if n % 2:
            result *= x
        return result     

