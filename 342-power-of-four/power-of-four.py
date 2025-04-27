class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def isfour(n):
            if n==1:
                return True
            if n<1:
               return False        
            return isfour(n/4)
           
        return isfour(n)           
        