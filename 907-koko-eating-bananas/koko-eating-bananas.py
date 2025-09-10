class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validate(speed):
            hours = 0 
            for pile in piles:
                hours += ceil(pile / speed)
            return hours <= h     
                
        left, right = 1, max(piles)  
        while left <= right:
            mid = (left + right) // 2
            if not validate(mid):     
                left = mid + 1
            else:
                right = mid - 1
        return left               