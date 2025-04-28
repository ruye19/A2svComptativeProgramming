class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n==1 or n==0:
                return 1
            return  n* factorial(n-1)
        num=factorial(n)
        
        count=0
        while num != 1 and num %10 == 0:
            count +=1
            num=num//10
        return count     


    