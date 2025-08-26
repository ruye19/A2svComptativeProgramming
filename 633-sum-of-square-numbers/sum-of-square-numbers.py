class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0 
        high = int(sqrt(c))
        while low <=  high:
            if low * low + high * high < c:
                low += 1
            elif   low * low + high * high > c: 
                high -= 1
            else:
                return True          
        return False        

        
        