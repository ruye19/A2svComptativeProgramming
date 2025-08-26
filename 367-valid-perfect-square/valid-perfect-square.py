class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0 
        high = num
        while low <=  high:
            mid = (high + low) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1     
        return False        

        